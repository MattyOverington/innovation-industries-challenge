from app import schemas
from .base import Base
from typing import List


class Job(Base):
    id : int = None
    client : str = None
    description : str = None
    completed : bool = None
    cost : int = None
    lead : int = None
