from flask import abort
from api.models import db, User
from api.services.user_service import UserService

class Auth:

    @staticmethod
    def signup(data):
        required = ["email", "username", "password"]
        for field in required:
            if field not in data:
                abort(400, description=f"Falta el campo {field}")

        email = data["email"]
        username = data["username"]
        password = data["password"]

        # Verificar duplicados
        if User.query.filter_by(email=email).first():
            abort(400, description="El email ya está registrado")

        if User.query.filter_by(username=username).first():
            abort(400, description="El username ya está registrado")

        # Crear usuario
        new_user = User(email=email, username=username)
        UserService.set_password(new_user, password)
        

        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500, description="Error al crear usuario")

        return new_user.serialize()


    @staticmethod
    def login(data):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            abort(400, description="Email y password son requeridos")

        user = User.query.filter_by(email=email).first()

        if user is None:
            abort(401, description="Email no encontrado")

        if not UserService.check_password(user, password):
            abort(401, description="Contraseña incorrecta")

        return user.serialize()
