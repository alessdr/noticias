from werkzeug.exceptions import HTTPException
from flask import Flask, jsonify
from flask_cors import CORS
from logger_config import logger
from dotenv import load_dotenv
from waitress import serve
from constants import ENVIRONMENT_PROD

import json
import os


def create_app(config=None):
    app = Flask(__name__)

    # App config
    app.secret_key = os.getenv('SECRET_KEY')
    app.api_key = os.getenv('API_KEY')

    # Set CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Definition of the routes. Put them into their own file. See also
    # Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints
    @app.route("/")
    def hello_world():
        logger.info("/")
        return "Hello World"

    @app.route("/api/<some_data>")
    def foo_url_arg(some_data):
        logger.info("/foo/%s", some_data)
        return jsonify({"echo": some_data})

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
    if environment == ENVIRONMENT_PROD:
        threads = os.getenv('THREADS')
        serve(app, host='0.0.0.0', port=port, threads=threads)
    else:
        app.run(host="0.0.0.0", port=port, debug=debug)
