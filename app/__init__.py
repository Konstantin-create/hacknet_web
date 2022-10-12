import os
import threading
from app.modules import github_tools, dashboard_tools
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

web_site_folder = os.path.dirname(__file__)

threading.Thread(target=github_tools.set_statistics).start()
threading.Thread(target=github_tools.set_pinned_repos).start()
threading.Thread(target=github_tools.set_user_description).start()

from app.routes import *
