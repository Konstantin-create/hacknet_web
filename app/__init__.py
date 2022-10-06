import os
import threading
from app.modules import github_tools, dashboard_tools
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
web_site_folder = os.path.dirname(__file__)

threading.Thread(target=github_tools.set_statistics).start()
threading.Thread(target=github_tools.set_pinned_repos).start()
threading.Thread(target=github_tools.set_user_description).start()


@app.route('/')
def init_page():
    dashboard_tools.request_handler(ip=request.remote_addr, url='/')
    return render_template(
        'index.html', gh_stat=github_tools.get_statistic(),
        gh_pinned=github_tools.get_pinned_repos(),
        web_site_folder=web_site_folder
    )


@app.route('/blog')
def blog_page():
    dashboard_tools.request_handler(ip=request.remote_addr, url='/blog')
    return render_template('blog_page.html')


@app.route('/admin/login')
def admin_login_page(error: int = 100):  # dev: Code 100 is OK code
    return render_template('admin/login_page.html')


@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template(
        'admin/dashboard_page.html',
        all_requests=dashboard_tools.generate_requests_data(),
        all_visitors=dashboard_tools.generate_pages_data()
    )


@app.route('/admin/login/form', methods=['GET', 'POST'])
def admin_login_handler():
    if request.method == 'POST':
        print(request.form.get('username'), request.form.get('password'))
        return redirect('/admin/dashboard')
    return admin_login_page(error=200)  # dev: Error code 200 is login error code
