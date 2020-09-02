from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from waitress import serve
from api.routes import initialize_routes
from resources.constants import ENVIRONMENT_PROD
from database.db import initialize_db
from resources.app_config import config
from resources.errors import errors
from resources.utils import str_to_bool

import os


def create_app():
    app = Flask(__name__)

    # Config app parameters
    app = config(app)

    # Definition of the routes
    api = Api(app, errors=errors)
    initialize_routes(api)

    # Hashing lib
    bcrypt = Bcrypt(app)

    # Auth lib
    jwt = JWTManager(app)

    # Database init
    initialize_db(app)

    # Set CORS
    CORS(app)

    return app


if __name__ == "__main__":
    # Load .env
    load_dotenv()
    # Load vars
    port = os.getenv("PORT")
    debug = str_to_bool(os.getenv("DEBUG"))
    environment = os.getenv("ENVIRONMENT")
    # Init app
    app = create_app()
    # Run
    if environment == ENVIRONMENT_PROD:
        threads = os.getenv("THREADS")
        serve(app, host="0.0.0.0", port=port, threads=threads)
    else:
        app.run(host="0.0.0.0", port=port, debug=debug)
