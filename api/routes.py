from flask import Blueprint, Response, request, jsonify
from database.models import News

import json


routes_api = Blueprint('routes_api', __name__)


@routes_api.route('/api/v1/noticias/', methods=['GET'])
def get_list_news():
    try:
        list_news = News.objects.all().to_json()
        return Response(list_news, mimetype="application/json", status=200)
    except Exception as err:
        return Response(json.dumps({'message': str(err)}), mimetype="application/json", status=500)


@routes_api.route('/api/v1/noticias/<id_news>', methods=['GET'])
def get_news(id_news):
    try:
        news = News.objects.get(id=id_news).to_json()
        return Response(news, mimetype="application/json", status=200)
    except Exception as err:
        return Response(json.dumps({'message': str(err)}), mimetype="application/json", status=500)


@routes_api.route('/api/v1/noticias/', methods=['POST'])
def create_news():
    try:
        body = request.get_json()
        news = News(**body).save()
        return {'id': str(news.id)}, 200
    except Exception as err:
        return Response(json.dumps({'message': str(err)}), mimetype="application/json", status=500)


@routes_api.route('/api/v1/noticias/<id_news>', methods=['PUT'])
def update_news(id_news):
    try:
        body = request.get_json()
        news = News.objects.get(id=id_news).update(**body)
        return Response(news, mimetype="application/json", status=200)
    except Exception as err:
        return Response(json.dumps({'message': str(err)}), mimetype="application/json", status=500)


@routes_api.route('/api/v1/noticias/<id_news>', methods=['DELETE'])
def delete_news(id_news):
    try:
        News.objects.get(id=id_news).delete()
        return '', 200
    except Exception as err:
        return Response(json.dumps({'message': str(err)}), mimetype="application/json", status=500)
