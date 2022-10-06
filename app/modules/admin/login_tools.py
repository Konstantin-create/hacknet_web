import json
import os
from hashlib import sha256


class AdminUser:
    """Class of admin user"""

    __slots__ = ('username', 'password', 'authorized')

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = sha256(password.encode('utf-8')).hexdigest()
        self.authorized = False

    def get_local_login(self) -> tuple | None:
        """Function to get local credentials of admin user. Return saved username and password"""

        if os.path.exists(f'app/data/admin/credentials.json'):
            try:
                _data = json.load(open(f'app/data/admin/credentials.json', 'r'))
                return _data['username'], _data['password']
            except Exception as e:
                return None

    def check_login(self) -> bool:
        """Function to check login"""

        _local_login = self.get_local_login()
        if _local_login is None:
            return True
        else:
            self.authorized = _local_login[0] == self.username and _local_login[1] == self.password
            return self.authorized
