import bcrypt
from flask import abort

class UserService:
    @staticmethod
    def set_password(user, password):
        """Hashea un password en texto plano y lo almacena."""
        password_bytes = password.encode('utf-8')
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        user.password = hashed.decode('utf-8')

    @staticmethod
    def check_password(user, password):
        """Verifica un password en texto plano contra el hash almacenado."""
        password_bytes = password.encode('utf-8')
        hashed_bytes = user.password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_bytes)
