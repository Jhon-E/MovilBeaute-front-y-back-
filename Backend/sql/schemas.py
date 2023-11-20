from pydantic import BaseModel
from typing import List, Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    name: str
    
class Uservalid(BaseModel):
    email: EmailStr
    password: str
    
class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class StylistBase(BaseModel):
    email: EmailStr
    name: str
    profession: str

class StylistCreate(StylistBase):
    password: str

class Stylist(StylistBase):
    id: int

    class Config:
        orm_mode = True
