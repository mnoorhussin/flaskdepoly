from socketserver import DatagramRequestHandler
from unicodedata import name
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from collections import Counter
from .models import Product, Employer, User
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
        user_id = request.form.get("current_user.first_name")


        if len(product_name) < 1:
            flash('Product Name is too short!', category='error')
        else:
            new_product = Product(product_name = product_name, description = description, date=date,price=price, qty=qty, user_id=current_user.first_name)
            db.session.add(new_product)
            db.session.commit()
            flash('Product added!', category='success')

    return render_template("home.html", user=current_user)



@views.route('/delete/<int:id>')
@login_required
def delete_product(id):
    product_to_delete = Product.query.get_or_404(id)
    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        flash("Product deleted successfully")
        return redirect('/')
    except:
        return" There was problem deleting your product!"   
    else:
        return render_template("home.html", product_to_delete=product_to_delete, user=current_user)  






@views.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    editproduct = Product.query.get_or_404(id)
    if request.method == 'POST':
        editproduct.product_name = request.form['product_name'] 
        editproduct.qty = request.form['qty']
        editproduct.price = request.form['price']
        try:
            db.session.commit()
            flash("Product updated successfully")
            return redirect('/')
        except:
            return" There was problem updating your product!"        

    else:
        return render_template("update.html", editproduct=editproduct, user=current_user)
    
    
@views.route('/delete-user/<int:id>')
@login_required
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("User deleted successfully")
        return redirect('/profile')
    except:
        return" There was problem deleting User!"   
    else:
        return render_template("profile.html", user_to_delete=user_to_delete, user=current_user)  



@views.route('/update-user/<int:id>', methods=['GET', 'POST'])
@login_required
def update_user(id):
    edituser = User.query.get_or_404(id)
    if request.method == 'POST':
        edituser.first_name = request.form['first_name'] 
        edituser.last_name = request.form['last_name']
        edituser.email = request.form['email']
        edituser.role = request.form['role']

        try:
            db.session.commit()
            flash("User updated successfully")
            return redirect('/profile')
        except:
            return" There was problem updating User!"        

    else:
        return render_template("update-user.html", edituser=edituser, user=current_user)   


   
@views.route('/products')
@login_required
def products():
    products = Product.query.all()
    return render_template("products.html", products=products, user=current_user)



@views.route('/profile')
@login_required
def profile():
    profile = User.query.all()
    return render_template("profile.html", User=User, user=current_user)


@views.route('/employee')
@login_required
def employee():
    employee = User.query.all()
    return render_template("employee.html", employee=employee, user=current_user)