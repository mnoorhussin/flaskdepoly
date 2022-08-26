from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")



@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")


@auth.route('/products')
def products():
    return render_template("products.html")


@auth.route('/developers')
def developers():
    return render_template("developers.html")

@auth.route('/notes')
def notes():
    return render_template("notes.html")


    
