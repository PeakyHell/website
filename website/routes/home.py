from flask import Blueprint, render_template


home = Blueprint("Home", __name__)


# Routes
@home.get("/")
def hello_world():
    return render_template("index.html")
