### INF601 - Advanced Programming in Python
### Raymond Lee
### Mini Project 3


# Mini Project 3

## Description

This project is web application designed to allow users to read, write, and interact with movie reviews.
The application, built with Flask web framework and utilizing HTML and Jinja2 for templating, incorporates user 
authentication features. Users can register, log in, and log out seamlessly within the system. Users can create accounts
with unique usernames, email, bios, and passwords. Once logged in, users can access their user profile page, which 
displays information such as their username and other profile details. Users can also edit their profile information,
such as their email address, bio, and username. Users can browse a list of movies and read reviews submitted by other 
users. They can also submit their own reviews for movies they have watched. The security of the application includes 
secure password storage using hashing algorithms and session management to track user sessions. For database 
integration, the application connects with a SQL light database to store user information, movie details, and reviews. 
This allows for efficient data management and retrieval, ensuring that the application can handle a large number of 
users and reviews. CSS and Bootstrap are implemented with HTML in application primarily for styling and layout purposes.

## Getting Started

### Dependencies

* [Flask](https://flask.palletsprojects.com/en/3.0.x/)
* [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Jinja2](https://flask.palletsprojects.com/en/3.0.x/templating/#jinja-setup)


### Pip install instructions

Please run the following:
```
pip install -r requirements.txt
```

### Executing program

In a terminal window, please type the following: <br>
Setup Database

```
flask --app flaskr init-db
```
Run application

```
flask --app flaskr run 

```

## Authors

Contributors names and contact info

ex. Raymond Lee 

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License.

## Acknowledgments

Inspiration, code snippets, etc.
* [Flask Tutorial](https://flask.palletsprojects.com/en/3.0.x/tutorial/)
