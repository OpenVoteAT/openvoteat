from datetime import datetime
from pydantic import BaseModel
from typing import List




class Election(BaseModel):

    id: int
    name: str
    from_date: datetime
    to_date: datetime
    num_of_votes: int
    choices: dict

    class Config:
        orm_mode = True