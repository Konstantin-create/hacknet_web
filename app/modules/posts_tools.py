from app import db
from app.modules.models import Posts


def get_posts(total=20):
    print(Posts.query.order_by(Posts.id.desc()).limit(20).all())


def add_post(header: str = '', text: str = '', tags: str = '', img: str = ''):
    post = Posts(header=header, text=text, tags=tags, img)
