from flask import Flask, render_template
__author__ = 'boomatang'

app = Flask(__name__)


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


# error pages
@app.errorhandler(404)
def fail404(e):
    return render_template("errors/404.html")


@app.errorhandler(405)
def fail404(e):
    return render_template("errors/405.html")



if __name__ == '__main__':
    app.run(debug=True, port=7000)
