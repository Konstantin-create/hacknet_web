# Base imports
import os
import threading

# My modules imports
from config import Config
from app.modules.models import Admin
from app.modules import github_tools, dashboard_tools

# Flask imports
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, url_for

from flask_login import LoginManager
from flask_login import login_user, current_user

# Flask init
app = Flask(__name__)
app.config.from_object(Config)

# DB init
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask login
login_manager = LoginManager(app)

web_site_folder = os.path.dirname(__file__)

threading.Thread(target=github_tools.set_statistics).start()
threading.Thread(target=github_tools.set_pinned_repos).start()
threading.Thread(target=github_tools.set_user_description).start()


@login_manager.user_loader
def load_user(id):
    return Admin.query.get(int(id))


from app.modules.models import *
from app.routes import *
