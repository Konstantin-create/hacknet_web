from flask import Flask, render_template

# Flask init
app = Flask(__name__)

from app.routes import *

app.run()
