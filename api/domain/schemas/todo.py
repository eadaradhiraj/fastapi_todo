from api.domain.schemas.schema_base import SchemaBase


class TodoBase(SchemaBase):
    """your code goes here"""
    description: str
    user_id: int


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    class Config:
        orm_mode = True


class TodoResponse(Todo):
    pass