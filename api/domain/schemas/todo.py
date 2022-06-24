from api.domain.schemas.schema_base import SchemaBase
from typing import Optional
import datetime

class TodoBase(SchemaBase):
    """your code goes here"""
    description: str
    user_id: int


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: Optional[int] = None
    description: str = None
    time_created: datetime.datetime = None

    class Config:
        orm_mode = True


class TodoResponse(Todo):
    pass
