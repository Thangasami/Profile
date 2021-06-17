from flask import Flask, redirect, url_for, render_template, send_file

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/")
def hm():
    return render_template("home.html")
@app.route("/admin")
def admin():
    return redirect(url_for("home"))
@app.route("/journey")
def journey():
    return render_template("journey.html")


if __name__ == "__main__":
    app.run()