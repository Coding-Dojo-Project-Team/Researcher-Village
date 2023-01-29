from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Project:
    db = "group_projects"
    def __init__(self,data):
        self.id = data['id']
        self.project_name = data['projeect_name']
        self.category = data['category']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def project_insert(cls,data):
        query = "INSERT INTO projects (project_name, category, user_id) VALUES(%(project_name)s,%(category)s, %(user_id)s);"
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
                    "year" : project_dictionary ['year'],
                    "password" : project_dictionary['password'],
                    "created_at" : project_dictionary['users.created_at'],
                    "updated_at" : project_dictionary['users.updated_at'],
                }

                user_obj = User(user_dictionary)

                project_obj.user = user_obj

                all_projects.append(project_obj)
            return all_projects
        
    @classmethod
    def get_one_project(cls,data):
        query = "SELECT * FROM project JOIN users ON project.user_id = users.id WHERE project.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        
        if len(results) == 0:    
            return None
        else: 
            project_dictionary = results[0]
            project_obj = cls(results[0])
            user_dictionary = {
                    "id" : project_dictionary['users.id'],
                    "first_name" : project_dictionary['first_name'],
                    "last_name" : project_dictionary['last_name'],
                    "email" : project_dictionary['email'],
                    "year" : project_dictionary ['year'],
                    "password" : project_dictionary['password'],
                    "created_at" : project_dictionary['users.created_at'],
                    "updated_at" : project_dictionary['users.updated_at'],
                }

            project_obj = User(user_dictionary)

            project_obj.user = user_obj
            return project_obj
        
    @staticmethod
    def validate_project(form_data):
        is_valid = True
        print(form_data)
        return is_valid   # Please let me know desired validations so I can enter them
    
    @classmethod
    def delete_project(cls, data):
        query = "DELETE FROM project WHERE id =%(id)s"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def project_edit(cls, data):
        query = "UPDATE project SET project_name = %(project_name)s, category = %(category)s WHERE id =%(id)s"
        return connectToMySQL(cls.db).query_db(query,data)
