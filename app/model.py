from . import db
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import backref
#from sqlalchemy import ForeignKey
from sqlalchemy import event


class EmployeeProfile(db.Model):
  __tablename__ = 'employee_profiles'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80))
  last_name = db.Column(db.String(80))
  age = db.Column(db.Integer)
  gender = db.Column(db.String(80))
  username = db.Column(db.String(80), unique=True)
  password = db.Column(db.String(255))

  def __init__(self, first_name, last_name, age, gender, username, password):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.gender = gender
    self.username = username
    self.password = generate_password_hash(password, method='pbkdf2:sha256')

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    try:
      return unicode(self.id)
    except NameError:
      return str(self.id)

  def __repr__(self):
    return '<Employee %r>' % (self.id)
  
@event.listens_for(EmployeeProfile.__table__, 'after_create')
def create_admin(*args, **kwargs):
  employee = EmployeeProfile('Admin', 'User', 20, 'Female', 'adminuser', 'adminadmin')
  db.session.add(employee)
  db.session.commit()

class CustomerProfile(db.Model):

  __tablename__ = 'customer_profiles'
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80))
  last_name = db.Column(db.String(80))
  phone_number = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(255), unique=True)
  hair_type = db.Column(db.String(80))
  date_added = db.Column(db.DateTime)

  def __init__(self, first_name, last_name, phone_number, email, hair_type, date_added):
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email
    self.hair_type = hair_type
    self.date_added = date_added

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    try:
      return unicode(self.id)
    except NameError:
      return str(self.id)

  def __repr__(self):
    return '<Customer %r>' % (self.id)

class AppointmentProfile(db.Model):
  __tablename__ = 'appointment_schedule'
  id = db.Column(db.Integer, primary_key=True)
  customer_id = db.Column(db.Integer, db.ForeignKey('customer_profiles.id'))
  employee_id = db.Column(db.Integer, db.ForeignKey('employee_profiles.id'))
  customer_profiles = db.relationship("CustomerProfile", backref=backref('customer_profiles', uselist=False))
  title = db.Column(db.String(255))
  status = db.Column(db.String(80))
  start_date = db.Column(db.DateTime)
  start_time = db.Column(db.String(80))
  end_time = db.Column(db.String(80))

  def __init__(self, customer_id, employee_id, title, status, start_date, start_time, end_time):
    self.customer_id = customer_id
    self.employee_id = employee_id
    self.title = title
    self.status = status
    self.start_date = start_date
    self.start_time = start_time
    self.end_time = end_time

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    try:
      return unicode(self.id)
    except NameError:
      return str(self.id)

  def __repr__(self):
    return '<Appointment %r>' % (self.title)