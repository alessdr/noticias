from flask_bcrypt import generate_password_hash, check_password_hash
from .db import db


class News(db.Document):
    title = db.StringField(required=True)
    content = db.StringField(required=True)
    publish_date = db.DateTimeField(required=True)


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=8)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
