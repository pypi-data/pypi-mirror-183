from typing import Optional
from hashlib import blake2b
from pydantic import BaseModel, validator
from datetime import datetime
from libs.auth.password import Password


class UserDataBase(BaseModel):
    fullname: str
    email: str
    username: Optional[str] = ""
    whatsapp: str = ""
    password: str = ""
    lastlogin: datetime = datetime.now()
    role: Optional[str] = "user"
    meta_resetkey: Optional[str] = ""
    avatar: Optional[str] = ""
    is_verified: Optional[bool] = False
    status: Optional[str] = "inactive"
    regcode: Optional[str] = ""
    id: Optional[int]
    # created_at: Optional[datetime] = datetime.now()
    # updated_at: Optional[datetime] = datetime.now()

    @validator("password", always=True, check_fields=False)
    def set_pass(cls, v):
        t = Password().get_password_hash(v)
        return t

    @validator("username", always=True, check_fields=False)
    def set_username(cls, v, values):
        m = values["email"]
        h = blake2b(digest_size=4)
        h.update(m.encode("utf-8"))
        t = h.hexdigest()
        return f"u{str(t)}"

    @validator("lastlogin", always=True, check_fields=False)
    def set_lastlogin(cls, v, values):
        return datetime.now()

    class Config:
        orm_mode = True
