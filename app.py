from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')


# open index.html (homepage)
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


# open about.html
@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")


# open mailto.html
@app.route("/mailto", methods=["GET", "POST"])
def mailto():
    return render_template("mailto.html")


# open projects.html
@app.route("/projects", methods=["GET", "POST"])
def projects():
    return render_template("projects.html")