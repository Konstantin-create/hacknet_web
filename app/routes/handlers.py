from app import db
from app import web_site_folder
from app.modules.models import Posts
from app import app, request, redirect
from app.modules import dashboard_tools
from app.routes.pages import admin_login_page
from app.routes import admin_post_creator, admin_post_editor_page


# Admin clear statistics button click handler
@app.route('/admin/clear-stat')
def admin_clear_stat():
    # todo: login required
    try:
        dashboard_tools.clear_statistics()
    except Exception as e:
        print(e)
    return redirect('/admin/dashboard')


# Admin login form data handler
@app.route('/admin/login/form', methods=['GET', 'POST'])
def admin_login_handler():
    if request.method == 'POST':
        username, password = request.form.get('username'), request.form.get('password')
        # todo: login admin in flask-login
        return redirect('/admin/dashboard')
    return admin_login_page(error_code=200)  # dev: Error code 200 is login error code


@app.route('/admin/add-post', methods=['GET', 'POST'])
def admin_add_post_handler():
    if request.method == 'POST':
        # todo: check is user admin
        header = request.form.get('post-header')
        text = request.form.get('post-text')
        tags = request.form.get('post-tags')
        image = request.files.get('post-file', '')
        post_id = Posts.query.order_by(Posts.id.desc()).first().id

        # Check fields
        if header == '':
            return admin_post_creator(header_error=True)
        if text == '':
            return admin_post_creator(text_error=True)
        if tags == '':
            return admin_post_creator(tags_error=True)

        post = Posts(
            header=header,
            text=text,
            tags=tags,
            img=f'{web_site_folder}/static/posts/img/{post_id}-1.jpg'
        )
        with open(f'{web_site_folder}/static/posts/img/{post_id}-1.jpg', 'w') as file:
            file.write(image)
        db.session.add(post)
        db.session.commit()
        return redirect('/admin/dashboard')


@app.route('/admin/edit-post/<int:post_id>', methods=['GET', 'POST'])
def admin_post_edit_handler(post_id):
    # todo: check is user admin
    if request.method == 'POST':
        post = Posts.query.get(post_id)

        header = request.form.get('post-header')
        text = request.form.get('post-text')
        tags = request.form.get('post-tags')
        image = request.files.get('post-file', '')

        # Check fields
        if header == '':
            return admin_post_editor_page(header_error=True)
        if text == '':
            return admin_post_editor_page(text_error=True)
        if tags == '':
            return admin_post_editor_page(tags_error=True)
        with open(f'{web_site_folder}/static/posts/img/{post_id}-1.jpg', 'w') as file:
            file.write(image)

        post.header = header
        post.text = text
        post.tags = tags

        db.session.commit()
        return redirect('/admin/dashboard')


@app.route('/admin/delete-post/<int:post_id>')
def admin_delete_post_handler(post_id):
    # todo: check is user admin

    try:
        post = Posts.query.get(post_id)
        db.session.delete(post)
        db.session.commit()
        return redirect('/admin/posts-creator')
    except Exception as e:
        return f'<span style="color: red">An error occurred: </span>{e}'
