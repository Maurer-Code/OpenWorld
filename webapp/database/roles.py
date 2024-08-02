from webapp import db
from webapp.database.base import Base

import numpy as np



class Role(Base):

    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    settings = db.Column(db.Integer, default=0)


    def __init__(self, name):
        self.name = name

    def update_modification_date(self):
        pass
        #self.modified_on = datetime.now().replace(microsecond=0)
        #db.session.commit()

    def get_admin_rights(self) -> bool:
        return np.base_repr(self.settings, padding=0)[-Index['Admin']] == '1'

    def get_bool(self, index) -> bool:
        return np.base_repr(self.settings, padding=0)[-index] == '1'

    def get_values(self) -> list:

        return [bool(self.settings & (1 << n)) for n in range(len(Index.keys()))]

    def get_keys(self) -> list:
        return list(Index.keys())

    def __repr__(self):
        return f'<Role {self.name}>'
