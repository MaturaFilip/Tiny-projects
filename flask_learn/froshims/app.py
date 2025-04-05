from flask import Flask, render_template, request

# refers to this file name
app = Flask(__name__)

# define route -> what should happen when you visit /
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    
    if not request.form.get("name") or not request.form.get("sport"):
        return render_template("failure.html")
    return render_template("success.html")