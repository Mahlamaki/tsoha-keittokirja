from sqlalchemy.sql import text, exists
from app import app
from flask import redirect, render_template, request, session
from db import db
from werkzeug.security import check_password_hash, generate_password_hash
 
@app.route("/")
def index():
    return render_template("index.html") 
    
    
@app.route("/Kirjaudu_sisaan",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = f"SELECT id, password FROM users WHERE username= '{username}'"
    result = db.session.execute(text(sql))
    user = result.fetchone()
    message = "Väärä käyttäjätunnus tai salasana"    
    if not user:
        return render_template("index.html", message = message)
    else:
        hash_value = user.password
    if check_password_hash(hash_value, password):
        session["username"] = username
    else:
        return render_template("index.html", message = message)
 
    return redirect("/")
    

@app.route("/Kirjaudu_ulos")
def logout():
    del session["username"]
    return redirect("/")
    
    
@app.route("/uusi_tunnus")
def new_user():
    return render_template("register.html")
      
@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    
    if  password1 == password2:
        password = password1
        hash_value = generate_password_hash(password)
        sql = f"INSERT INTO users (username, password) VALUES ('{username}', '{hash_value}')"
        db.session.execute(text(sql))
        db.session.commit()
    else:
        message = "Salasanat eivät täsmää"
        return render_template("register.html", message = message)
    	
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
    
@app.route("/selaa/", methods=["GET","POST"])
def browse():
    category = request.form.get("category")
    
    if category != "4":
    	sql = f"SELECT recipe.name, recipe.content, category.name  FROM recipe, category WHERE category.id =recipe.category_id AND category.id = {category}";
    	data = db.session.execute(text(sql))
    	row = data.fetchone()
    	header= row[2]
    else:
    	sql = f"SELECT recipe.name, recipe.content FROM recipe";
    	data = db.session.execute(text(sql))
    	header ="Kaikki reseptit"
    	
   
    return render_template("browse.html", header = header, data = data )  

    


