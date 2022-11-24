from app import login_manager
from app.modules.models import Admin


@login_manager.user_loader
def load_user(id):
    return Admin.query.get(int(id))
