from flask import Flask
from .routes.case_routes import case_routes  # Importa el blueprint

def create_app():
    app = Flask(__name__)

    # Aquí podrías cargar config si deseas (desde .env o config.py)
    app.config.from_pyfile('config.py')

    # Registrar blueprint
    app.register_blueprint(case_routes)

    return app
