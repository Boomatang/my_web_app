from flask import Flask, render_template, request
import time
from forms_basics import *


__author__ = 'boomatang'
__version__ = '1'

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/register/', methods=['POST', 'GET'])
def register():
    form = create_user()
    if request.method == 'POST':
        form_values = {
            'first_name': form.first_name(),
            'surname': form.surname(),
            'email': form.email(),
            'password': form.password(),
            're_password': form.re_password(),
            'account_type': 32,
            'join_date': time.time()}




        # TODO: add in the sql function and the right redircts

    return render_template("users/register.html", form=form)


@app.route('/')
def index():
    # TODO add the sql function to bring in the products
    product_list = range(0, 8)
    return render_template("main.html", product_list=product_list)


@app.route('/products/')
def products():
    # TODO add the sql function to bring in the products
    product_list = range(0, 16)

    return render_template("products/products.html", product_list=product_list)


@app.route('/product_view/')
def product_view():

    return render_template('products/product_view.html')


# TODO: Set up the account page
@app.route('/account/')
def account():
    return "PAge to be made"


# error pages
@app.errorhandler(404)
def fail404(e):
    return render_template("errors/404.html")


@app.errorhandler(405)
def fail404(e):
    return render_template("errors/405.html")



if __name__ == '__main__':
    app.run(debug=True, port=7000)
