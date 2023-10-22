from db import db
from sqlalchemy.sql import text

def add_recipe(category,name,recipe,user_id):
    sql = f"INSERT INTO recipe (category_id, name, content, user_id) VALUES ('{category}','{name}', '{recipe}', '{user_id}')"
    db.session.execute(text(sql))
    db.session.commit()
    
def delete_recipe(recipe_id):
    sql = f"DELETE FROM likes WHERE recipe_id = {recipe_id}"   
    db.session.execute(text(sql))
    sql = f"DELETE FROM favourites WHERE recipe_id = {recipe_id}"   
    db.session.execute(text(sql))
    sql = f"DELETE FROM recipe WHERE id = {recipe_id}"
    db.session.execute(text(sql))          
    db.session.commit()

def get_recipe(recipe_id):
    sql = f"SELECT recipe.name, recipe.content, recipe.id FROM recipe WHERE id = {recipe_id}"   
    return db.session.execute(text(sql)).fetchone()
    
def get_by_category(category):
    sql = f"SELECT recipe.id, recipe.name, recipe.content  FROM recipe, category WHERE category.id =recipe.category_id AND category.id = {category} ORDER BY recipe.name";
    return db.session.execute(text(sql))

def get_category(category):
    sql = f"SELECT category.name FROM category WHERE category.id = {category}";
    return db.session.execute(text(sql)).fetchone()
    
def all_recipes():
    sql = f"SELECT recipe.id, recipe.name, recipe.content FROM recipe ORDER BY recipe.name";
    return db.session.execute(text(sql))
    
def get_my_recipes(user_id):
    sql = f"SELECT recipe.name, recipe.content, id FROM recipe WHERE recipe.user_id = {user_id} ORDER BY recipe.name";
    return db.session.execute(text(sql))   
