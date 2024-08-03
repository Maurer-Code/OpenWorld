from flask_sqlalchemy.model import Model
from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, inspect


class RootEntity(Model):
    __abstract__ = True

    deleted = Column(Boolean, nullable=False, default=False)
    created_by_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_date = Column(DateTime, nullable=False)
    changed_by_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    last_modified = Column(DateTime, nullable=False)

    def _as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def set_with_dict(self, dataset: dict):
        key_words = self.__table__.columns.keys()

        filtered_dataset = {key: dataset[key] for key in key_words if key in dataset} if key_words else dataset

        for key, value in filtered_dataset.items():
            setattr(self, key, value)
