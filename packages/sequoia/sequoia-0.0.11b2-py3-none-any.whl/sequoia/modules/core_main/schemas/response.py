from pydantic import BaseModel

# from typing import Optional


class ResUserCreate(BaseModel):
    email: str = ""

    class Config:
        orm_mode = True
