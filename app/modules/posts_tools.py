from bs4 import BeautifulSoup

from app import db
from app import web_site_folder

from config import Config

from app.modules.find_tools import approximate_search
from app.modules.models import Posts, Likes, Dislikes


def get_posts(page_id: int, on_page: int = 10) -> list:
    """Function to get items for page by page id"""

    if on_page == -1:
        return Posts.query.order_by(Posts.id.desc()).all()

    return Posts.query.order_by(Posts.id.desc()).paginate(page=page_id, per_page=Config.POSTS_PER_PAGE).items


def get_post(post_id: int) -> Posts | None:
    """Function to get post by id"""

    return Posts.query.get(post_id)


def get_pages() -> int:
    """Function to get total posts pages"""

    return Posts.query.order_by(Posts.id.desc()).paginate(per_page=Config.POSTS_PER_PAGE).pages


def get_finder_posts(page_id: int, header: str, on_page: int = 10) -> list:
    """Function to get items for page by page id and header"""

    if on_page == -1:
        return Posts.query.order_by(Posts.id.desc()).filter_by(header=header).all()
    return approximate_search(header, Posts.query.all())


def add_viewer(post) -> None:
    """Function to add viewer to post table"""

    post.views += 1
    db.session.add(post)
    db.session.commit()


def get_likes(post) -> int:
    """Function to count likes on post"""

    return len(Likes.query.filter_by(post_id=post.id).all())


def get_dislikes(post) -> int:
    """Function to count dislikes on post"""

    return len(Dislikes.query.filter_by(post_id=post.id).all())


def add_like(post_id: int, user_ip: str):
    """Function to like post"""

    like_obj = Likes.query.filter_by(post_id=post_id).filter_by(user_ip=user_ip).first()
    if not like_obj:
        like = Likes(post_id=post_id, user_ip=user_ip)
        dislike_obj = Dislikes.query.filter_by(post_id=post_id).filter_by(user_ip=user_ip).first()
        if dislike_obj:
            db.session.delete(dislike_obj)
        db.session.add(like)
    else:
        db.session.delete(like_obj)
    db.session.commit()


def add_dislike(post_id: int, user_ip: str):
    """Function to dislike post"""

    dislike_obj = Dislikes.query.filter_by(post_id=post_id).filter_by(user_ip=user_ip).first()
    if not dislike_obj:
        dislike = Dislikes(post_id=post_id, user_ip=user_ip)
        like_obj = Likes.query.filter_by(post_id=post_id).filter_by(user_ip=user_ip).first()
        if like_obj:
            db.session.delete(like_obj)
        db.session.add(dislike)
    else:
        db.session.delete(dislike_obj)
    db.session.commit()


def get_short_description(post_id: int) -> str:
    """Function to get short description for post"""

    with open(f'{web_site_folder}/templates/temp/posts/{post_id}.html', 'r') as file:
        full_text = file.read()
    soup = BeautifulSoup(full_text, 'html.parser')
    p_tags = soup.find_all('p')
    return p_tags[0]
