# Full Stack Nanodegree Casting Agency Capstone Project

The Technology used to build the project are Python and Flask micro-framework. For this Back-end i have applied the PEP-8 style.
Casting Agency, is a Full-Stack project that i build for the challenge to graduate from Udacity FSND-nanodegree, i have build it and deploy it in heroku after testing.
Also i follow the PEP-8 style guidlelines for easy reading.
## Getting Started

### Installing Dependencies

First, you need to have the following tools:
1. Python3 and PIP.

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the root of the directory and run:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server locally in development environment

After creating your virtual enviroment, within the `root` directory, do the following.

To run the server, execute:

```bash
pip install -r requirements.txt
source setup.sh
python app.py
```

the `source setup.sh` will prepare all the needed environment variables to run the server.

#### Testing

To run the tests:
```
dropdb capstone_test
createdb capstone_test
source setup.sh
python test_app.py
```

## API Reference

### Introduction

The API builded to make users eable to perform CRUD operations on Casting Agency database easily. It have been builded using Flask micro-framework, which is Python framework.

All the responses of the API is in JSON format.

### Getting Started

#### Base URL

This project is deployed and available on Heroku:
```
https://doj-capstone.herokuapp.com/
```

### Error

The API have clear and defined errors that will make the debug process easier for developers.

#### Error Types:

- 404 - Not Found
- 422 - Unprocesaable
- 400 - Bad Request
- 401 - Unauthorized

#### Error Response Example:

```
{
    "success": False,
    "error": 404,
    "message": "Resource Not Found"
}
```

### Endpoints Library

This section will contain all the endpoints with their response examples to make everything clear for the users of our API

#### GET /actors

- Return: return list of all the available actors.

- Sample Request: ```curl https://doj-capstone.herokuapp.com/actors```

- Arguments: None

- Sample Response:
    ```
    {
          "success": True,
          "actors": [
            {
              "id": 1,
              "name": "Khadija Ahmed",
              "gender": "Female",
              "age": 45
            }, 
            {
              "id": 5,
              "name": "Muslim Hadi",
              "gender": "Female",
              "age": 95
            }
          ]
    }
    ```
#### GET /movies

- Return: return list of all the available movies.

- Sample Request: ```curl https://doj-capstone.herokuapp.com/movies```

- Arguments: None

- Sample Response:
    ```
    {
          "success": True,
          "movies": [
            {
              "id": 1,
              "title": "Sharp Blade",
              "release": "6 Oct, 1988"
            }, 
            {
              "id": 4,
              "title": "Bruslie",
              "release": "08 Jun, 1999"
            }
          ]
    }
    ```

#### DELETE /actors/id

- Return: 
    - deleted actor id and result of success.

- Sample Request: ```curl -X "DELETE" https://doj-capstone.herokuapp.com/actors/2```

- Arguments: 
    - it take the id of the actor in the URL after the ```actors/```

- Sample Response:
    ```
    {
        "success": True,
        "actor_id": 2
    }
    ```

#### DELETE /movies/id

- Return: 
    - the deleted movie ID and result of success.

- Sample Request: ```curl -X "DELETE" https://doj-capstone.herokuapp.com/movies/5```

- Arguments: 
    - it take the id of the movie in the URL after the ```movies/```

- Sample Response:
    ```
    {
        "success": True,
        "movie_id": 2
    }
    ```

#### POST /actors

- Return: 
    - the request success message.
    - the created actor data.
    - the id of the created actor.

- Sample Request: 
    ```curl -d '{"name": "Khadija Ahmed", "age": 54, "gender": "Female"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "POST" https://doj-capstone.herokuapp.com/actors```

- Arguments: 
    - None

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "actor": {
            "id": 15,
            "name": "Khadija Ahmed",
            "gender": "Female",
            "age": 54
        },
        "actor_id": 45
    }
    ```

#### POST /movies

- Return: 
    - the request success state.
    - the created movie object.
    - the ID of the created movie.

- Sample Request: 
    ```curl -d '{"title": "Sharp Blade", "release":"08 Dec, 1988"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "POST" https://doj-capstone.herokuapp.com/movies```

- Arguments: 
    - None

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "movie": {
            "id": 87,
            "title": "Sharp Blade",
            "release": "08 Dec, 1988"
        },
        "movie_id": 99
    }
    ```

#### PATCH /actors

- Return:
    - the request success state.
    - the modified actor object.
    - the ID of the modified actor.

- Sample Request: 
    ```curl -d '{"name": "Khadija Ahmed", "age": 33, "gender": "Female"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "PATCH" https://doj-capstone.herokuapp.com/actors/15```

- Arguments: 
    - the ID of the actor that need to modified.

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "actor": {
            "id": 15,
            "name": "Khadija Ahmed",
            "gender": "Female",
            "age": 33
        },
        "actor_id": 85
    }
    ```

#### PATCH /movies

- Return:
    - the request success state.
    - the modified movie object.
    - the ID of the modified movie.

- Sample Request: 
    ```curl -d '{"title": "World war"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "PATCH" https://doj-capstone.herokuapp.com/movies/87```

- Arguments: 
    - the ID of the movie that need to modified.

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "movie": {
            "id": 55,
            "title": "World war",
            "release": "09 Dec, 1988"
        },
        "movie_id": 185
    }
    ```

## Authentication and Permissions

Authentication is handled via [Auth0](https://auth0.com).

All endpoints require authentication, and proper permission. Except the GET/actors and GET/movies are the public endpoints. So, anyone can access.

For testing, you can use the Tokens that available in the setup.sh file.

API endpoints use these roles and permissions, in the project i have included two rules, Casting Director and Executive Director:

- Casting Director:
    * 'delete:actor' (remove actor from the casting agency database).
    * 'patch:actor' (edit or modify actor data that exist in the casting agency database).
    * 'patch:movie' (edit or modify actor data that exist in the casting agency database).
    * 'post:actors' (create new actors in the casting agency database).

- Executive Director:
    * Same as the Casting Director permissions, plus
    * 'delete:movie' (remove movie from the casting agency database).
    * 'post:movies' (create new movies in the casting agency database).
