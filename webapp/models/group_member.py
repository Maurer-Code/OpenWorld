from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from webapp.models.base.root_entity import RootEntity


class GroupMember(RootEntity):
    __tablename__ = 'group_member'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("Users")
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    groups = relationship("Groups")
