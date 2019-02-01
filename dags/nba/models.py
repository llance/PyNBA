from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, Boolean,  DateTime, Float, ForeignKey

Base = declarative_base(metadata=MetaData(schema='nba_api'))

class Teams(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    abbreviation = Column(String)
    nickname = Column(String)
    city = Column(String)
    state = Column(String)
    year_founded = Column(Integer)

    def __repr__(self):
        return "<Teams(name='%s')>" % (self.name)