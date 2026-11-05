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

IP ADDRESS --> A number that uniquely identifies a device on a network --> two types : ipv4 and ipv6 ipv4 example --> 202.181.101.100 domain name -> a human friendly name for an ip address e.g. https://www.google.com

Internet --> global interconnection of devices world wide www --> a service that lets you connect to the internet via a browser

http -> hypertext transafer protocol -> standard communication protocol for the browser -> sends data as raw text

https -> hypertext transafer protocol secure -> same as http but now data is encrypted -> switch from http to https using an ssl / tls certificate

plan ---> develop ---> test ---> deploy apps(cloud)

ipv4 --> 2^32 https://meet.google.com/meet/dsh-idtb-oqb

person A -------> 10000 ------> Netflix

person A ------> 10000-> encrypted --> s00dj99eh89de993hd89sjhds99sh ---> Netflix ---> decrypt back to 10000

127.0.0.1 ---> ip address of your local device localhost ---> domain name for 127.0.0.1

How to perform db operations with psycopg2 cur -> an object that is used to perfom db operations(select, insert, update , delete) cur.execute() -> a function / method for executing sql queries cur.fetchall() ---> retrieves or fetches data from Postgres to Python

---> data fetched from cur.fetchall() is retrieved as a list of tuples

list ---> entire dataset tuple ---> a single row of data

(1, 'milk', Decimal('50.00'), Decimal('60.00'))

conn.commit() ---> save my data / changes in the database

task ---> insert 2 sales data using psycopg2 ---> fetch that sales data and display it on your terminal w/psycopg2

--> making insert functions reusable : let it take parameters

let the insert functions take a single param of a tuple -> the tuple then contains prod details / sale details

%s -> placeholder for a column --> the no of placeholders must match the no of columns specified

fetching complex data --> fetching data from more than one table

sales per product --> selling_price(products) --> quantity (sales) --> name(products) selling_price * quantity per product name

select products.name as p_name,sum(products.selling_price * sales.quantity) as total_sales from sales join products on products.id = sales.pid group by p_name;

multiline strings ---> allow us to write strings that traverse more than one line ---> they use tripple opening and closing quotes(single or double) """ """ or ''' '''

Task 1.write a function to fetch stock data with psycopg2 2.write a function that can insert any stock data using parameters with psycopg2 3.write functions that use psycopg2 to get the following data: -> sales per day -> profit per product -> profit per day