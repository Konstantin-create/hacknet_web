import threading
from flask import Flask, render_template
from app.modules.github_tools import set_profile_data

app = Flask(__name__)

#  Start thread with GitHub statistic parser
threading.Thread(target=set_profile_data).start()

from app.routes import *

app.run()
