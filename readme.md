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

OOP ---> Object Oriented Programming

---> Python has 2 categories of data types: 1.Inbuilt / Primitve data types --> int, str, bool, list, tuple, dict -->come with the programming language 2.User defined data types ---> custom data types created by the developer using classes and objects

OOP ---> a concept / paradigm in programming whereby programs are built around classes and objects

class ---> a template / blueprint for creating objects ---e.g class Person ---> name , age , id no, email,address, nationality class Laptop --->ram , rom, processor, I/O , BIOS object -> an instance of a class ---> Kim, 23

Objects and classes have an IS A relationship

--> Every class is defined by the following 3 things: 1.Identity ---> unique name of the class 2.State ---> represented by attributes --> what does a class have? attribute --> a variable in a class 3.Behaviour ---> represented by methods ---<> what can a class do? --->method ---> a function inside a class

class Person 1.Identity ---> Person 2.State ----> name, age, id no , is_student,email 3.Behaviour --> sleep, read, eat , work , travel, drive

class Horse class Teacher

OOP object class attribute methods inheritance self encapsulation abstraction polymorphism ---> method overloading

INTRODUCTION TO FLASK framework vs library

Approach 1 ---> framework Approach 2 ---> library

framework ---> collection prebuilt tools and code meant to help developers build applications easily without having to build from scratch but it requires them to follow very strict guidelines set by the framework

Examples of frameworks:

Python -> Flask, FastAPI, Django
JS --> React , Angular , Vue , Svelte
PHP --> Laravel
Java ---> Spring
Go ---> Gin, Chi
C# ---> .NET
Ruby ---> Ruby on Rails
Rust --> Tokio
Routing in Flask ---> Routing : a mechanism that maps / connects URLs to functions ---> It is a system for resource navigation ---> Routing in flask is enabled by a function called decorator function

URL ---> The full address used to access an application or a resource e.g. https://meet.google.com/meet/dsh-idtb-oqb parts of a url

Scheme / Protocol ---> http or https
Domain name ---> meet.google.com
Path --> specific resource to be accessed when using an application e.g /dsh-idtb-oqb
Port ---> :5432, :5500 , :3000, decorator function --> A function that determines or modifies the behaviour of another function ---> In Python , they are usually preceded with the prefix '@' ---> Our decorator function for routing is called @app.route() which can take 2 arguments:
Path
Methods
view function ---> a function meant to return data / response to a user

@app.route('/'). ---> decorator function def home(): ----> view function return "Hello World". ---> data to be returned

@app.route('/products') def products(): return "Products Page"

@app.route('/sales) def sales(): return "Sales page"

app.run() ---> starts a minimal server to run your application

www.jumia.com/sales ---> @app.route()

name index route ---> default route for a landing page ---> /

https://www.safaricom.co.ke/

task ---> create the following routes : /stock ,/dashboaard, /register , /login

returning full html pages
N/B: Every view function in a route must have a unique name

returning full html pages --> Instead of rendering a single piece of data , we should instead return full html pages and then render as much content as we want in those html pages ---> To do this we need to have our project structure as follows:

static :contains all static files to be rendered with flask e.g. css, js, images , videos, icons, favicons templates : contains all html files to be rendered with Flask --> index.html --> products.html --> sales.html --> stock.html --> dashboard.html --> register.html --> login.html

database.py main.py

---> To render html files in Flask we use a function imported from flask called render_template() template --> a single html file