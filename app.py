import random
from flask import Flask, render_template, request, flash, url_for, session
import time
from werkzeug.utils import redirect
from forms_basics import *
from sql_statments import *
from passlib.hash import sha256_crypt

__author__ = 'boomatang'
__version__ = '1'

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmjydtriytdsdN]LWX/,?RT'

@app.route("/logout/")
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
            is_new = check_new_user_email(form_values['email'])

            if is_new:
                create_user_account(form_values)
                flash("Thank you, " + form_values['first_name'] + " for joining our family.")
                return redirect(url_for('index'))
            else:
                flash("It seems that email is already used.")
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
