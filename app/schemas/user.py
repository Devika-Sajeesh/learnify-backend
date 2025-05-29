from pydantic import BaseModel, constr
from typing import Optional

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=30)
    password: str
    gpa: Optional[float] = None
    branch: Optional[str] = None
    sem: Optional[str] = None

class UserOut(BaseModel):
    id: int
    username: str
    gpa: Optional[float]
    branch: Optional[str]
    sem: Optional[str]
    subin: Optional[str] = None
    subnin: Optional[str] = None


    class Config:
        orm_mode = True
