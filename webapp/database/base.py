

from webapp import db
from sqlalchemy import inspect


class Base(db.Model):

    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


    def _as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


    def set_with_dict(self, dataset: dict):

        key_words = self.__table__.columns.keys()

        filtered_dataset = {key: dataset[key] for key in key_words if key in dataset} if key_words else dataset

        for key, value in filtered_dataset.items():
            setattr(self, key, value)