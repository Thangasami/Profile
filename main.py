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

@app.route("/reach")
def reach():
    return render_template("reach.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/download")
def download_file():
    p = "resume.pdf"
    return send_file(p,as_attachment=True)

if __name__ == "__main__":
    app.run()