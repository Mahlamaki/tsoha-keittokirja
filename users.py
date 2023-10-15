import os
from db import db
from sqlalchemy.sql import text
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash


    
 
def login(username,password):
        
    sql = f"SELECT id, password FROM users WHERE username= '{username}'"
    result = db.session.execute(text(sql))
    user = result.fetchone()
        
    if not user:
    	return False
        
    if not check_password_hash(user.password, password):
    	return False
    	
    session["user_id"] = user[0]
    session["username"] = username
    return True
    	
    	  
   

def create_user(username, password):
    hash_value = generate_password_hash(password)

    try:
    	sql = f"INSERT INTO users (username, password) VALUES ('{username}', '{hash_value}')"
    	db.session.execute(text(sql))
    	db.session.commit()
    except:
    	return False
    	
    return login(username, password)
    

def logout():
    del session["user_id"]
    del session["username"]
    
    
 

