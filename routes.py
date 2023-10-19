from sqlalchemy.sql import text, exists
from app import app
from flask import redirect, render_template, request, session
from db import db
import users
import recipes

from werkzeug.security import check_password_hash, generate_password_hash
 
@app.route("/")
def index():
    return render_template("index.html") 
    
    
@app.route("/Kirjaudu_sisaan",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
        
    if not users.login(username, password):
    	message = "Väärä käyttäjätunnus tai salasana"
    	return render_template("index.html", message = message)
        
    return redirect("/")
    

@app.route("/Kirjaudu_ulos")
def logout():
    users.logout()
    return redirect("/")
    

@app.route("/uusi_tunnus")
def new_user():
    return render_template("register.html")
 
      
@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if len(username) < 1 or len(username) > 25:
        message = "Käyttäjänimen on oltava vähintään 1 ja maksimissaan 25 merkkiä pitkä"
        return render_template("register.html", message = message)   	
    if  password1 != password2:
        message = "Salasanat eivät täsmää"
        return render_template("register.html", message = message)
    if  password1 == "":
        message = "Sinun on luotava salasana"
        return render_template("register.html", message = message)    

    if not users.create_user(username, password1):
        message = "Rekistetöinti ei onnistunut. Käyttäjänimi on jo käytössä."
        return render_template("register.html", message=message)
    return redirect("/")    	
    
    
    
@app.route("/luo-uusi-resepti")
def new_recipe():
    return render_template("new_recipe.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form["title"]
    recipe =request.form["message"]
    category = request.form["category"]
    user_id = session["user_id"]
    sql = f"INSERT INTO recipe (category_id, name, content, user_id) VALUES ('{category}','{name}', '{recipe}', '{user_id}')"
    db.session.execute(text(sql))
    db.session.commit()
    return render_template("move.html", message = "Reseptin luonti onnistui!")

    
@app.route("/selaa/", methods=["GET","POST"])
def browse():
    category = request.form.get("category")
    user_id = session["user_id"]
    
    
    if category != "4":
    	sql = f"SELECT recipe.id, recipe.name, recipe.content  FROM recipe, category WHERE category.id =recipe.category_id AND category.id = {category}";
    	sql1 = f"SELECT category.name FROM category WHERE category.id = {category}";
    	data = db.session.execute(text(sql))
    	data1=db.session.execute(text(sql1))
    	row = data1.fetchone()
    	header= row[0]
    else:
    	sql = f"SELECT recipe.id, recipe.name, recipe.content FROM recipe";
    	data = db.session.execute(text(sql))
    	header ="Kaikki reseptit"
    
    	
   
    return render_template("browse.html", header = header, data = data )  
 
@app.route("/favourites/<int:recipe_id>", methods=["GET","POST"])

def favourites(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    user_id = session["user_id"]
    in_favourites = recipes.check_if_in_favourites(recipe.id, user_id)
    
    if in_favourites == False:
    	recipes.add_to_favourites(recipe.id, user_id)
    	in_favourites = True
    else:
    	recipes.delete_from_favourites(recipe.id,user_id)
    	in_favourites = False

    return render_template("recipe.html", name = recipe[0], content = recipe[1], user_id =user_id, recipe_id = recipe_id, in_favourites = in_favourites)    
    
@app.route("/suosikit", methods=["GET","POST"])
def browse_favourites():
    user_id = session["user_id"]
    data = recipes.get_favourites(user_id)
    header = "Suosikit"
    return render_template("favourites.html", header = header, data = data ) 

@app.route("/omat_sivut", methods=["GET","POST"])
def move():
    user_id = session["user_id"]
    sql = f"SELECT recipe.name, recipe.content, id FROM recipe WHERE recipe.user_id = {user_id}";
    data = db.session.execute(text(sql))
    return render_template("userpage.html", data = data)
    
@app.route("/delete_recipe/<int:recipe_id>", methods=["GET","POST"])   
def delete(recipe_id):
    user_id = session["user_id"]
    recipes.delete_recipe(recipe_id)
    return render_template("move_delete.html", message = "Reseptin poisto onnistui!")
    


@app.route("/recipe/<int:recipe_id>", methods=["GET"])
def open_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    user_id = session["user_id"]
    recipe_id = recipe_id
    in_favourites = recipes.check_if_in_favourites(recipe.id, user_id)

    return render_template("recipe.html", name = recipe[0], content = recipe[1], user_id =user_id, recipe_id = recipe_id, in_favourites = in_favourites) 
    




    

    


