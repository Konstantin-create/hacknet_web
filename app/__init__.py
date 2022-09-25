import os
import threading
from app.modules import github_tools
from flask import Flask, render_template, make_response

app = Flask(__name__)
web_site_folder = os.path.dirname(__file__)

threading.Thread(target=github_tools.set_statistics).start()
threading.Thread(target=github_tools.set_pinned_repos).start()
threading.Thread(target=github_tools.set_user_description).start()


@app.route('/')
def init_page():
    return render_template(
        'index.html', gh_stat=github_tools.get_statistic(),
        gh_pinned=github_tools.get_pinned_repos(),
        web_site_folder=web_site_folder
    )


@app.route('/blog')
def blog_page():
    return render_template('blog_page.html')


@app.route('/admin/login')
def admin_login_page():
    return render_template('admin/login_page.html')
