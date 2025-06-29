# Aquí irán las rutas de autenticación
from flask import Blueprint

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/', methods=['GET'])
def home():
    return "Auth Service está corriendo 🚀"
