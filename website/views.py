from unicodedata import name
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Product
from .models import Employer
from .import db
import json





views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        product_name = request.form.get("product_name")
        description = request.form.get("description")
        date = request.form.get("date")
        qty = request.form.get("qty")
        price = request.form.get("price")

        if len(product_name) < 1:
            flash('Product Name is too short!', category='error')
        else:
            new_product = Product(product_name = product_name, description = description, date=date,price=price, qty=qty, user_id=current_user.id)
            db.session.add(new_product)
            db.session.commit()
            flash('Product added!', category='success')

    return render_template("home.html", user=current_user)


    
        

@views.route('/delete-product', methods=['POST'])
def delete_product():
    product = json.loads(request.data)
    productId = product['productId']
    product = Product.query.get(productId)
    if product:
        if product.user_id == current_user.id:
            db.session.delete(product)
            db.session.commit()
            flash('Product deleted!', category='success')

    return jsonify({})



@views.route('/employers', methods=['GET', 'POST'])
@login_required
def employers():
    if request.method == 'POST':
        employer_firstname = request.form.get("employer_firstname")
        employer_lastname = request.form.get("employer_lastname")
        if len(employer_firstname) < 1:
            flash('Employer Name is too short!', category='error')
        else:
            new_employer = Employer(employer_firstname = employer_firstname, employer_lastname = employer_lastname, user_id=current_user.id)
            db.session.add(new_employer)
            db.session.commit()
            flash('Employer added!', category='success')

    return render_template("employers.html", user=current_user)





@views.route('/products')
def products():
    products = Product.query.all()
    return render_template("products.html", products=products, user=current_user)



@views.route('/employers')
def show_employers():
    employers = Employer.query.all()
    return render_template("employers.html", employers=employers, user=current_user)