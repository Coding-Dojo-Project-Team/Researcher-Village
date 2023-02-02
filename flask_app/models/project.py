from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User
from flask_app.models.task import Task

class Project:
    db = "group_project"
    def __init__(self,data):
        self.id = data['id']
        self.project_name = data['project_name']
        self.category = data['category']
        self.date = data['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.tasks = []

    @classmethod
    def project_insert(cls,data):
        query = "INSERT INTO projects (project_name, category, date, user_id) VALUES(%(project_name)s,%(category)s,%(date)s,%(user_id)s);"
        print(query)
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
        query = """SELECT * FROM projects 
        JOIN users ON projects.user_id = users.id 
        LEFT JOIN tasks ON projects.id = tasks.project_id 
        WHERE projects.id = %(id)s;"""
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
            user_obj = User(user_dictionary)
            project_obj.user = user_obj
            for dictionary in results:
                task_data = {"id" : dictionary['tasks.id'],
                "task" : dictionary['task'],
                "date" : dictionary['tasks.date'],
                "status" : dictionary['status'],
                "created_at" : dictionary['tasks.created_at'],
                "updated_at" : dictionary['tasks.updated_at'],
                "project_id" : dictionary['project_id'],
                "user_id" : dictionary['tasks.user_id']}
                project_obj.tasks.append(Task(task_data))
            return project_obj
        
    @staticmethod
    def validate_project(form_data):
        is_valid = True
        if len(form_data['project_name']) < 5:
            flash('Your project must have a name of 5 characters or more', 'project')
            is_valid = False
        if len(form_data['category']) == 0:
            flash('Your project must belong to category', 'project')
            is_valid = False
        if len(form_data['date']) == 0:
            flash('Your project must have a due date', 'project')
            is_valid = False
        print(form_data)
        return is_valid
    
    @classmethod
    def delete_project(cls, data):
        query = "DELETE FROM projects WHERE id =%(id)s"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def project_edit(cls, data):
        query = "UPDATE projects SET project_name = %(project_name)s, category = %(category)s, date = %(date)s  WHERE id =%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM projects WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0]) 
    
