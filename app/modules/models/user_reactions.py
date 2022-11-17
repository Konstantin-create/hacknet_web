from app import db


class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_ip = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<Like: {self.user_ip} | {self.post_id}>'


class Dislikes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_ip = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<Dislike: {self.user_ip} | {self.post_id}>'
