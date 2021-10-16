from datetime import datetime
from pydantic import BaseModel
from typing import List


class ElectionBase(BaseModel):
    name: str
    from_date: datetime
    to_date: datetime
    num_of_votes: int
    choices: dict

class ElectionCreate(ElectionBase):
    pass

class Election(ElectionBase):
    id: int

    class Config:
        orm_mode = True

class CodeBase(BaseModel):
    code: str

class CodeCreate(CodeBase):
    pass

class Code(CodeBase):
    id: int

    class Config:
        orm_mode = True