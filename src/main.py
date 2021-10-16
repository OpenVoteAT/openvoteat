from typing import List

from fastapi import Depends, FastAPI, HTTPException
from pydantic.schema import schema
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#---------/election-------------
@app.post("/election", response_model=schemas.Election)
def post_election(election: schemas.ElectionCreate ,db: Session = Depends(get_db)):
    return crud.create_election(db, election=election)
#-------------------------------


#---------/election/id----------
@app.get("/election/{election_id}", response_model=schemas.Election)
def get_election(election_id: int ,db: Session = Depends(get_db)):
    return crud.get_election(db, election_id=election_id)

#@app.patch("/election/{election_id}", response_model=schemas.Election)
#def patch_election(election_id: int ,election:schemas.ElectionCreate, db: Session = Depends(get_db)):
#    return crud.patch_election(db, election_id=election_id, election=election)
#-------------------------------

#-------------/vote-------------
@app.post("/vote", response_model=schemas.Vote)
def add_vote(code: schemas.CodeBase, vote: schemas.VoteCreate ,db: Session = Depends(get_db)):
    return crud.add_vote(db,code=code,vote=vote)
#-------------------------------


#------------TEST---------------


#-------------/code-------------
@app.post("/code", response_model=schemas.Code)
def post_code(codeCreate: schemas.CodeCreate ,db: Session = Depends(get_db)):
    return crud.create_code(db, codeCreate=codeCreate)
#-------------------------------

