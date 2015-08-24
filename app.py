from functools import wraps
import random
import re
from flask import Flask, render_template, request, flash, url_for, session
import time
from werkzeug.utils import redirect
from forms_basics import *
from sql_statments import *
from passlib.hash import sha256_crypt

__author__ = 'boomatang'
__version__ = '1'

app = Flask(__name__)
# TODO: This key need to be change with new sites and moved to a safe place. Its here for testing only
app.secret_key = 'A0Zr98j/3yX R~XHH!jmjydtriytdsdN]LWX/,?RT'


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login in first..')
            return redirect(url_for('login'))

    return wrap


# ####################################

@app.route("/login/", methods=["POST", "GET"])
def login():
    form = UserLogin()

    if request.method == 'POST':
        email = thwart(request.form['email'])
        password = thwart(request.form['password'])

        if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            if not check_new_user_email(email):
                user = get_user_id(email)

                check = comfirm_password(user[0], email, password)
                password = random.random()

                if check:
                    session['username'] = user[1]
                    session['userid'] = user[0]
                    session['logged_in'] = True
                    flash("Welcome back " + session['username'] + '.')
                    return redirect(url_for('index'))

                else:
                    flash("Please check your login details")
                    return redirect(url_for('login'))
            else:
                flash("Please check your login details")
                return redirect(url_for('login'))
        else:
            flash("Please check your login details")
            return redirect(url_for('login'))

    return render_template("users/login.html", form=form)


@app.route("/logout/")
@login_required
def logout():
    name = session['username']
    session.clear()
    gc.collect()
    flash(name + " has been logged out!")
    return redirect(url_for('index'))


@app.route('/register/', methods=['POST', 'GET'])
def register():
    form = Create_User()
    if request.method == 'POST':
        form_values = {
            'first_name': thwart(request.form['first_name']),
            'surname': thwart(request.form['surname']),
            'email': thwart(request.form['email']),
            'password': sha256_crypt.encrypt(thwart(request.form['password'])),
            'account_type': int(thwart(str(32))),
            'join_date': int(thwart(str(int(time.time()))))}
        re_password = thwart(request.form['re_password'])

        if sha256_crypt.verify(re_password, form_values['password']):
            re_password = random.random()

            if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", form_values['email']):

                is_new = check_new_user_email(form_values['email'])

                if is_new:
                    create_user_account(form_values)
                    user = get_user_id(form_values['email'])
                    session['username'] = user[1]
                    session['userid'] = user[0]
                    session['logged_in'] = True

                    flash("Thank you, " + form_values['first_name'] + " for joining our family.")
                    return redirect(url_for('index'))
                else:
                    flash("It seems that email is already used.")
                    return redirect(url_for('register', form=form))
            else:
                flash("Please enter a valid email address")
                return redirect(url_for('register', form=form))
        else:
            flash("Your passwords did not match.")
            return redirect(url_for('register', form=form))

            # TODO: add in the sql function and the right redircts

    return render_template("users/register.html", form=form)


@app.route('/')
def index():
    # TODO add the sql function to bring in the products
    product_list = range(0, 8)
    return render_template("main.html", product_list=product_list)


@app.route('/products/', methods=['POST', 'GET'])
def products():
    # TODO Change to make the custom url and add to cart
    # TODO: Add function to shorten up the description so as to keep all the boxes the same size. This may mean adding in white space.
    product_list = product_full_list()

    if request.method == 'POST':
        flash("you got it right the first time")

        if request.form['action'] == 'View':
            # TODO: pass the page number in to the url
            IDprod = request.form['Product'][0]
            return redirect(url_for('product_view', ID=IDprod))

        elif request.form['action'] == 'Add to Cart':
            # TODO: Code needs to be added here after the cart pages have been set up
            flash("Item " + request.form['Product'] + " added to cart")

        else:
            render_template("products/products.html", product_list=product_list)

    return render_template("products/products.html", product_list=product_list)


@app.route('/product_view/', methods=['GET', 'POST'])
def product_view():
    # TODO: There is a lot of sql work needed here
    IDproduct = request.args.get('ID')


    return render_template('products/product_view.html')


# TODO: Set up the account page
@app.route('/account/')
def account():
    return redirect(url_for('index'))


# error pages
@app.errorhandler(404)
def fail404(e):
    return render_template("errors/404.html")


@app.errorhandler(405)
def fail404(e):
    return render_template("errors/405.html")


if __name__ == '__main__':
    app.run(debug=True, port=7000)
