from random import choice
from sqlalchemy.orm import Session

import models, schemas, utils

def get_election(db: Session, election_id: int):
    return    db.query(models.Election) \
                .filter(models.Election.id == election_id) \
                .first()

def create_election(db: Session, election: schemas.ElectionCreate):
    db_election = models.Election(
        name=election.name,
        from_date=election.from_date,
        to_date=election.to_date,
        num_of_votes=election.num_of_votes,
        choices=election.choices
    )
    db.add(db_election)
    db.commit()
    db.refresh(db_election)
    return db_election


def create_code(db: Session):
    #generate unique hash
    found_unused_hash = False
    while not found_unused_hash:
        hash = utils.generate_ranodm_Hash()
        #check if hash already exists
        q = db.query(models.Code) \
              .filter(models.Code.code == hash)
        found_unused_hash = db.query(q.exists())

    #store Code model into database
    db_code = models.Code(
        code=hash
    )
    db.add(db_code)
    db.commit()
    db.refresh(db_code)
    return db_code

def create_vote(db: Session, vote: schemas.VoteCreate):
    db_vote = models.Vote(
        choice=vote.choice,
        election_id=vote.election_id
    )
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote