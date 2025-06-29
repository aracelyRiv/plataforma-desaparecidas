from flask import Blueprint

case_routes = Blueprint('case_routes', __name__)

@case_routes.route('/', methods=['GET'])
def home():
    return "Case Service funcionando correctamente "
