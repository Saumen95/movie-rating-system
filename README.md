## movie-rating-system
A Django based Movie Rating System

## Technology:
1. Django 5.3
2. DB: MySQL

# <u>Design and Consideration:</u>

# User Authentication:
Django comes with a built-in user authentication system. To use it, you'll need to create user registration and login forms. Django's UserCreationForm and AuthenticationForm can be used for this purpose.

# Custom Profile to add phone Number to User Registration:

Incorporating a phone number field to the User model in your movie rating application involves extending Django's built-in user model. Given the context of our application, using a profile model to extend the User model with a one-to-one relationship is a practical approach. This method allows you to add additional user information, such as a phone number, without altering the existing user model directly.

## Commands:
* Install Django:
`pip install django
`
* Create Project:
  `django-admin startproject movie_rating_system
`
* Create App:
`python manage.py startapp ratings
`
* Create SuperUser:
  'python manage.py createsuperuser'

MySQL Config will be found in the settings.py file

## Features:
1. Create, update, delete Movies and Users
2. User Specific rating system
3. User Authentication
