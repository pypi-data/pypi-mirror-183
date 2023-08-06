from pydantic import BaseModel, Field
from typing import Optional


class ReqUserCreate(BaseModel):
    email: str = Field(..., description="Email")
    fullname: str = Field(..., description="Fullname")
    status: Optional[str] = "active"

    class Config:
        orm_mode = True
