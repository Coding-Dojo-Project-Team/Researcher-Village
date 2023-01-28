from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Project:
    db = "project_schema"
    def __init__(self,data):
        self.id = data['id']
        self.project_name = data['projeect_name']
        self.category = data['category']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def project_insert(cls,data):
        query = "INSERT INTO projects (project_name, category, user_id) VALUES(%(project_name)s,%(cetgory)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all_projects(cls):
        query = "SELECT * FROM projects JOIN users ON projects.user_id = users.id;"

        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        
        if len(results) == 0:              
            return[]
        else: 
            all_projects = []
            for project_dictionary in results:              
                project_obj = cls(project_dictionary)
                user_dictionary = {
                    "id" : project_dictionary['users.id'],
                    "first_name" : project_dictionary['first_name'],
                    "last_name" : project_dictionary['last_name'],
                    "email" : project_dictionary['email'],
                    "class"
                    "password" : project_dictionary['password'],
                    "created_at" : project_dictionary['users.created_at'],
                    "updated_at" : project_dictionary['users.updated_at'],
                }

                user_obj = User(user_dictionary)

                project_obj.user = user_obj

                all_projects.append(project_obj)
            return all_projects
