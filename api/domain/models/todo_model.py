from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from api.domain.models.model_base import ModelBase


class TodoModel(ModelBase):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    time_created = Column(DateTime(timezone=False), server_default=func.now())
    user = relationship('UserModel', back_populates='todos')
