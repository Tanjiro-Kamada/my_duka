from flask import Flask

#flask instance
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route('/products')
def products():
    return "Products Page"


@app.route('/sales')
def sales():
    return "Sales Pages"




# starts server to run app
app.run(debug=True)


