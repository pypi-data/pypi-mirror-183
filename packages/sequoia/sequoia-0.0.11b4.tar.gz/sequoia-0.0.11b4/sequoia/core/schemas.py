from typing import Optional, Union
from pydantic import BaseModel, validator


class CommonParams(BaseModel):
    page: Optional[int] = 1
    limit: Optional[int] = 15
    offset: Optional[int] = 0
    q: Optional[Union[int, str]] = None
    order: Optional[str] = "asc"
    order_by: Optional[str] = "id"

    @validator("limit", always=True, check_fields=False)
    def set_limit(cls, v):
        if v > 100:
            return 100
        else:
            return v

    @validator("offset", always=True, check_fields=False)
    def set_offset(cls, v, values):
        return int((values["page"] - 1) * values["limit"])

    # class Config:
    #     orm_mode = True
