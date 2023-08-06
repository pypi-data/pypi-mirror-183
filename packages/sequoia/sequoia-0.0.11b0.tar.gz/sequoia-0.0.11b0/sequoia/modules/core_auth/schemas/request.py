from pydantic import BaseModel, Field
from typing import Optional


class ReqUserLogin(BaseModel):
    email: str = Field(..., description="Email")
    password: str

    class Config:
        orm_mode = True


class ReqUserCreate(BaseModel):
    email: str = Field(..., description="Email")
    fullname: str = Field(..., description="Fullname")
    status: Optional[str] = "active"

    class Config:
        orm_mode = True


class ReqForgotPassword(BaseModel):
    email: str = Field(..., description="Email")

    class Config:
        orm_mode = True
