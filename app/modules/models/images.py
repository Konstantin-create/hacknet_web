from app import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f'<Image {self.id} - {self.image_path}>'
