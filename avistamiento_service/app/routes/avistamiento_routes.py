from flask import Blueprint

avistamiento_routes = Blueprint('avistamiento_routes', __name__)

@avistamiento_routes.route('/', methods=['GET'])
def home():
    return "Avistamiento Service funcionando correctamente "
