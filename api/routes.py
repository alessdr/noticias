from .news import NewsApi, NewsParamApi


def initialize_routes(api):
    api.add_resource(NewsApi, '/api/v1/noticias/')
    api.add_resource(NewsParamApi, '/api/v1/noticias/<id_news>')
