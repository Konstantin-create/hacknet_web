# Flask imports
from app import app
from flask import redirect, render_template

# Flask user
from flask_login import current_user
from app.modules.models import Admin

# Import modules
from app.modules import posts_tools
from app.modules import content_editor
from app.modules import dashboard_tools


# Admin login page router
@app.route('/admin/login')
def admin_login_page(error_code: int = 100):  # dev: Code 100 is OK code
    return render_template('admin/login_page.html', error_code=error_code)


# Admin dashboard page
@app.route('/admin/dashboard')
def admin_dashboard_page():
    if not current_user.is_authenticated:
        return redirect('/admin/login')

    admin = Admin.query.get(current_user.get_id())
    ip = 'no data'
    time_stamp = 'no data'
    if admin:
        ip = admin.last_login_ip
        time_stamp = admin.last_login_time.strftime("%B %d %Y - %H:%M:%S")

    return render_template(
        'admin/dashboard_page.html',
        all_requests=dashboard_tools.generate_requests_data(),
        all_visitors=dashboard_tools.generate_pages_data(),
        ip=ip,
        time_stamp=time_stamp
    )


# Admin content editor router
@app.route('/admin/content-editor')
def admin_content_editor():
    if not current_user.is_authenticated:
        return redirect('/admin/login')

    content_data = content_editor.get_content()
    return render_template(
        'admin/content_editor.html',
        content_data=content_data
    )


# Admin post creator
@app.route('/admin/posts-creator')
def admin_post_creator(header_error=False, text_error=False, tags_error=False):
    if not current_user.is_authenticated:
        return redirect('/admin/login')

    return render_template(
        'admin/posts_creator.html',
        posts=posts_tools.get_posts(1, on_page=-1),
        header_error=header_error,
        text_error=text_error,
        tag_error=tags_error
    )


@app.route('/admin/post-editor/<int:post_id>')
def admin_post_editor_page(post_id, header_error=False, text_error=False, tags_error=False):
    if not current_user.is_authenticated:
        return redirect('/admin/login')

    post = posts_tools.get_post(post_id)
    return render_template(
        'admin/posts_editor.html',
        post=post,
        post_preview_img_name=post.preview_img.split('/')[-1],
        post_main_img_name=post.main_img.split('/')[-1],

        header_error=header_error,
        text_error=text_error,
        tags_error=tags_error
    )
