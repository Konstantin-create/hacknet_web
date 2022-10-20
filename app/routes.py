# Import consts
from app import web_site_folder

# Import modules
from app.modules import posts_tools
from app.modules import github_tools
from app.modules import dashboard_tools

# Flask imports
from app import app, redirect, render_template, request


# Index page router
@app.route('/')
@app.route('/page/<int: page_id>')
def init_page(page_id=1):
    print(page_id)
    dashboard_tools.request_handler(ip=request.remote_addr, url='/')
    return render_template(
        'index.html',
        page_id=page_id,

        gh_stat=github_tools.get_statistic(),
        gh_pinned=github_tools.get_pinned_repos(),
        web_site_folder=web_site_folder
    )


# Blog page router
@app.route('/blog')
def blog_page():
    dashboard_tools.request_handler(ip=request.remote_addr, url='/blog')
    return render_template('blog_page.html')


# Admin login page router
@app.route('/admin/login')
def admin_login_page(error_code: int = 100):  # dev: Code 100 is OK code
    return render_template('admin/login_page.html', error_code=error_code)


# Admin dashboard page
@app.route('/admin/dashboard')
def admin_dashboard():
    # todo: login required
    return render_template(
        'admin/dashboard_page.html',
        all_requests=dashboard_tools.generate_requests_data(),
        all_visitors=dashboard_tools.generate_pages_data()
    )


# Admin clear statistics button click handler
@app.route('/admin/clear-stat')
def admin_clear_stat():
    # todo: login required
    try:
        dashboard_tools.clear_statistics()
    except Exception as e:
        print(e)
    return redirect('/admin/dashboard')


# Admin content editor router
@app.route('/admin/content-editor')
def admin_content_editor():
    # todo: login required
    return render_template(
        'admin/content_editor.html'
    )


# Admin post creator
@app.route('/admin/posts-creator')
def admin_post_creator():
    # todo: login required
    return render_template(
        'admin/posts-creator.html'
    )


# Admin login form data handler
@app.route('/admin/login/form', methods=['GET', 'POST'])
def admin_login_handler():
    if request.method == 'POST':
        username, password = request.form.get('username'), request.form.get('password')
        # todo: login admin in flask-login
        return redirect('/admin/dashboard')
    return admin_login_page(error_code=200)  # dev: Error code 200 is login error code
