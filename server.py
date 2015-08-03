import os
import uuid

from flask import Flask, render_template

from models.project import Project

app = Flask(__name__)

projectpaths = [
    r"F:\gis_data"
]

project_index = {}
projects = []


def get_projects(folders):
    for folder in projectpaths:
        for root, dirs, files in os.walk(folder):
            for name in files:
                if name.endswith(".qgs"):
                    project = Project.from_xml(os.path.join(root, name))
                    project_index[project.id] = project
                    yield project

@app.context_processor
def inject_projects():
    return dict(projects=projects)

@app.route("/<project>")
def view_project(project):
    data = project_index[project]
    return render_template("project.html", project=data)


@app.route("/")
def hello():
    return render_template("template.html", projects=projects)


def _init():
    global projects
    projects = list(get_projects(projectpaths))

if __name__ == "__main__":
    _init()
    app.run(debug=True)

