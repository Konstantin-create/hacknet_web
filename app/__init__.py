# Base imports
import os

# My modules imports
from config import Config

# Flask imports
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, url_for

from flask_login import LoginManager

# Flask init
app = Flask(__name__)
app.config.from_object(Config)

# DB init
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask login
login_manager = LoginManager(app)

web_site_folder = os.path.dirname(__file__)

from app.modules.models import *
from app.routes.admin import admin_login
from app.routes.admin import *
