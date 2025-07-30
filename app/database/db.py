from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Using SQLite database
DATABASE_URL = "sqlite:///./fastapi.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # Needed only for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # from autocommit=false <--> true

Base = declarative_base()
