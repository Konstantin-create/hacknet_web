import threading

from app import *
from app.modules import github_tools, dashboard_tools

if __name__ == '__main__':
    threading.Thread(target=github_tools.set_statistics).start()
    threading.Thread(target=github_tools.set_pinned_repos).start()
    threading.Thread(target=github_tools.set_user_description).start()

    app.run(host='0.0.0.0', port=80)
