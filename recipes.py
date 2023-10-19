import os
from db import db
from sqlalchemy.sql import text
from flask import request, session


def delete_recipe(recipe_id):
    sql = f"DELETE FROM favourites WHERE recipe_id = {recipe_id}"   
    db.session.execute(text(sql))
    sql = f"DELETE FROM recipe WHERE id = {recipe_id}"
    db.session.execute(text(sql))          
    db.session.commit()


def get_recipe(recipe_id):
    sql = f"SELECT recipe.name, recipe.content, recipe.id FROM recipe WHERE id = {recipe_id}"   
    return db.session.execute(text(sql)).fetchone()
    
def add_to_favourites(recipe_id, user_id):
    sql = f"INSERT INTO favourites (recipe_id, user_id) VALUES ('{recipe_id}','{user_id}')"
    db.session.execute(text(sql))
    db.session.commit()

def check_if_in_favourites(recipe_id, user_id):
    sql = f"SELECT recipe_id FROM favourites WHERE user_id = {user_id}"
    data = db.session.execute(text(sql)).fetchall()
    check = list(data)
    result = [i[0] for i in check]
    if recipe_id in result:
    	return True
    else:
    	return False
    	    	
def delete_from_favourites(recipe_id,user_id):
    sql = f"DELETE FROM favourites WHERE recipe_id = {recipe_id} AND user_id = {user_id}"   
    data =db.session.execute(text(sql))
    db.session.commit()
    
def get_favourites(user_id):
    sql = f"SELECT recipe.name, recipe.content, recipe.id FROM recipe WHERE recipe.id IN (SELECT recipe_id FROM favourites WHERE user_id = {user_id}) ORDER BY recipe.name"   
    return db.session.execute(text(sql))
    

