from app import db
from datetime import datetime


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String, nullable=False)
    text = db.Column(db.String(120), nullable=False)
    tags = db.Column(db.String(12000), nullable=False)
    time_stamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return f'<Post: {self.id} | {self.header}>'


class PostImages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    image = db.Column(db.LargeBinary, nullable=False)
