from .news import NewsApi, NewsParamApi
from api.auth import SignupApi, LoginApi


def initialize_routes(api):
    api.add_resource(NewsApi, '/api/v1/noticias')
    api.add_resource(NewsParamApi, '/api/v1/noticias/<id_news>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')