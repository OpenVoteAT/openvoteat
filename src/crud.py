from sqlalchemy.orm import Session

import models, schemas

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