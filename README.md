# Django_Blog_Project
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
            |Endpoint                           |HTTP Verb|
            |-----------------------------------|---------|
            |/                                  |GET      |
            |/:pk/                              |GET      |
            |/rest-auth/registration            |POST     |
            |/rest-auth/login                   |POST     |
            |/rest-auth/logout                  |GET      |
            |/rest-auth/password/reset          |POST     |
            |/rest-auth/password/reset/confirm  |POST     |
14. Adding two endpoints one to get list of all the users and other to get a specific user.
15. Added viewset and routes to eliminate multiple views for multiple endpoints.
16. Adding documentation for the endpoints.
17. Adding schema for the API and default documentation.
18. dockerized the whole app.