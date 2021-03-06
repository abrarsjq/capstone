import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


database_path = os.environ['DATABASE_URL']
if not database_path:
    database_name = "capstone_agency"
    database_path = "postgresql://{}:{}@{}/{}".format('postgres',
                                                      'admin',
                                                      'localhost:5432',
                                                      database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    # set up the database and connecting it with the app
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all()


class Actor(db.Model):
    # this is the actor model
    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.String)
    gender = db.Column(db.String)

    def __repr__(self):
        return f"<Actor id='{self.id}' name='{self.name}'>"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        # insert the object into the DB and commit
        db.session.add(self)
        db.session.commit()

    def update(self):
        # commit the updates
        db.session.commit()

    def delete(self):
        # remove the record from the database and commit the transaction
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


class Movie(db.Model):
    # this is the movie model
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release = db.Column(db.String)

    def __repr__(self):
        return f"<Movie id='{self.id}' title='{self.title}'>"

    def __init__(self, title, release):
        self.title = title
        self.release = release

    def insert(self):
        # insert the object into the DB and commit
        db.session.add(self)
        db.session.commit()

    def update(self):
        # commit the updates
        db.session.commit()

    def delete(self):
        # remove the record from the database and commit the transaction
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release': self.release,
        }
