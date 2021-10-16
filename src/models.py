from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from database import Base


class Election(Base):
    __tablename__ = "election"

    id                  = Column(Integer, primary_key=True, index=True)
    name                = Column(String)
    from_date           = Column(DateTime)
    to_date             = Column(DateTime)
    num_of_votes        = Column(Integer, default=True)
    choices             = Column(JSON, default=True)

    votes               = relationship("Vote")

class Code(Base):
    __tablename__ = "code"

    id                  = Column(Integer, primary_key=True, index=True)
    code                = Column(String, unique=True)


class Vote(Base):
    __tablename__ = "vote"

    id                  = Column(Integer, primary_key=True, index=True)
    choice              = Column(Integer)
    election_id         = Column(Integer, ForeignKey('election.id'))

    election            = relationship("Election", back_populates="votes")