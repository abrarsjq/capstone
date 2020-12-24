import json
import os
import unittest
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie


class TestCapstoneAgency(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'capstone_agency_test'
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(
                             'postgres', 'admin',
                             'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        # binds the app to the current context and initiating the database

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()
            self.db.create_all()

        self.director_token = os.environ['DIRECTOR_TOKEN']
        self.producer_token = os.environ['EXECUTIVE_PRODUCER']
        self.producer_credential = {
                                    'Authorization': 'Bearer {}'.format(
                                                    self.producer_token)}
        self.director_credential = {
                                    'Authorization': 'Bearer {}'.format(
                                                    self.director_token)}

        ''' This will create records in the
        test database to use it to test '''

        for i in range(5):
            actor = Actor(name='Brad Pitt',
                          age=44,
                          gender='male')
            actor.insert()
            movie = Movie(title='Titanic',
                          release='2020-12-18')
            movie.insert()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_add_movie_success(self):

        ''' this test will success becasue the token of
        producer and it is valid and he have permission '''

        response = self.client().post(
                                      '/movies',
                                      headers=self.producer_credential,
                                      json={'title': 'Titanic',
                                            'release': "2020-12-18"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_add_movie_failure(self):

        # 401 error will arise becasue no token provided

        response = self.client().post(
                                 '/movies',
                                 headers=self.director_credential,
                                 json={
                                     'title': 'Titanic',
                                     'release': "2020-12-18"
                                 })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_remove_movie_success(self):

        ''' this test will success becasue the token of producer
        and it is valid and he have permission '''

        movie = Movie.query.all()[0]
        response = self.client().delete('/movies/{}'.format(movie.id),
                                        headers=self.producer_credential)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_remove_movie_failure(self):

        # 401 error will arise becasue no token provided

        movie = Movie.query.all()[0]
        response = self.client().delete('/movies/{}'.format(movie.id),
                                        headers=self.director_credential)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_modify_movies_success(self):

        ''' this test will success becasue the token of producer
        and it is valid and he have permission '''

        movie = Movie.query.all()[0]
        response = self.client().patch('/movies/{}'.format(movie.id),
                                       headers=self.producer_credential,
                                       json={'title': 'Titanic',
                                             'release': "2020-12-18"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_modify_movies_failure(self):

        # 401 error will arise becasue no token provided

        movie = Movie.query.all()[0]
        response = self.client().patch('/movies/{}'.format(movie.id),
                                       json={'title': 'Titanic',
                                             'release': "2020-12-18"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_add_actor_success(self):

        ''' this test will success becasue the token of producer and
        it is valid and he have permission '''

        response = self.client().post('/actors',
                                      headers=self.producer_credential,
                                      json={'name': 'Brad Pitt',
                                            'age': 44,
                                            'gender': 'male'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_add_actor_failure(self):

        # 401 error will arise becasue no token provided

        response = self.client().post('/actors', json={'name': 'Brad Pitt',
                                                       'age': 44,
                                                       'gender': 'male'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_remove_actor_success(self):

        ''' this test will success becasue the token of
        producer and it is valid and he have permission '''

        actor = Actor.query.all()[0]
        response = self.client().delete('/actors/{}'.format(actor.id),
                                        headers=self.producer_credential)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_remove_actor_failure(self):

        # 401 error will arise becasue no token provided

        actor = Actor.query.all()[0]
        response = self.client().delete('/actors/{}'.format(actor.id))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_modify_actor_success(self):

        ''' this test will success becasue the token of
        producer and it is valid and he have permission '''

        actor = Actor.query.all()[0]
        response = self.client().patch('/actors/{}'.format(actor.id),
                                       headers=self.producer_credential,
                                       json={'name': 'Brad Pitt',
                                             'age': 44,
                                             'gender': 'male'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_modify_actor_failure(self):

        # 401 error will arise becasue no token provided

        actor = Actor.query.all()[0]
        response = self.client().patch('/actors/{}'.format(actor.id),
                                       json={'name': 'Brad Pitt',
                                             'age': 44,
                                             'gender': 'male'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_retireve_movies_success(self):

        # no token needed to request this API enpoint

        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_retireve_actors_success(self):

        # no token needed to request this API enpoint

        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
