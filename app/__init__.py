import threading
from app.modules import github_tools
from flask import Flask, render_template

app = Flask(__name__)

print(github_tools.get_user_description())
threading.Thread(target=github_tools.set_statistics).start()
threading.Thread(target=github_tools.set_pinned_repos).start()


@app.route('/')
def init_page():
    return render_template(
        'index.html', gh_stat=github_tools.get_statistic(),
        gh_pinned=github_tools.get_pinned_repos()
    )
