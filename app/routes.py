from app.modules import github_tools
from app import app, render_template, redirect, request


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', gh_stat=github_tools.get_profile_data())


@app.route('/admin/login')
def admin_login():
    return render_template('admin/admin-login.html')


@app.route('/admin/form/login', methods=['GET', 'POST'])
def form_login_route():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        return ''
    else:
        return redirect('/')
