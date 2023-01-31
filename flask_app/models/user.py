from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Bcrypt = Bcrypt(app)

db = "group_project"
class User:
    def __init__(self, user):
        self.id = user['id']
        self.first_name = user['first_name']
        self.last_name = user['last_name']
        self.year = user['year']
        self.email =user['email']
        self.password = user['password']
        self.created_at = user['created_at']
        self.updated_at = user['updated_at']

    @classmethod
    def authenticated_user_by_input(cls, user_input):
        valid = True
        existing_user = cls.get_user_email(user_input["email"])
        password_valid = True

        if not existing_user:
            valid = False
        else:
            password_valid = bcrypt.check_password_hash(
            existing_user.password, user_input['password'])
            if not password_valid:
                valid =False
        if not valid:
            flash("Email or password does not match.", "Login")
            return False
        return existing_user

    @classmethod
    def get_user_id(cls, user_id):
        data = {"id": user_id}
        query = "SELECT * FROM user WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query,data)

        if len(result) <1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_email(cls, email):
        data= {"email": email}
        query = "SELECT * FROM user WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query, data)

        if len(result) <1:
            return False
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * from user;"
        user_data = connectToMySQL(db).query_db(query)

        users = []
        for user in user_data:
            users.append(cls(user))
        return users

    @classmethod
    def create_valid_user(cls, user):

        if not cls.is_valid(user):
            return False

        pw_hash = bcrypt.generate_password_hash(user['password'])
        user = user.copy()
        user['password'] = pw_hash

        query = """
                INSERT into user (first_name, last_name, year, email, password)
                VALUES (%(first_name)s, %(last_name)s, %(year)s, %(email)s, %(password)s;"""
        new_user_id = connectToMySQL(db).query_db(query, user)
        new_user = cls.get_user_id(new_user_id)
        return (new_user)

    @classmethod
    def is_valid(cls, user):
        valid = True

        if len(user['first_name']) <2:
            flash("First name must be at least 2 characters.","Register")
            valid = False
        if len(user['last_name']) <2:
            flash("Last name must be at least 2 character.","Register")
            valid = False
        if len(user['year']) <0:
            flash("Class year is required.","Register")
            valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address format.","Register")
            valid = False
        if len(user['password']) <8:
            flash("Password must be at least 8 characters.","Register")
            is_valid = False
        email_already_has_account = User.get_user_email(user['email'])
        if email_already_has_account:
            flash("email registered to another User.")
            valid = False
        return valid