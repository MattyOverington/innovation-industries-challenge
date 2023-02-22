from email.policy import default
from sqlalchemy import Column, ForeignKey, Boolean, Float, Integer, String, Date, func, or_, and_
from sqlalchemy.orm import relationship, object_session
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
import datetime as dt

from sqlalchemy.sql.sqltypes import VARCHAR

from app import utils
from app.db.base import Base
from enum import IntEnum

class Job(Base):
	id = Column(Integer, primary_key=True, index=True)
	client = Column(String)
	description = Column(String)
	completed=Column(Boolean)
	cost=Column(Integer)
	lead = Column(Integer, ForeignKey("Employee.id"))
	sqlite_autoincrement=True
