from resources.logger_config import logger
from flask import Blueprint, jsonify


routes_api = Blueprint('routes_api', __name__)


@routes_api.route("/")
def hello_world():
    logger.info("/")
    return "Hello World"


@routes_api.route("/api/<some_data>")
def foo_url_arg(some_data):
    logger.info("/foo/%s", some_data)
    return jsonify({"echo": some_data})
