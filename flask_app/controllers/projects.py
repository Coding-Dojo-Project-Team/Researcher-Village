from crypt import methods

from flask import flash, redirect, render_template, request, session

from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project

@app.route("/post")
def post_project():
    return render_template("post.html")

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html", user=User.get_by_id(data))

@app.route('/project')
def projects():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("project.html",user=User.get_by_id(data), new_system = Project.get_all_projects())

@app.route('/projects/to_db', methods=["POST"])      
def project():
    if 'user_id' not in session:
        return redirect("/")
    if not Project.validate_project(request.form):
        return redirect("/post")
    data = {
        "project_name": request.form['project_name'],
        "category": request.form['category'],
        "user_id":session["user_id"]
    }
    Project.project_insert(data)  
    return redirect("/project")

@app.route("/project/delete/<int:id>")
def delete_project(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : id
    }
    Project.delete_project(data)
    return redirect("/project")

@app.route("/project/edit/<int:id>")
def edit_project (id):
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "id" : id,  
    }
    return render_template("update.html", user=User.get_by_id(data), "Place Holder" = Project.get_one_project(data))
