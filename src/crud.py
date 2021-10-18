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

    #check if hash is valid
    hash_query = db.query(models.Code).filter(models.Code.code == hash_code)
    hash_orm = hash_query.first()
    if not hash_orm is not None:
        print("Hash invalid")
        return None

    # load election
    election_query = db.query(models.Election) \
                    .filter(models.Election.id == hash_orm.election_id)
    election_orm =  election_query.first()
    
    if election_orm is None:
        print("Election not Found")
        return None

    # check if now is in the allowed timespan
    now = datetime.today()
    allowed = election_orm.from_date < now and election_orm.to_date > now
    if not allowed:
        print("Date invalid")
        return None

    # check if the vote is valid
    allowed = utils.is_valid_choice(electionChoice=election_orm.choices,userChoice=vote.choice)
    if not allowed:
        print("Vote invalid")
        return None

    # create Vote
    vote_orm = models.Vote(
        choice = vote.choice,
        election_id = hash_orm.election_id
    )
    db.add(vote_orm)
    db.commit()
    db.refresh(vote_orm)

    #remove hash
    hash_query.delete()
    db.commit()

    return vote_orm