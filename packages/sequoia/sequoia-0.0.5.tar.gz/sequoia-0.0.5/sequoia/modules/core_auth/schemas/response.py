from pydantic import BaseModel
from typing import Optional


class ResLogin(BaseModel):
    id: int
    email: str = ""
    fullname: str = ""
    role: str = ""
    status: str = ""
    token: str = ""

    class Config:
        orm_mode = True


class ResMe(BaseModel):
    id: int
    email: str = ""
    fullname: str = ""
    role: str = ""
    status: str = ""
    whatsapp: str = ""
    alamat: Optional[list] = []

    class Config:
        orm_mode = True
