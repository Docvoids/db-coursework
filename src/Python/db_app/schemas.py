from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    profile_picture: Optional[str] = None
    status: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    profile_picture: Optional[str] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True
