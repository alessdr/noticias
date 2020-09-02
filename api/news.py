from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from database.models import News
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, \
    DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, InternalServerError, \
    NewsAlreadyExistsError, UpdatingNewsError, DeletingNewsError, NewsNotExistsError
from resources.utils import validate_date, adjust_dict_news, adjust_news

import json


class NewsApi(Resource):
    # @jwt_required
    def get(self):
        try:
            # Retrieve news list (MongoDB Document)
            list_news_doc = News.objects.all().to_json()

            # To dict
            list_news_dict = json.loads(list_news_doc)

            # To json (adjusted)
            list_news = json.dumps(adjust_dict_news(list_news_dict))

            return Response(list_news, mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

    # @jwt_required
    def post(self):
        try:
            body = request.get_json()
            body['publish_date'] = validate_date(body['publish_date'])
            news = News(**body).save()
            return {'id': str(news.id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise NewsAlreadyExistsError
        except Exception:
            raise InternalServerError


class NewsParamApi(Resource):
    # @jwt_required
    def put(self, id_news):
        try:
            body = request.get_json()
            body['publish_date'] = validate_date(body['publish_date'])
            news_id = News.objects.get(id=id_news).update(**body)
            return {'id': news_id}, 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingNewsError
        except Exception:
            raise InternalServerError

    # @jwt_required
    def delete(self, id_news):
        try:
            News.objects.get(id=id_news).delete()
            return '', 200
        except DoesNotExist:
            raise DeletingNewsError
        except Exception:
            raise InternalServerError

    # @jwt_required
    def get(self, id_news):
        try:
            # Retrieve news (MongoDB Document)
            news_doc = News.objects.get(id=id_news).to_json()

            # To dict
            news_obj = json.loads(news_doc)

            # To json (adjusted)
            news = json.dumps(adjust_news(news_obj))

            return Response(news, mimetype="application/json", status=200)
        except DoesNotExist:
            raise NewsNotExistsError
        except Exception:
            raise InternalServerError
