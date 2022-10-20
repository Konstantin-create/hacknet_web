from app import db
from app.modules.models import Posts


def get_posts(total=20) -> list:
    return Posts.query.order_by(Posts.id.desc()).limit(20).all()


def add_post(header: str = '', text: str = '', tags: str = '', img: str = '') -> dict:
    try:
        post = Posts(header=header, text=text, tags=tags, img=img)
        db.session.add(post)
        db.session.commit()
        return {'success': True, 'error': ''}
    except Exception as e:
        return {'success': False, 'error': e}
