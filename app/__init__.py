from flask import Flask, render_template

# Flask init
app = Flask(__name__)

from .routes import *

app.run()
