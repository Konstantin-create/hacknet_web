# Import consts
from config import Config
from app import web_site_folder

# Import modules
from app.modules import posts_tools
from app.modules import github_tools
from app.modules import content_editor
from app.modules import dashboard_tools

# Flask imports
from app import app, render_template, request, redirect, url_for


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


@app.route('/blog/find', methods=['GET', 'POST'])
@app.route('/blog/find/page/<int:page_id>')
def find_page(page_id=1):
    if request.method == 'POST' or page_id != 0:
        request_data = request.form.get('posts-finder')
        content_data = content_editor.get_content()
        dashboard_tools.request_handler(ip=request.remote_addr, url=f'/blog/{"+".join(request_data.split())}')
        posts = posts_tools.get_finder_posts(page_id, request_data)
        posts = [posts[i:i + Config.POSTS_PER_PAGE] for i in range(0, len(posts), Config.POSTS_PER_PAGE)]

        return render_template(
            'find_page.html',
            page_id=page_id,
            header=request_data,
            posts=posts[page_id - 1],
            total_pages=len(posts),
            content_data=content_data['blog']
        )

    return redirect('/blog')


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
