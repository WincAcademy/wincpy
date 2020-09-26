from flask import Flask, render_template, redirect, url_for

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is an empty Flask project that you need to work on.'
