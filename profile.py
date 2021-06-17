from flask import Flask, redirect, url_for, render_template, send_file

profile = Flask(__name__)

@profile.route("/home")
def home():
    return render_template("home.html")
@profile.route("/")
def hm():
    return render_template("home.html")
@profile.route("/admin")
def admin():
    return redirect(url_for("home"))
@profile.route("/journey")
def journey():
    return render_template("journey.html")


if __name__ == "__main__":
    profile.run()