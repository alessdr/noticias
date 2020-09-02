import unittest
import json

from app import app
from database.db import db


class SignupTest(unittest.TestCase):

    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost/movie-bag-test'
    }

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def test_successful_signup(self):
        # Given
        payload = json.dumps({
            "email": "alessdr@gmail.com",
            "password": "123mudar"
        })

        # When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
