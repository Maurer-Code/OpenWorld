from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from webapp.models.enum.docker_variable_typ import DockerVariablesTyp
from webapp.models.base.root_entity import RootEntity


class DockerVariable(RootEntity):
    __tablename__ = 'docker_variable'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'), nullable=False)
    variable = Column(String, nullable=False)
    value = Column(String, nullable=False)
    typ = Column(Enum(DockerVariablesTyp), nullable=False)
    is_env = Column(Boolean, default=False)
