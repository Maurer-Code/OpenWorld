
from sqlalchemy import Column, Integer, String, Boolean
from webapp.models.base.root_entity import RootEntity


class Users(RootEntity):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String(150), unique=True)
    password = Column(String, nullable=False)
    enabled = Column(Boolean, default=False)