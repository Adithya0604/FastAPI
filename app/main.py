from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Form
from sqlalchemy.orm import Session
from app.database.db import SessionLocal, Base, engine
import re, base64, asyncio
from app.models import UploadDocument, DocumentQuestion
from fastapi.responses import JSONResponse

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Message": "FastAPI has been started..."}


@app.post("/documents/")
async def uploadDocumentEndpoint(
    title: str = Form(...),
    inputDocument: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    allowedDocumentType = ["application/pdf", "text/plain"]

    if inputDocument.content_type not in allowedDocumentType:
        raise HTTPException(status_code=400, detail="Invalid Document type")

    documentRead = await inputDocument.read()
    documentBase64 = base64.b64encode(documentRead).decode("utf-8")

    convertedDocument = UploadDocument(title=title, document=documentBase64)

    db.add(convertedDocument)
    db.commit()
    db.refresh(convertedDocument)

    return JSONResponse(
        status_code=200, content={"ResponceMessage": "Document Uploaded Sucessfully"}
    )


@app.get("/documents/{id}")
async def retrivingDocument(id: int, db: Session = Depends(get_db)):
    requestedDocument = db.query(UploadDocument).filter(UploadDocument.id == id).first()

    if not requestedDocument:
        raise HTTPException(status_code=400, detail=f"Invalid Document ID: {id}")

    convertedDocument = base64.b64decode(requestedDocument.document)

    return JSONResponse(
        status_code=200, content={"Requested Document": requestedDocument.document}
    )


async def processingQuestion(questionId: int, db: Session = Depends(get_db)):
    await asyncio.sleep(5)

    fetchingQuestion = (
        db.query(DocumentQuestion).filter(DocumentQuestion.id == questionId).first()
    )
    if fetchingQuestion:
        fetchingQuestion.questionStatus = "Answered"
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Question not found")


@app.post("/documents/{id}/question")
async def questionSubmition(id: int, Question: str = Form(...), db: Session = Depends(get_db)):
    requestedDocument = db.query(UploadDocument).filter(UploadDocument.id == id).first()

    if not requestedDocument:
        raise HTTPException(status_code=404, detail={"Invalid Document Id Searching"})

    relatedDocumentQuestion = DocumentQuestion(
        documentId=id, documentQuestions=Question, questionStatus="Pending"
    )

    db.add(relatedDocumentQuestion)
    db.commit()
    db.refresh(relatedDocumentQuestion)

    await asyncio.create_task(processingQuestion(relatedDocumentQuestion.id, db))

    return JSONResponse(
        status_code=200,
        content={
            "Message": f"This is a generated answer to your question: {Question}",
            "status": "pending",
            "question_id": relatedDocumentQuestion.id,
        },
    )


@app.get("/questions/{id}")
def retiveStatus(id, db: Session = Depends(get_db)):
    question = db.query(DocumentQuestion).filter(DocumentQuestion.id == id).first()

    if not question:
        raise HTTPException(
            status_code=404, detail=f"Invalid Question with QuestionId: {id}"
        )

    return JSONResponse(
        status_code=200,
        content={
            "Status": question.questionStatus,
            "Answered": f"This is a generated answer to your question: {question.documentQuestions}",
        },
    )
