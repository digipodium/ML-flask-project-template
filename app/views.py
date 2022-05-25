

from inspect import formatargvalues
import logging

from flask import render_template,redirect,request,flash,session,url_for
import flask
from . import app
from .models import *







@app.route('/', methods=('GET', 'POST'))
def index():    
    return render_template('index.html',)

@app.route('/event/create', methods=["GET","POST"])
def event_create():

    return render_template('event_create_form.html',)
           
@app.route('/venues/create',methods=["GET","POST"])
def venue_create():
    if request.method=="POST":
        
        title=request.form.get("title")
        address=request.form.get("address")
        image_1=request.form.get("image_1")
        image_2=request.form.get("image_2")
        image_3=request.form.get("image_3")
        image_4=request.form.get("image_4")
        price=request.form.get("price")
        try:
            item= Venue(title=title,address=address,image_4=image_4,image_3=image_3,image_2=image_2,image_1=image_1,price=price)
            db.session.add(item)
            db.session.commit()
            db.session.close()
            return redirect(url_for('venue_create'))
    
        except Exception as e:
            return redirect(url_for('venue_create'))

    else:    
        return render_template('venue_create_form.html')
 
@app.route('/booking/create',methods=["GET","POST"])
def booking_create():
    if request.method=="POST":
        college=request.form.get("college")
        name=request.form.get("name")
        venue=request.form.get("venue")
        duration=request.form.get("duration")
        try:
            item= Booking(college=college,name=name,duration=duration,venue=venue)
            db.session.add(item)
            db.session.commit()
            db.session.close()
            return redirect(url_for('payment'))
        except Exception as e:
            print(e) 
    else:    
        return render_template('booking_create_form.html')

@app.route('/payment',methods=["GET","POST"])
def payment():
    if request.method=="POST":
      amount=request.form.get("amount")
      cardNumber=request.form.get('cardNumber')
      cvv =request.form.get('cvv')
      try:
            item=Payment(amount=amount,cardNumber=cardNumber)
            item.set_password(cvv)
            db.session.add(item)
            db.session.commit()
            return redirect(url_for('transactionp'))
      except:
            return "There was error"

    else:
        return render_template('payment_create_form.html')   

@app.route('/login')
def login():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = CollegeAdmin.query.filter_by(username=username).first()
            if user is None or not user.check_password(password):
                flash('Invalid username or password','danger')
                return redirect(url_for('login'))
            Admin(user, remember=True)
            return redirect(url_for('index'))
    return render_template('login_create_form.html')

@app.route('/signup', methods=["GET","POST"])
def signup():
    if request.method=='POST':
        email = request.form.get('email')
        username = request.form.get('username')
        cpassword = request.form.get('cpassword')
        password = request.form.get('password')
        # print(cpassword, password, cpassword==password)
        if username and password and cpassword and email:
            if cpassword != password:
                flash('Password do not match','danger')
                return redirect('signup_create_form.html')
        else:
            if CollegeAdmin.query.filter_by(email=email).first() is not None:
                flash('Please use a different email address','danger')
                return redirect('signup_create_form.html')
            elif CollegeAdmin.query.filter_by(username=username).first() is not None:
                flash('Please use a different username','danger')
                return redirect('signup_create_form.html')
            else:
                user = CollegeAdmin(username=username, email=email)
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                flash('Congratulations, you are now a registered user!','success')
                return redirect(url_for('index'))
    return render_template('signup_create_form.html')

@app.route('/forgot',methods=['GET', 'POST'])
def forgot():
    if request.method=='POST':
        email = request.form.get('email')
        if email:
            pass
    return render_template('forgot.html', title='Password reset page')


        