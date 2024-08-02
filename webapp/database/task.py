from webapp import db
from webapp.database.base import Base


class Task(Base):

    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    repository = db.Column(db.String(100), nullable=False)

    editor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    editor = db.relationship('User', backref='project')

    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    assignee = db.relationship('User', backref='project')

    def __repr__(self):
        return f'<Task {self.name}>'
