from app import app
from flask import redirect, render_template, request, session


@app.route("/")
def index():
    return render_template("index.html") 

#@app.route("/luo-uusi-resepti", methods=["POST"])
#def new():
#    if request.method= == "POST":
#        return render_template("new_recipe.html")
