from sqlalchemy import Integer, Column, String

from app.infrastructure.db.database import Base


class DbNic(Base):
    __tablename__ = 'nic'
    id: int | Column = Column(Integer, primary_key=True, index=True)
    uuid: str | Column = Column(String)
    num: str | Column = Column(String)
    type: str | Column = Column(String)


class DbUser(Base):
    __tablename__ = 'user'
    id: int | Column = Column(Integer, primary_key=True, index=True)
    uuid: str | Column = Column(String)
    name: str | Column = Column(String)
    lastname: str | Column = Column(String)
    email: str | Column = Column(String)
