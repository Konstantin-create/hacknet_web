import os
import threading
from flask_sqlalchemy import SQLAlchemy
from app.modules import github_tools, dashboard_tools
from flask import Flask, render_template, request, redirect

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite://database.db'
db.init_app(app)

web_site_folder = os.path.dirname(__file__)

threading.Thread(target=github_tools.set_statistics).start()
threading.Thread(target=github_tools.set_pinned_repos).start()
threading.Thread(target=github_tools.set_user_description).start()

from app.routes import *
