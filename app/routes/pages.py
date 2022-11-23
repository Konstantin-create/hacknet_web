# Import consts
from app import db
from app import web_site_folder

# Import modules
from app.modules import posts_tools
from app.modules import github_tools
from app.modules import content_editor
from app.modules import dashboard_tools

# Flask imports
from app import app, render_template, request, redirect, url_for

# Flask user
from flask_login import current_user


# Index page router
@app.route('/')
def init_page():
    dashboard_tools.request_handler(ip=request.remote_addr, url='/')
    content_data = content_editor.get_content()
    return render_template(
        'index.html',
        gh_stat=github_tools.get_statistic(),
        gh_pinned=github_tools.get_pinned_repos(),
        web_site_folder=web_site_folder,
        content_data=content_data['index']
    )


# Blog page router
@app.route('/blog')
@app.route('/blog/page/<int:page_id>')
def blog_page(page_id=1):
    dashboard_tools.request_handler(ip=request.remote_addr, url='/blog')
    content_data = content_editor.get_content()

    return render_template(
        'blog_page.html',
        page_id=page_id,
        total_pages=posts_tools.get_pages(),
        posts=posts_tools.get_posts(page_id),
        content_data=content_data['blog']
    )

@app.route('/blog/find/page/<int:page_id>')
@app.route('/blog/find', methods=['GET', 'POST'])
def find_page(page_id=1):
    if request.method == 'POST' or page_id != 0:
        request_data = request.form.get('posts-finder')
        content_data = content_editor.get_content()
        dashboard_tools.request_handler(ip=request.remote_addr, url=f'/blog/{"+".join(request_data.split())}')

        return render_template(
            'find_page.html',
            page_id=page_id,
            header=request_data,
            total_pages=posts_tools.get_finder_pages(request_data),
            posts=posts_tools.get_finder_posts(page_id, request_data),
            content_data=content_data['blog']
            )
            
    return redirect('/blog')


# Admin login page router
@app.route('/admin/login')
def admin_login_page(error_code: int = 100):  # dev: Code 100 is OK code
    return render_template('admin/login_page.html', error_code=error_code)


# Admin dashboard page
@app.route('/admin/dashboard')
def admin_dashboard_page():
    if not current_user.is_authenticated:
        return redirect('/admin/login')

    return render_template(
        'admin/dashboard_page.html',
        all_requests=dashboard_tools.generate_requests_data(),
        all_visitors=dashboard_tools.generate_pages_data()
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


@app.route('/posts/<int:post_id>')
def view_post(post_id):
    dashboard_tools.request_handler(ip=request.remote_addr, url=f'/posts/{post_id}')
    post = posts_tools.get_post(post_id)
    posts_tools.add_viewer(post)
    likes = posts_tools.get_likes(post)
    dislikes = posts_tools.get_dislikes(post)

    content_data = content_editor.get_content()

    return render_template(
        'post_template.html',
        post=post,
        content_data=content_data,
        likes=likes,
        dislikes=dislikes
    )
