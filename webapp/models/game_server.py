from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from webapp.models.base.root_entity import RootEntity
from webapp.models.enum.game_server_state import GameServerState


class GameServer(RootEntity):
    __tablename__ = 'game_server'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'), nullable=False)
    game = relationship("Game")
    member_group_id = Column(Integer, ForeignKey('group_members.id'), nullable=False)
    group_members = relationship("GroupMembers")
    container_id = Column(String, nullable=False)
    status = Column(Enum(GameServerState), nullable=False)
