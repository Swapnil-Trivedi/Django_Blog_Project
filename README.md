# Blog Project API
## About
This is an REST API implementation for a blog application that allows users to create and share things they post with other users.

## Goal
The goal of this project is to provide a uniform API for both mobile and web frontend applications.

## Features
With this API:
- You can create a user account - Registration
- You can login and log out - Authorization and Authentication
- You can create, view, update, and delete a post in your user account
- You can view posts from other users

## API Documentation
Documentation for this API can be found at http://127.0.0.1:8000/docs, when you run the application locally

## Tools
Tools used during the development of this API are:
- [OpenAPI/Swagger](https://swagger.io/specification/) - This is a tool for documenting the API
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - This is the authentication library for Django rest framework
- [Django-auth](https://docs.djangoproject.com/en/4.0/topics/auth/) - Tool for user authorization
- [Django_Rest_framework](https://www.django-rest-framework.org/) - Framework for Django to integrate and develop rest api
- [Django](https://www.djangoproject.com/) - high-level Python web framework that encourages rapid development
- [Docker](https://www.docker.com/) - Virtualization tool to contain the application backend

## Requirements
- Python 2.7.1x+. preferably use Python 3.x.x+

## Tests
Even God commands us to run tests: 1 Thessalonians 5:21; "Test all things."
So to run tests, go to your command line prompt and execute the following command

```
    sh
    $cd Django_Blog_Project
    $ python manage.py test posts

```
## Endpoint Brief
This is the brief of all the endpoints available with this api set.
Endpoint                           |   HTTP Verb   
-----------------------------------|---------------
/                                  |   GET         
/:pk/                              |   GET         
users/                             |   GET         
users/:pk/                         |   GET         
/rest-auth/registration            |   POST        
/rest-auth/login                   |   POST        
/rest-auth/logout                  |   GET         
/rest-auth/password/reset          |   POST        
/rest-auth/password/reset/confirm  |   POST          


## Running the application
To run this application on a linux box, clone the repository and execute the following command.
```
    sh
    $ cd Django_Blog_Project
    $ pip install pipenv
    $ pipenv install
    $ pipenv shell
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py test posts
    $ python manage.py runserver

```

# Django_Blog_Project commit history
Pseudo Blog application made using Django
1. Developing a backend using django-rest framework for a blog application.
2. Added Django structure for blog project and added post app.
3. Adding model for post : Author, title , body , createdAt , updatedAt. will be using default auth model for the user. This will  import the user from or auth into the model and will help in avoiding duplication.
4. Added basic testcase for checking our model for posts.
5. Added Django rest framework and added default permissions.
6. Endpoints are added for the api. PostList: to get the list of all blogs, PostDetail: to get the detail of specific blog.
7. Added test User and login feature for now on endpoints.
8. changing permissions at view level for better access.
9. Adding permission at project level as it can be hard to manage multiple views.
10. Implementing token based authentication on django.
11. Using django-rest-auth in combination with django-allauth to simplify authentication endpoint creation for sign-in, sign-up and sign-out.
12. Setting django auth for sign up and email backend service. will console log email for now.
13. functionality endpoints added so far :
/                                  |   GET         
/:pk/                              |   GET         
users/                             |   GET         
users/:pk/                         |   GET         
/rest-auth/registration            |   POST        
/rest-auth/login                   |   POST        
/rest-auth/logout                  |   GET         
/rest-auth/password/reset          |   POST        
/rest-auth/password/reset/confirm  |   POST  
14. Adding two endpoints one to get list of all the users and other to get a specific user.
15. Added viewset and routes to eliminate multiple views for multiple endpoints.
16. Adding documentation for the endpoints.
17. Adding schema for the API and default documentation.
18. Dockerized the whole app.