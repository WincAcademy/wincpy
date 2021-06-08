# Do not modify these two lines.

__winc_id__ = 'cfcf9de827a34e539ce924062dbafeb1'
__human_name__ = 'spa'

# Implement your program below.
from flask import Flask, render_template
import helpers


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html'), 200
