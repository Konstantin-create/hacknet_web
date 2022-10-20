from app import db
from config import Config
from app.modules.models import Posts


def get_posts(page_id: int) -> list:
    """Function to get items for page by page id"""

    return Posts.query.order_by(Posts.id.desc()).paginate(page=page_id, per_page=Config.POSTS_PER_PAGE).items


def get_pages():
    """Function to get total posts pages"""

    return Posts.query.order_by(Posts.id.desc()).paginate(per_page=Config.POSTS_PER_PAGE).pages


def add_post(header: str = '', text: str = '', tags: str = '', img: str = '') -> dict:
    """Function to add post in to db"""

    try:
        post = Posts(header=header, text=text, tags=tags, img=img)
        db.session.add(post)
        db.session.commit()
        return {'success': True, 'error': ''}
    except Exception as e:
        return {'success': False, 'error': e}


def delete_post(post_id: int):
    """Function to remove post from db"""

    pass
