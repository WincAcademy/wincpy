from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/home')
def redirect_index():
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', title='Index')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/lon')
def lon():
    return render_template('lon.html', title='League of Nations')
