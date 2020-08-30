from werkzeug.exceptions import HTTPException
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from waitress import serve
from api.routes import routes_api
from constants.constants import ENVIRONMENT_PROD
from resources.logger_config import logger
from resources.app_config import config
from database.db import initialize_db

import os
import json


def create_app():
    app = Flask(__name__)

    # Config app parameters
    app = config(app)

    # Definition of the routes
    app.register_blueprint(routes_api)

    # Hashing lib
    bcrypt = Bcrypt(app)

    # Database init
    initialize_db(app)

    # Exceptions
    @app.errorhandler(HTTPException)
    def handle_exception(error):
        response = error.get_response()
        response.data = json.dumps({
            "code": error.code,
            "name": error.name,
            "description": error.description,
        })
        response.content_type = "application/json"
        logger.exception('%s.', error)
        return response, error.code

    # Set CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    return app


if __name__ == "__main__":
    # Load .env
    load_dotenv()
    # Load vars
    port = os.getenv('PORT')
    debug = os.getenv('DEBUG')
    environment = os.getenv('ENVIRONMENT')
    # Init app
    app = create_app()
    # Run
    if environment == ENVIRONMENT_PROD:
        threads = os.getenv('THREADS')
        serve(app, host='0.0.0.0', port=port, threads=threads)
    else:
        app.run(host="0.0.0.0", port=port, debug=debug)
