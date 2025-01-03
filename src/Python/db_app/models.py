from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    profile_picture = Column(String(255), nullable=True)
    status = Column(String(16), nullable=True)