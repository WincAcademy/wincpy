# Don't modify these variables
__winc_id__ = "cc1b724762854e85a8defa04287f708b"
__human_name__ = "requests"

# Your code below this line
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "<p>Home, sweet home.</p>"


@app.route("/greet/")
@app.route("/greet/<entity>", methods=["GET"])
def greet(entity="world"):
    return f"<h1>Hello, {entity}!</h1>"
