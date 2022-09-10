import threading
from app.modules import github_tools
from flask import Flask, render_template

app = Flask(__name__)

threading.Thread(target=github_tools.set_statistics).start()


@app.route('/')
def init_page():
    return render_template('index.html', gh_stat=github_tools.get_stars())


