from app.database.db import Base, engine
from app.models import User


print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Database created!")
