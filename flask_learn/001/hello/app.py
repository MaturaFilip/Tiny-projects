from flask import Flask, render_template, request

# refers to this file name
app = Flask(__name__)

# define route -> what should happen when you visit /
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("greet.html", name=name)
    return render_template("index.html")



# GET = see the form, FORM -> process the form
#@app.route("/greet", methods=["POST"]) # defaultně je ["GET"] musí být změněno i v indexu
#def greet():
#    name = request.form.get("name", "world") # args.get
#    return render_template("greet.html", name=name)