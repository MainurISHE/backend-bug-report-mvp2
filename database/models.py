from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(String)
    email = Column(String)
    password = Column(String)


class BugReport(Base):
    __tablename__ = "bug_reports"

    id = Column(Integer, primary_key=True)

    email = Column(String)

    author = Column(String)

    release_build = Column(String)

    fixed_by = Column(String)

    description = Column(Text)

    priority = Column(String)

    severity = Column(String)