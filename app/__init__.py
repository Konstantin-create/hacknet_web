from flask import Flask, render_template

app = Flask(__name__)

from app.routes import *

app.run(host='0.0.0.0', port=5000)

