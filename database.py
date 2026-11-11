import psycopg2

conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='891023',dbname='myduka_db')


cur = conn.cursor()



# cur.execute("select * from products")
# products_data = cur.fetchall()
# print(products_data)

def get_products():
    cur.execute("select * from products")
    products_data = cur.fetchall()
    return products_data

products_data = get_products()
print(products_data)

# def insert_products():
#     cur.execute("insert into products(name,buying_price,selling_price) values('lenovo laptop',21000,30500)")
#     conn.commit()

# insert_products()
# products_data = get_products()
# print(products_data)

def get_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data

sales_data = get_sales()
print(sales_data)

def insert_sales():
    cur.execute("insert into sales(pid,quantity) values(1,5)")
    cur.execute("insert into sales(pid,quantity) values(2,12)")
    cur.execute("insert into sales(pid,quantity) values(2,19)")
    conn.commit()

insert_sales()
sales_data = get_sales()
print(sales_data)

def get_sales_per_product():
 cur.execute(
    """
        select products.name as p_name,sum(products.selling_price * sales.quantity) as total_sales
        from sales join products on products.id = sales.pid group by p_name;
    """)
 sales_per_product = cur.fetchall()
 return sales_per_product


sales_per_product = get_sales_per_product()
print(sales_per_product)

def fetch_stock():
    cur.execute("select * from products;")
    stock = cur.fetchall()
    return stock

def insert_stock(name, buying_price, selling_price,quantity):
    cur.execute(
        """
        insert into products (name, buying_price, selling_price)
        values (%s, %s, %s);
        """,
        (name, buying_price, selling_price),
    )
    conn.commit()

def get_sales_per_day():
    cur.execute(
        """
        select date(sales.created_at) as day,
               sum(products.selling_price * sales.quantity) as total_sales
        from sales join products on products.id = sales.pid
        group by day
        order by day;
        """
    )
    sales_per_day = cur.fetchall()
    return sales_per_day

def get_profit_per_product():
    cur.execute(
        """
        select products.name as p_name,
               sum((products.selling_price - products.buying_price) * sales.quantity) as profit
        from sales join products on products.id = sales.pid
        group by p_name;
        """
    )
    profit_per_product = cur.fetchall()
    return profit_per_product

def get_profit_per_day():
    cur.execute(
        """
        select date(sales.created_at) as day,
               sum((products.selling_price - products.buying_price) * sales.quantity) as profit
        from sales join products on products.id = sales.pid
        group by day
        order by day;
        """
    )
    profit_per_day = cur.fetchall()
    return profit_per_day
 
 
insert_stock("Sugar 1kg", 150, 180, 50)
 
print(fetch_stock())
print(get_sales_per_day())
print(get_profit_per_product())
print(get_profit_per_day())