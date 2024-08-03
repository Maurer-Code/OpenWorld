from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from webapp.models.base.root_entity import RootEntity


class GroupAuthoritie(RootEntity):
    __tablename__ = 'group_authoritie'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    groups = relationship("Groups")
    authority = Column(String, nullable=False)
