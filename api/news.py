from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from database.models import News
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, \
    DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, InternalServerError, \
    NewsAlreadyExistsError, UpdatingNewsError, DeletingNewsError, NewsNotExistsError


class NewsApi(Resource):
    @jwt_required
    def get(self):
        try:
            list_news = News.objects.all().to_json()
            return Response(list_news, mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            news = News(**body).save()
            return {'id': str(news.id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise NewsAlreadyExistsError
        except Exception:
            raise InternalServerError


class NewsParamApi(Resource):
    @jwt_required
    def put(self, id_news):
        try:
            body = request.get_json()
            news = News.objects.get(id=id_news).update(**body)
            return Response(news, mimetype="application/json", status=200)
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingNewsError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, id_news):
        try:
            News.objects.get(id=id_news).delete()
            return '', 200
        except DoesNotExist:
            raise DeletingNewsError
        except Exception:
            raise InternalServerError

    @jwt_required
    def get(self, id_news):
        try:
            news = News.objects.get(id=id_news).to_json()
            return Response(news, mimetype="application/json", status=200)
        except DoesNotExist:
            raise NewsNotExistsError
        except Exception:
            raise InternalServerError
