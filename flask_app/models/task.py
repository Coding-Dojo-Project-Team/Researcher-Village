from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User
from flask_app.models.project import Project

class Task:
    db = "group_project"
    def __init__(self,data):
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None


    @classmethod
    def task_insert(cls,data):
        query = "INSERT INTO tasks (task, date, status, project_id) VALUES(%(task)s,%(date)s,%(status)s %(project_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all_tasks(cls):
        query = "SELECT * FROM tasks JOIN users ON tasks.project_id = project.id;"

        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        
        if len(results) == 0:              
            return[]
        else: 
            all_tasks = []
            for task_dictionary in results:              
                task_obj = cls(task_dictionary)
                project_dictionary = {
                    "id" : task_dictionary['project.id'],
                    "task" : task_dictionary['task'],
                    "date" : task_dictionary['date'],
                    "status" : task_dictionary['status'],
                    "created_at" : task_dictionary['users.created_at'],
                    "updated_at" : task_dictionary['users.updated_at'],
                }

                project_obj = Project(project_dictionary)

                task_obj.user = project_obj

                all_tasks.append(task_obj)
            return all_tasks
        
    @classmethod
    def get_one_task(cls,data):
        query = "SELECT * FROM tasks JOIN projects ON task.project_id = projects.id WHERE task.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        
        if len(results) == 0:    
            return None
        else: 
            task_dictionary = results[0]
            task_obj = cls(results[0])
            project_dictionary = {
                    "id" : task_dictionary['project.id'],
                    "task" : task_dictionary['task'],
                    "date" : task_dictionary['date'],
                    "status" : task_dictionary['status'],
                    "created_at" : task_dictionary['projects.created_at'],
                    "updated_at" : task_dictionary['projects.updated_at'],
                }

            task_obj = Project(project_dictionary)

            task_obj.project = project_obj
            return task_obj
        

    @staticmethod
    def validate_task(form_data):
        is_valid = True
        print(form_data)
        return is_valid 
    
    @classmethod
    def delete_task(cls, data):
        query = "DELETE FROM tasks WHERE id =%(id)s"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def task_edit(cls, data):
        query = "UPDATE tasks SET task = %(task)s, date = %(date)s, status = %(status)s WHERE id =%(id)s"
        return connectToMySQL(cls.db).query_db(query,data)