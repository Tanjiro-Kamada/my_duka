*INTRODUCTION TO FLASK*

---> Create a new project called myduka
---> In this project create 2 files:
   1. database.py
   2. main.py

---> Open up a new terminal and run the following commands:
   1.  pip install flask
   2.  pip install psycopg2-binary


create database myduka_db;
\c myduka_db

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    buying_price NUMERIC(20, 2) NOT NULL CHECK (buying_price >= 0),
    selling_price NUMERIC(20, 2) NOT NULL CHECK (selling_price >= 0)
);
CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);


*Psycopg2*
-> A database adapter used to connect a Postgres database to Python 
-> To establish this connection we first import psycopg2 then use psycopg2.connect() function which takes some arguments


*psycopg2.connect()* -> a function meant to establish a connection to the database ---> It takes some arguments:

1. host -> the server in which my database is located /hosted ----> localhost (locally running on my computer)
2. port -> where on my pc is the Postgres service running. ---> 5432
3. user  - username of the postgres user ---> 'postgres'
4. password - password attached to that postgres user ---> 'your own password'
5. dbname - the name of the database you want to connect to ---> 'myduka_db'


*ip addresses and domain names*