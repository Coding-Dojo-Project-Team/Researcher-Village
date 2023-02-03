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

@app.route('/tasks/to_db/<int:id>', methods=["POST"])      
def task(id):
    if 'user_id' not in session:
        return redirect("/")
    if not Task.validate_task(request.form):
        return redirect(f"/project/{id}")
    data = {
        "task": request.form['task'],
        "status": 'To Do',
        "date": request.form['date'],
        'project_id': id,
        "user_id": session["user_id"]
    }
    Task.task_insert(data)  
    return redirect(f"/project/{id}")

@app.route("/task/delete/<int:id>/<int:proj_id>")
def delete_tasks(id,proj_id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : id
    }
    Task.delete_task(data)
    return redirect(f"/project/{proj_id}")

@app.route("/task/edit/<int:id>/<int:proj_id>")
def task_edit_page (id, proj_id):
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "id" : id,  
    }
    return render_template("updated_task.html", task = Task.get_one_task(data))

@app.route('/task/update/<int:id>/<int:proj_id>', methods=['POST'])
def update_task(id,proj_id):
    if 'user_id' not in session:
        return redirect("/")
    if not Task.validate_task(request.form):
        return redirect(f"/task/edit/{id}/{proj_id}")
    data = {
        'task': request.form['task'],
        'date': request.form['date'],
        'status': request.form['status'],
        'id': id,
    }
    Task.task_edit(data)
    return redirect(f"/project/{proj_id}")