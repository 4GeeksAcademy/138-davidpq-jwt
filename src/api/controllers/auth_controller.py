from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from api.services.auth_service import Auth

auth_bp = Blueprint('auth', __name__, "/api")
# SIGNUP
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    new_user = Auth.signup(data)
    return jsonify(new_user), 201


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = Auth.login(data)

    # Generar token JWT
    token = create_access_token(identity=str(user["id"]))
    return jsonify({
        "token": token,
        "user": user
    }), 200


# RUTA PROTEGIDA
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    print(user_id)
    user = Auth.get_current_user(user_id)
    return jsonify(user), 200