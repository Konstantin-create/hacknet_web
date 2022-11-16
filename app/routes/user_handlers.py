from app import db
from app import app, redirect
from app.modules.models import Posts

@app.route('/user/add-post-like/<int:post_id>')
def user_add_like(post_id: int):

    try:
        post = Posts.query.get(post_id)
        post.likes += 1
        db.session.add(post)
        db.session.commit()
    except:
        pass
    return redirect(f'/posts/{post_id}')

@app.route('/user/add-post-like/<int:post_id>')
def user_add_dislike(post_id: int):

    try:
        post = Posts.query.get(post_id)
        post.dislikes += 1
        db.session.add(post)
        db.session.commit()
    except:
        pass
    return redirect(f'/posts/{post_id}')
