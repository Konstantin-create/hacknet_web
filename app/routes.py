from app.modules import github_tools
from app import app, render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', gh_stat=github_tools.get_profile_data())


@app.route('/find')
def find():
    return render_template()
