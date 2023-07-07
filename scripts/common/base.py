# Import the modules required
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

# Create the engine
engine = create_engine("postgresql+psycopg2://dcstudent:S3cretPassw0rd@localhost:5432/campdata-prod")

# Initialize the session
session = Session(engine)

# Initialize the declarative base
Base = declarative_base()
