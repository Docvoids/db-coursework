from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "mysql+mysqlconnector://root:8642qwer@localhost:3306/proman_roman"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()

# Dependency for database session
def get_db():
    """
    Provides a SQLAlchemy database session.
    Ensures proper closing of the session after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()