#from crypt import methods

from flask import flash, redirect, render_template, request, session

from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project
from flask_app.models.task import Task


@app.route("/post")
def post_task():
    return render_template("post.html")

# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data ={
#         'id': session['user_id']
#     }
#     return render_template("dashboard.html", project=Project.get_by_id(data))

@app.route('/task')
def tasks():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("project.html",project=Project.get_by_id(data), new_system = Task.get_all_tasks())

@app.route('/tasks/to_db', methods=["POST"])      
def task():
    if 'user_id' not in session:
        return redirect("/")
    if not Task.validate_task(request.form):
        return redirect("/post")
    data = {
        "task": request.form['task'],
        "status": request.form['status'],
        "date": request.form['date'],
        "user_id":session["user_id"]
    }
    Task.task_insert(data)  
    return redirect("/task")

@app.route("/task/delete/<int:id>")
def delete_tasks(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : id
    }
    Task.delete_task(data)
    return redirect("/project")

@app.route("/task/edit/<int:id>")
def edit_tasks (id):
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "id" : id,  
    }
    return render_template("update.html", project=Project.get_by_id(data)) #"Place Holder" = Task.get_one_task(data)
