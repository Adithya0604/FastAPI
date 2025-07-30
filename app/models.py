from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base

class UploadDocument(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    document = Column(Text)
    
    questions = relationship('DocumentQuestion', back_populates='document')

class DocumentQuestion(Base):
    __tablename__ = 'DocumentsQuestions'
    
    id = Column(Integer, primary_key=True, index=True)
    documentId = Column(Integer, ForeignKey("documents.id"))
    documentQuestions = Column(Text)
    questionStatus = Column(String(10), default='pending')
    
    document = relationship('UploadDocument', back_populates='questions')