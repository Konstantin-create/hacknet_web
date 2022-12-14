from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    last_login_ip = db.Column(db.String)
    last_login_time = db.Column(db.DateTime, default=datetime.utcnow())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def set_last_login(self, ip: str):
        self.last_login_ip = ip
        self.last_login_time = datetime.utcnow()

    def __repr__(self):
        return f'<Admin {self.id} - {self.username}>'
