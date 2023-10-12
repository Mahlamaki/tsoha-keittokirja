CREATE TABLE recipe(id SERIAL PRIMARY KEY, category_id INTEGER REFERENCES category, name TEXT, content TEXT);

CREATE TABLE category(id SERIAL PRIMARY KEY, name TEXT);

CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);

CREATE TABLE favourites(id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users, recipe_id INTEGER REFERENCES recipe);
