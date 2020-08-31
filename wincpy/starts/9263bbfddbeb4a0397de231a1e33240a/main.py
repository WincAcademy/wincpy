from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is an empty Flask project that you need to work on.'
