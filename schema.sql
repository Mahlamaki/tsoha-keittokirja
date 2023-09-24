CREATE TABLE recipe(id SERIAL PRIMARY KEY, category_id INTEGER REFERENCES category, name TEXT, content TEXT);

CREATE TABLE category(id SERIAL PRIMARY KEY,name TEXT);

