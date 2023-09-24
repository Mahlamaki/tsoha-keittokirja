CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);

CREATE TABLE recipe(id SERIAL PRIMARY KEY, creator_id INTEGER REFERENCES users, name TEXT, content TEXT, creation TIMESTAMP);

