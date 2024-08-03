from sqlalchemy import Column, Integer, String
from webapp.models.base.root_entity import RootEntity


class Game(RootEntity):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=False)
    registry_url = Column(String, nullable=False)
