import json
import os
from hashlib import sha256


class AdminUser:
    """Class of admin user"""

    __slots__ = ('cur_dir', 'username', 'password')

    def __init__(self, username: str, password: str):
        self.cur_dir = os.path.dirname(__name__)
        self.username = username
        self.password = sha256(password).hexdigest()

    def get_local_login(self) -> tuple:
        """Function to get local credentials of admin user. Return saved username and password"""

        if os.path.exists(f'{self.cur_dir}/app/data/admin/credentials.json'):
            try:
                _data = json.load(open(f'{self.cur_dir}/app/data/admin/credentials.json', 'r'))
                return _data[list(_data.keys())[0]], _data[list(_data.keys())[1]]
            except json.JSONDecoder:
                return None, None

    def check_login(self) -> bool:
        """Function to check login"""

        _local_login = self.get_local_login()
        return _local_login[0] == self.username and _local_login[1] == self.password
