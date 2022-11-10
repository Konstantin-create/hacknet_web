from app import db
from datetime import datetime


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<Admin {self.id} - {self.username}>'
