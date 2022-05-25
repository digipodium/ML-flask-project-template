from email.policy import default
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from validators import card_number
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


db = SQLAlchemy()

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.now)

    def password(self,password):
        self.password= generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



    def __str__(self) -> str:
        return self.username


class CollegeAdmin(db.Model):
    __tablename__ ="collegeadmin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    college = db.Column(db.String)
    designation = db.Column(db.String)
    password = db.Column(db.String)
    cpassword = db.Column(db.String)
    email = db.Column(db.String)
    mobile = db.Column(db.String)

def __str__(self) -> str:
        return self.username



class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String)
    address = db.Column(db.String)
    image_1 = db.Column(db.String)
    image_2 = db.Column(db.String)
    image_3 = db.Column(db.String)
    image_4 = db.Column(db.String)
    price = db.Column(db.Integer)
    isbooked =db.Column(db.Boolean)
    admin = db.Column(db.Integer, db.ForeignKey('admin.id'))

    def __str__(self) -> str:
            return self.username

     

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventname = db. Column(db.String)
    description = db.Column(db.String)
    created_on = db.Column(db.DateTime,default=datetime.now)
    created_on = db.Column(db.DateTime,default=datetime.now)
    venue = db.Column(db.Integer, db.ForeignKey('admin.id'))
    isconfirmed =db.Column(db.Boolean)
    college_admin = db.Column(db.Integer, db.ForeignKey('collegeadmin.id'))
        
    def __str__(self) -> str:
            return self.eventname


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.Integer, db.ForeignKey('collegeadmin.id'))
    college_admin = db.Column(db.Integer, db.ForeignKey('collegeadmin.id'))
    college=db.Column(db.String,nullable=False)
    name=db.Column(db.String,nullable=False)
    venue=db.Column(db.String,nullable=False)
    duration=db.Column(db.Integer,nullable=False)
   
    def __str__(self) -> str:
            return self.id

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking = db.Column(db.Integer, db.ForeignKey('collegeadmin.id'))
    college_admin = db.Column(db.Integer, db.ForeignKey('collegeadmin.id'))
    amount=db.Column(db.Integer,nullable=False) 
    venue = db.Column(db.Integer, db.ForeignKey('collegeadmin.id'))
    createdon = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    cardNumber= db.Column(db.Integer, nullable=False)
    cvv= db.Column(db.Integer, nullable=False)
  

    def __str__(self) -> str:
            return self.id


    