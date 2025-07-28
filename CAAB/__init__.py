import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv 
from flask_cors import CORS, cross_origin
from .db import db
from urllib.parse import quote_plus
from .controllers.auth import login
from .controllers.User import User_creation_bp
from .controllers.get_departments import departments_dp
from .controllers.get_dropdowns import dropdowns_bp
from .controllers.navigation import navigator_bp
from .controllers.Dealer import Dealer_bp
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import timedelta
from flask_http_middleware import MiddlewareManager
from CAAB.middlewares.logger import LoggingMiddleware 

load_dotenv()

def create_app():
    app = Flask(__name__ )
    # CORS(app, support_credentials=True)
    CORS(app)

    db_user = os.getenv("DB_User")
    db_password = quote_plus(os.getenv("DB_Password"))
    db_host = os.getenv("DB_Host")
    db_port = os.getenv("DB_Port")
    db_name = os.getenv("DB_Name")
    app.config.from_mapping(
        SECRET_KEY=os.getenv("MY_SECRET_KEY"),
        JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI= f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES"))),
        JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")))
    )

    db.init_app(app)
    jwt = JWTManager(app)
    app.register_blueprint(login, url_prefix='/auth')
    app.register_blueprint(User_creation_bp, url_prefix='/User')
    app.register_blueprint(departments_dp)
    app.register_blueprint(dropdowns_bp, url_prefix = '/dropdowns')
    app.register_blueprint(Dealer_bp, url_prefix = '/Dealer')
    app.register_blueprint(navigator_bp)

    app.wsgi_app = MiddlewareManager(app)
    app.wsgi_app.add_middleware(LoggingMiddleware)
    return app