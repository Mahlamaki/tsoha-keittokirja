from sqlalchemy.sql import text
from app import app
from flask import redirect, render_template, request, session
from db import db

@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/luo-uusi-resepti")
def new_recipe():
    return render_template("new_recipe.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form["title"]
    recipe =request.form["message"]
    category = request.form["category"]
    sql = f"INSERT INTO recipe (category_id, name, content) VALUES ('{category}','{name}', '{recipe}')"
    db.session.execute(text(sql))
    db.session.commit()
    return render_template("move.html")
    

    

    


