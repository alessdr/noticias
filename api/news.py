from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from database.models import News

import json


class NewsApi(Resource):
    @jwt_required
    def get(self):
        try:
            list_news = News.objects.all().to_json()
            return Response(list_news, mimetype="application/json", status=200)
        except Exception as err:
            return Response(json.dumps({'message': str(err)}), mimetype="application/json", status=500)

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            news = News(**body).save()
            return {'id': str(news.id)}, 200
        except Exception as err:
            return Response(json.dumps({'message': str(err)}), mimetype="application/json", status=500)


class NewsParamApi(Resource):
    @jwt_required
    def put(self, id_news):
        try:
            body = request.get_json()
            news = News.objects.get(id=id_news).update(**body)
            return Response(news, mimetype="application/json", status=200)
        except Exception as err:
            return Response(json.dumps({'message': str(err)}), mimetype="application/json", status=500)

    @jwt_required
    def delete(self, id_news):
        try:
            News.objects.get(id=id_news).delete()
            return '', 200
        except Exception as err:
            return Response(json.dumps({'message': str(err)}), mimetype="application/json", status=500)

    @jwt_required
    def get(self, id_news):
        try:
            news = News.objects.get(id=id_news).to_json()
            return Response(news, mimetype="application/json", status=200)
        except Exception as err:
            return Response(json.dumps({'message': str(err)}), mimetype="application/json", status=500)