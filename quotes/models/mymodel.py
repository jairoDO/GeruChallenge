from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime
)

from .meta import Base

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)


class SessionModel(Base):
    __tablename__= '_session'
    id = Column(Integer, primary_key=True, autoincrement=True)
    identifier = Column(Text)
    datetime = Column(DateTime)
    page = Column(Text)

    def __init__(self, identifier, datetime, page):
        self.identifier = identifier
        self.datetime = datetime
        self.page = page

    def to_json(self):
        return {'id': self.id,
                'identifier': self.identifier,
                'datetime': self.datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'page': self.page}

Index('my_index', MyModel.name, unique=True, mysql_length=255)
Index('my_session_index', SessionModel.id, unique=True, mysql_length=255)
