from datetime import datetime
from pydantic import BaseModel
from typing import List

class CodeBase(BaseModel):
    code: str

class CodeCreate(BaseModel):
    election_id: int

class Code(CodeBase):
    id: int
    election_id: int

    class Config:
        orm_mode = True




class VoteBase(BaseModel):
    choice: dict

class VoteCreate(VoteBase):
    pass

class Vote(VoteBase):
    id: int
    election_id: int

    class Config:
        orm_mode = True



class ElectionBase(BaseModel):
    name: str
    from_date: datetime
    to_date: datetime
    num_of_votes: int
    choices: List[str]

class ElectionCreate(ElectionBase):
    pass

class Election(ElectionBase):
    id: int
    votes: List[Vote] = []
    codes: List[Code] = []

    class Config:
        orm_mode = True
