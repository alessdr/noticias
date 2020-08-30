class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class NewsAlreadyExistsError(Exception):
    pass


class UpdatingNewsError(Exception):
    pass


class DeletingNewsError(Exception):
    pass


class NewsNotExistsError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "NewsAlreadyExistsError": {
        "message": "News with given title already exists",
        "status": 400
    },
    "UpdatingNewsError": {
        "message": "Updating news added by other is forbidden",
        "status": 403
    },
    "DeletingNewsError": {
        "message": "Deleting news added by other is forbidden",
        "status": 403
    },
    "NewsNotExistsError": {
        "message": "News with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    }
}
