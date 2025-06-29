from flask import Blueprint

face_routes = Blueprint('face_routes', __name__)

@face_routes.route('/', methods=['GET'])
def home():
    return "Face Service funcionando correctamente "
