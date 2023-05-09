import os

from flask import Flask, redirect, render_template, request, session, url_for

from helpers import get_users, hash_password

# Don't modify this
__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

# You can modify everything from here
app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        print(request.args.get("error"))
        return render_template("login.html", error=request.args.get("error"))
    elif request.method == "POST":
        users = get_users()
        attempted_password = hash_password(request.form["password"])

        try:
            username = request.form["username"]
            stored_password = users[username]
        except KeyError:
            return redirect(url_for("login", error=True))

        if stored_password == attempted_password:
            session["username"] = request.form["username"]
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("login", error=True))


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        bonus_words = [
            "application",
            "association",
            "bark",
            "anchor",
            "authority",
            "business",
            "busy",
            "class",
            "clap",
        ]
        return render_template(
            "dashboard.html", username=session["username"], words=bonus_words
        )
    else:
        return redirect(url_for("login"))


@app.route("/logout", methods=["GET", "POST"])
def logout():
    try:
        session.pop("username", None)
    except:
        # User was not logged in. That's fine.
        pass
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
