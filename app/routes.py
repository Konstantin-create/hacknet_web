from app.get_data_values import Data
from app import app, render_template


@app.route('/')
def index_page():
    """Function of index page routing"""
    return render_template('index.html', Data=Data)
