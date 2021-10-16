from sqlalchemy import Column, Integer, String, DateTime, JSON

from database import Base


class Election(Base):
    __tablename__ = "election"

    id                  = Column(Integer, primary_key=True, index=True)
    name                = Column(String, unique=True)
    from_date           = Column(DateTime)
    to_date             = Column(DateTime)
    num_of_votes        = Column(Integer, default=True)
    choices             = Column(JSON, default=True)

class Code(Base):
    __tablename__ = "code"

    id                  = Column(Integer, primary_key=True, index=True)
    code                = Column(String, unique=True)