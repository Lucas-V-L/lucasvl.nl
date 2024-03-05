from flask import Flask, render_template, request, abort
import re
app = Flask(__name__)

from os import listdir
from os.path import isfile, join, getmtime

def getProjectTime(name):
    return getmtime(join("templates/pages/projects", name))

def getProjects():
    projects = [f for f in listdir("templates/pages/projects") if isfile(join("templates/pages/projects", f)) and f[-5:] == ".html"]
    projects.sort(key=getProjectTime, reverse=True)
    return projects

def getTools():
    return []

valid_ID = re.compile("/^[^a-z]+|[^\w:.-]+/gi")

@app.route("/")
def home():
    return render_template("index.html",\
            homepage=render_template("pages/homepage.html"),\
            aboutpage=render_template("pages/aboutpage.html"),\
            radiopage=render_template("pages/Radio.html"),\
            render_template=render_template,\
            re=re,\
            valid_ID=valid_ID,\
            projects=getProjects(),\
            tools=getTools())

@app.route("/plain")
def plain_home():
    return render_template("plain.html",\
            content=render_template("pages/homepage.html"),\
            pageName="Home",\
            projects=getProjects(),\
            tools=getTools())

@app.route("/plain/about")
def plain_about():
    return render_template("plain.html",\
            content=render_template("pages/aboutpage.html"),\
            pageName="About",\
            projects=getProjects(),\
            tools=getTools())

@app.route("/projects/<project>")
def projectviewer(project):
    if project in getProjects():
        return render_template("plain.html",\
                content=render_template(join("pages/projects", project)),\
                re=re,\
                valid_ID=valid_ID,\
                projects=getProjects(),\
                tools=getTools())
    abort(404)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
