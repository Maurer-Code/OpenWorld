from webapp import db
from webapp.database.base import Base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime


class User(UserMixin, Base):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    image = db.Column(db.String(100))
    position = db.Column(db.String(50))
    department = db.Column(db.String(50))

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref='user')

    active = db.Column(db.Boolean)


    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def update_last_login(self, remember_me):
        self.remember_me = remember_me
        self.last_login = datetime.now().replace(microsecond=0)
        db.session.commit()

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'



