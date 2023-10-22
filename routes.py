from sqlalchemy.sql import text, exists
from app import app
from flask import redirect, render_template, request, session
from db import db
import users
import recipes
import favourites
import likes

 
@app.route("/")
def index():
    return render_template("index.html") 
    
    
@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]    
    if not users.login(username, password):
    	message = "Väärä käyttäjätunnus tai salasana"
    	return render_template("index.html", message = message)        
    return redirect("/")
    

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
    
    
@app.route("/register")
def new_user():
    return render_template("register.html")
 
      
@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if len(username) < 1 or len(username) > 25:
        return render_template("register.html", message = "Käyttäjänimen on oltava vähintään 1-25 merkkiä pitkä")   	
    if  password1 != password2:
        return render_template("register.html", message = "Salasanat eivät täsmää")
    if  password1 == "":
        return render_template("register.html", message = "Sinun on luotava salasana") 
    if  len(password1) > 25:
        return render_template("register.html", message = "Salasanan tulee olla 1-25 merkkiä pitkä")          
    if users.check_if_user_exists(username)[0]:
        return render_template("register.html", message = "Rekistetöinti ei onnistunut. Käyttäjänimi on jo käytössä.")        
    if not users.create_user(username, password1):
        return render_template("register.html", message = "Rekistetöinti ei onnistunut. Käyttäjänimi on jo käytössä.")
    return redirect("/")    	
    
    
@app.route("/create_new_recipe")
def new_recipe():
    return render_template("new_recipe.html")


@app.route("/send", methods=["POST"])
def send():
    name = request.form["title"]
    recipe =request.form["message"]
    category = request.form["category"]
    user_id = session["user_id"]
    if len(name) < 1 or len(name) > 30:
    	return render_template("new_recipe.html", message = "Reseptin nimessä pitää olla 1-30 merkkiä")
    if len(recipe) < 1 or len(recipe) > 2000:
    	return render_template("new_recipe.html", message = "Reseptin pituuden tulee olla 1-2000 merkkiä")
    recipes.add_recipe(category,name,recipe,user_id)
    return render_template("move.html", message = "Reseptin luonti onnistui!", name = len(name), recipe=len(recipe))

    
@app.route("/browse_recipes/", methods=["GET","POST"])
def browse():
    category = request.form.get("category")
    user_id = session["user_id"]       
    if category != "4":
    	data = recipes.get_by_category(category)
    	category_name = recipes.get_category(category)
    	header= category_name[0]
    else:
    	data = recipes.all_recipes()
    	header ="Kaikki reseptit" 
    return render_template("browse.html", header = header, data = data )  
 
 
@app.route("/favourites/<int:recipe_id>", methods=["GET","POST"])

def favourites_actions(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    user_id = session["user_id"]
    in_favourites = favourites.check_if_in_favourites(recipe.id, user_id) 
    if in_favourites == False:
    	favourites.add_to_favourites(recipe.id, user_id)
    	in_favourites = True
    else:
    	favourites.delete_from_favourites(recipe.id,user_id)
    	in_favourites = False
    liked= likes.check_if_liked(recipe_id, user_id)
    like_count = likes.count_likes(recipe_id)
    return render_template("recipe.html", name = recipe[0], content = recipe[1], user_id =user_id, recipe_id = recipe_id, in_favourites = in_favourites, liked=liked[0], likes = like_count[0]) 
    
    
@app.route("/favourite_recipes", methods=["GET","POST"])
def browse_favourites():
    user_id = session["user_id"]
    data = favourites.get_favourites(user_id)
    header = "Suosikit"
    return render_template("browse.html", header = header, data = data ) 


@app.route("/my_page", methods=["GET","POST"])
def move():
    user_id = session["user_id"]
    data = recipes.get_my_recipes(user_id)
    header = "Omat reseptit"
    return render_template("userpage.html", header = header, data = data)
    
    
@app.route("/delete_recipe/<int:recipe_id>", methods=["POST"])   
def delete(recipe_id):
    user_id = session["user_id"]
    recipes.delete_recipe(recipe_id)
    return render_template("move_delete.html", message = "Reseptin poisto onnistui!")
    

@app.route("/recipe/<int:recipe_id>", methods=["GET"])
def open_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    user_id = session["user_id"]
    recipe_id = recipe_id
    in_favourites = favourites.check_if_in_favourites(recipe_id, user_id)
    liked= likes.check_if_liked(recipe_id, user_id)
    like_count = likes.count_likes(recipe_id)
    return render_template("recipe.html", name = recipe[0], content = recipe[1], user_id =user_id, recipe_id = recipe_id, in_favourites = in_favourites, liked=liked[0], likes = like_count[0]) 
    
    
@app.route("/my_recipe/<int:recipe_id>", methods=["GET"])
def open_my_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    user_id = session["user_id"]
    recipe_id = recipe_id
    like_count = likes.count_likes(recipe_id)
    return render_template("my_recipe.html", name = recipe[0], content = recipe[1], user_id =user_id, recipe_id = recipe_id, likes = like_count[0]) 
    
@app.route("/like/<int:recipe_id>", methods=["GET","POST"])
def like_function(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    user_id = session["user_id"]
    liked= likes.check_if_liked(recipe_id, user_id)     
    if liked[0] == False:
        likes.add_like(recipe_id, user_id)   
    if liked[0] == True:
        likes.delete_like(recipe_id, user_id)    
    in_favourites = favourites.check_if_in_favourites(recipe.id, user_id)
    liked= likes.check_if_liked(recipe_id, user_id)
    like_count = likes.count_likes(recipe_id)
    return render_template("recipe.html", name = recipe[0], content = recipe[1], user_id =user_id, recipe_id = recipe_id, in_favourites = in_favourites, liked=liked[0], likes = like_count[0]) 


    


