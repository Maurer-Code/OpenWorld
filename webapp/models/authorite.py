from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from webapp.models.base.root_entity import RootEntity


class Authoritie(RootEntity):
    __tablename__ = 'authoritie'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    users = relationship("Users")
    authority = Column(String, nullable=False)
