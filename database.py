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

def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price) values('lenovo laptop',21000,30500)")
    conn.commit()

insert_products()
products_data = get_products()
print(products_data)