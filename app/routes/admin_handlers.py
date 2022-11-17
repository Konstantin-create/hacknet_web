from app import db
from app import web_site_folder

from app.modules.models import Posts, Admin

from flask_login import login_user, current_user, logout_user
from app import app, request, redirect, url_for

from app.modules import content_editor
from app.modules import dashboard_tools

from app.routes import admin_post_creator, admin_post_editor_page, admin_login_page


# Admin clear statistics button click handler
@app.route('/admin/clear-stat')
def admin_clear_stat():
    if not current_user.is_authenticated:
        return redirect('/admin/login')

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

        if username == '' or password == '':
            return admin_login_page(error_code=400)

        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            login_user(admin, remember=True)
            return redirect('/admin/dashboard')
    return admin_login_page(error_code=200)  # dev: Error code 200 is login error code


@app.route('/admin/logout')
def admin_logout_handler():
    logout_user()
    return redirect('/admin/login')


@app.route('/admin/add-post', methods=['GET', 'POST'])
def admin_add_post_handler():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect('/admin/login')

        header = request.form.get('post-header')
        text = request.form.get('post-text')
        tags = request.form.get('post-tags')
        image = request.files.get('post-file', '')
        print(f'{image=}')
        try:
            post_id = Posts.query.order_by(Posts.id.desc()).first().id + 1
        except Exception as e:
            post_id = 1

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
    if not current_user.is_authenticated:
        return redirect('/admin/login')

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
    if not current_user.is_authenticated:
        return redirect('/admin/login')

    try:
        post = Posts.query.get(post_id)
        db.session.delete(post)
        db.session.commit()
        return redirect('/admin/posts-creator')
    except Exception as e:
        return f'<span style="color: red">An error occurred: </span>{e}'


@app.route('/admin/edit-content/total', methods=['GET', 'POST'])
def edit_content():
    if not current_user.is_authenticated:
        return redirect('/admin/login')

    if request.method == 'POST':
        # Index page items
        index_header_item1 = request.form.get('index-header-item1')
        index_header_item2 = request.form.get('index-header-item2')
        index_header_item3 = request.form.get('index-header-item3')

        index_header_item1_link = request.form.get('index-header-item1-link')
        index_header_item2_link = request.form.get('index-header-item2-link')
        index_header_item3_link = request.form.get('index-header-item3-link')

        index_main_header = request.form.get('index-main-header')
        index_footer_link1 = request.form.get('index-footer-link1')
        index_footer_link2 = request.form.get('index-footer-link2')
        index_footer_link3 = request.form.get('index-footer-link3')

        # Blog page items
        blog_header_item1 = request.form.get('blog-header-item1')
        blog_header_item2 = request.form.get('blog-header-item2')
        blog_header_item3 = request.form.get('blog-header-item3')

        blog_header_item1_link = request.form.get('blog-header-item1-link')
        blog_header_item2_link = request.form.get('blog-header-item2-link')
        blog_header_item3_link = request.form.get('blog-header-item3-link')

        content_editor.edit_content(
            {
                'index': {
                    'headers': [index_header_item1, index_header_item2, index_header_item3],
                    'header_links': [index_header_item1_link, index_header_item2_link, index_header_item3_link],
                    'main_header': index_main_header,
                    'footer': [index_footer_link1, index_footer_link2, index_footer_link3]
                },
                'blog': {
                    'headers': [blog_header_item1, blog_header_item2, blog_header_item3],
                    'header_links': [blog_header_item1_link, blog_header_item2_link, blog_header_item3_link]
                }
            }
        )
