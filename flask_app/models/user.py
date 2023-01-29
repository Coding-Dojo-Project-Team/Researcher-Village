from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
import re

EMAIL_ REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Bcrypt = Bcrypt(app)

db = "group_project"
class User:
    def __init__(self, user):
        pass