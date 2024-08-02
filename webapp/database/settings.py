from webapp import db
from webapp.database.base import Base


class Settings(Base):

    __tablename__ = 'settings'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    editor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    editor = db.relationship('User', backref='settings')

    def __repr__(self):
        return f'<Settings {self.name}>'
