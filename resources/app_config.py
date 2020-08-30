import os


def config(app):
    app.secret_key = os.getenv('SECRET_KEY')
    app.api_key = os.getenv('API_KEY')

    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://' + os.getenv('DB_HOST') + ':' +
                os.getenv('DB_PORT') + '/' +
                os.getenv('DB_NAME')
    }

    return app
