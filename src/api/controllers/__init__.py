from api.controllers.auth_controller import auth_bp

def register_controllers(app):
    """
    Registra todos los blueprints (controladores) en la aplicación Flask.
    Se llama desde app.py al inicializar la aplicación.
    """
    app.register_blueprint(auth_bp, url_prefix='/api')
