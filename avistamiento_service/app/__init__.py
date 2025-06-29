from flask import Flask
from app.routes.avistamiento_routes import avistamiento_routes 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(avistamiento_routes) 
    return app
    