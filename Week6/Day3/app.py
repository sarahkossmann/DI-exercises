from flask import Flask
from flask import render_template
from login import Form
import db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def home():
    html = render_template('home.html')
    return html

@app.route('/products')
def products():
    products = db.load_database()
    product_list = render_template('products.html', products=products)
    return product_list

@app.route('/login')
def add_item():
    form = Form()
    login = render_template('login.html', form=form)
    return login

@app.route('/product_details/<int:product_id>')
def detail():
    pass



if __name__ == "__main__":
    app.run()