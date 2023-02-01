#from crypt import methods

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
    # don't we want all projects to show in dashboard?
    return render_template("dashboard.html", user=User.get_user_id(data))

@app.route('/project')
def projects():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    # should project page return a project by id with its tasks?
    return render_template("project.html",user=User.get_by_id(data), new_system = Project.get_all_projects())

@app.route('/projects/to_db', methods=["POST"])      
def project():
    if 'user_id' not in session:
        flash("You must be logged in to add a project.")
        return redirect("/")
    valid_project = Project.project_insert(request.form)  #<----Create form validation in model and then add condition for this here.
    return redirect("/dashboard") 

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
    return render_template("update.html", user=User.get_by_id(data)) #<--"Place Holder" = Project.get_one_project(data)
