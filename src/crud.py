from random import choice
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
from sqlalchemy.sql.functions import mode
from datetime import datetime

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

def patch_election(db: Session, election_id: int, election: schemas.ElectionCreate):
    election_orm = db.query(models.Election).filter(models.Election.id == election_id)

    election_orm.update(
        values=election.dict()
    )
    election_orm = election_orm.first()

    if election_orm is None:
        return None

    db.commit()
    db.refresh(election_orm)
    return election_orm


def create_code(db: Session, codeCreate: schemas.CodeCreate):
    #generate unique hash
    found_unused_hash = False
    while not found_unused_hash:
        hash = utils.generate_ranodm_hash()
        #check if hash already exists
        found_unused_hash = db.query(models.Code) \
                              .filter(models.Code.code == hash) \
                              .first() is not None

    #store Code model into database
    db_code = models.Code(
        code=hash,
        election_id=codeCreate.election_id
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

def add_vote(db: Session, code: schemas.CodeBase, vote: schemas.VoteCreate):
    # Captcha
    # get the hash
    hash_code = code.code
    # decode hash
        # TODO
    # check the vote
        # TODO
    # check the hash
    hash_db = db.query(models.Code).filter(models.Code.code == hash_code).first()
    allowed = hash_db is not None
    if not allowed:
        return None
    # check if the vote is allowed
    # date
    now = datetime.today()
    election_db = db.query(models.Election) \
                    .filter(models.Election.id == hash_db.election_id) \
                    .filter(models.Election.from_date < now) \
                    .filter(models.Election.to_date > now) \
                    .first()
    allowed = allowed and (election_db is not None)
    if not allowed:
        return None
    # create Vote
    db_vote = models.Vote(
        choice = vote.choice,
        election_id = hash_db.election_id
    )
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote