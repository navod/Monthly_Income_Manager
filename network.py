from flask import Flask
from config import Config
from model import db
from controller import userController,whishlistController
from flask_cors import CORS, cross_origin

def create_app(config=Config):
    application = Flask(__name__)
    # cors = CORS(application, resources={r"/api/*": {"origins": "*"}})
    application.config.from_object(config)
    db.init_app(application)
    
    application.register_blueprint(userController.blue_print)
    application.register_blueprint(whishlistController.blue_print)
    application.register_blueprint(whishlistController.blue_print_2)
    CORS(application)

    with application.app_context():
        db.create_all()
        return application
    
   