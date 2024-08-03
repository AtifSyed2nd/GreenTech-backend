# Jamiatul Irshad

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
The main settings of the project are stored in core app.You can refer to requirements.txt file to check what modules have been installed.

## User Authentication

For User Authentication we have used PyJWT.
In user_auth app in views we have created a LoginView. Inside this view we are encoding the jwt token.
And in middleware called custom_authentication.py in the same app we are decoding the jwt token.

## Records

In records we have created 2 models called Statistics and Expenses.



