from sqlalchemy import Column, Integer, String
from webapp.models.base.root_entity import RootEntity


class Group(RootEntity):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    group_name = Column(String, nullable=False)
