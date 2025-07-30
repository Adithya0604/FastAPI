# FastAPI

# Async Document Q&A Microservice with Mock LLM
A backend microservice built with FastAPI and PostgreSQL that lets users upload documents, ask questions about them, and receive simulated answers asynchronously—mimicking a real-world LLM-powered document Q&A service.

# 🚀 Features
1. Document Upload: Store documents with title and content.

2. Q&A: Ask questions about uploaded documents.

3. Async Answers: Simulate LLM answer generation in the background.

4. Status Tracking: Query the processing status and get answers.

5. Tech Stack: FastAPI, PostgreSQL, async SQLAlchemy, type annotations, clean modular code.

# Setup Instructions
1. Clone the Repository
 --> git clone https://github.com/Adithya0604/FastAPI.git
 --> cd FastAPI

2. Prepare the Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Setup SqlAlchemy
Install PostgreSQL.

Create a database 

5. Start the Development Server
uvicorn app.main:app --reload

# After starting the server, you can explore and test all APIs interactively using the automatically generated Swagger interface:

http://127.0.0.1:8000/docs

# API Endpoints
Endpoint	Method	Description
/documents/	POST	Upload a new document (title, content)
/documents/{id}	GET	Retrieve a document by ID
/documents/{id}/question	POST	Ask a question about a document
/questions/{id}	GET	Retrieve Q&A status and answer#

# Project Structure

FastAPI
  |_ requirments.txt
  |_ README.md
  |_ app/
     |_ venv
     |_ models.py – DB models
     |_ main.py – FastAPI EntryPoint
     |_ Init_db.py – Tables Creation
     |_ __init__.py  – Package file for app
     |_ database  - DB Folder
           |__ db.py - database File
           |__ __init__.py. - Package file for DB
   
