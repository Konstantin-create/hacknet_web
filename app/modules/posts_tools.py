from app import db
from app.modules.models import Posts


def get_posts(page_id: int, total: int = 10) -> list:
    return Posts.query.order_by(Posts.id.desc()).paginate(page=1, per_page=10).items


def add_post(header: str = '', text: str = '', tags: str = '', img: str = '') -> dict:
    try:
        post = Posts(header=header, text=text, tags=tags, img=img)
        db.session.add(post)
        db.session.commit()
        return {'success': True, 'error': ''}
    except Exception as e:
        return {'success': False, 'error': e}
