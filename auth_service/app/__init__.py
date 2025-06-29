from flask import Flask
from .routes.auth_routes import auth_routes  # Importa el blueprint

def create_app():
    app = Flask(__name__)

    # Aquí podrías cargar config si deseas (desde .env o config.py)
    app.config.from_pyfile('config.py')

    # Registrar blueprint
    app.register_blueprint(auth_routes)

    return app
