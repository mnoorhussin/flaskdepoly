from unicodedata import name
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from collections import Counter
from .models import Product
from .models import Employer
from .models import User
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


@views.route('/products')
@login_required
def products():
    products = Product.query.all()
    return render_template("products.html", products=products, user=current_user)



@views.route('/dashboard')
@login_required
def dashboard():
    employers = User.query.all()
    return render_template("dashboard.html", User=User, user=current_user)





