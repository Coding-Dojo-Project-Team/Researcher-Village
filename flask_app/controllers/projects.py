#from crypt import methods

from flask import flash, redirect, render_template, request, session

from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project
from datetime import timedelta, date

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
    return render_template("dashboard.html", user=User.get_user_id(data), projects = Project.get_all_projects())

@app.route('/project/<int:id>')
def projects(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id':id
    }
    user_data ={
        'id': session['user_id']
    }
    project_dictionary = Project.get_by_id(data)
    time = project_dictionary.date
    due_soon = time + timedelta(days= -2)
    over_due = time + timedelta(days= +1)
    current_time = date.today()
    # should project page return a project by id with its tasks?
    return render_template("project.html",user=User.get_user_id(user_data), project = Project.get_one_project(data), due_soon= due_soon, current_time=current_time, over_due=over_due)

@app.route('/projects/to_db', methods=["POST"])      
def project():
    if 'user_id' not in session:
        flash("You must be logged in to add a project.")
        return redirect("/")
    valid_project = Project.validate_project(request.form)
    if not valid_project:
        return redirect('/post')
    data = {
        'project_name': request.form['project_name'],
        'category': request.form['category'],
        'date': request.form['date'],
        'user_id': session['user_id']
    }
    Project.project_insert(data)
    return redirect("/dashboard")

@app.route('/project/edit/<int:id>')
def update(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        'id': id
    }
    user_data = {
        'id' : session['user_id']
    }
    return render_template('update.html', user = User.get_user_id(user_data), project = Project.get_by_id(data))

@app.route("/project/delete/<int:id>")
def delete_project(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : id
    }
    Project.delete_project(data)
    return redirect("/dashboard")


@app.route("/project/update/<int:id>", methods=['POST'])
def edit_project (id):
    if 'user_id' not in session:
        return redirect("/")
    valid_project = Project.validate_project(request.form)
    if not valid_project:
        return redirect(f'/project/edit/{id}')
    data = {
        'project_name': request.form['project_name'],
        'category': request.form['category'],
        'date': request.form['date'],
        'id': id
    }
    Project.project_edit(data)
    return redirect(f"/project/{id}")
