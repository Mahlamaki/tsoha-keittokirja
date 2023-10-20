from db import db
from sqlalchemy.sql import text


def add_like(recipe_id, user_id):
    sql = f"INSERT INTO likes (recipe_id, user_id) VALUES ('{recipe_id}','{user_id}')"
    db.session.execute(text(sql))
    db.session.commit()
    
def delete_like(recipe_id, user_id):
    sql = f"DELETE FROM likes WHERE recipe_id = {recipe_id} AND user_id = {user_id}"   
    data =db.session.execute(text(sql))
    db.session.commit()    
    
def count_likes(recipe_id):
    sql = f"SELECT COUNT(*) FROM likes WHERE recipe_id = {recipe_id}"   
    return db.session.execute(text(sql)).fetchone()
    
def check_if_liked(recipe_id, user_id):
    sql = f"SELECT EXISTS (SELECT 1 FROM likes WHERE recipe_id = {recipe_id} AND user_id = {user_id}) AS liked"   
    return db.session.execute(text(sql)).fetchone()
