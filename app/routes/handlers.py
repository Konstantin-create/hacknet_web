from app import app, request, redirect
from app.modules import dashboard_tools
from app.routes.pages import admin_login_page


# Admin clear statistics button click handler
@app.route('/admin/clear-stat')
def admin_clear_stat():
    # todo: login required
    try:
        dashboard_tools.clear_statistics()
    except Exception as e:
        print(e)
    return redirect('/admin/dashboard')


# Admin login form data handler
@app.route('/admin/login/form', methods=['GET', 'POST'])
def admin_login_handler():
    if request.method == 'POST':
        username, password = request.form.get('username'), request.form.get('password')
        # todo: login admin in flask-login
        return redirect('/admin/dashboard')
    return admin_login_page(error_code=200)  # dev: Error code 200 is login error code
