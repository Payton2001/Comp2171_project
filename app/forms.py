from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, DateField, DateTimeField
from wtforms.validators import InputRequired
#from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms_alchemy import QuerySelectField

from app.model import CustomerProfile

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[InputRequired()])
  password = PasswordField('Password', validators=[InputRequired()])


class AddAppointmentForm(FlaskForm):
  customer_id = QuerySelectField(u'Customer ID', query_factory=lambda:CustomerProfile.query,get_label="id")
  title = StringField('Appointment Title', validators=[InputRequired()])
  status = SelectField('Appointment Status',
                       choices=[('Upcoming', 'Upcoming'),
                                ('In Progress', 'In Progress'),
                                ('Completed', 'Completed')],
                       validators=[InputRequired()])
  start_date = DateField('Appointment Start Date')
  start_time = DateTimeField('Appointment Start Time')
  end_time = DateTimeField('Appointment End Time')


class AddEmployeeForm(FlaskForm):
  first_name = StringField('Employee First Name', validators=[InputRequired()])
  last_name = StringField('Employee Last Name', validators=[InputRequired()])
  age = StringField('Employee Age', validators=[InputRequired()])
  gender = StringField('Employee Gender', validators=[InputRequired()])
  username = StringField('Username', validators=[InputRequired()])
  password = StringField('Password', validators=[InputRequired()])


class AddCustomerForm(FlaskForm):
  first_name = StringField('Customer First Name', validators=[InputRequired()])
  last_name = StringField('Customer Last Name', validators=[InputRequired()])
  phone_number = StringField('Customer Phone Number', validators=[InputRequired()])
  email = StringField('Customer Email', validators=[InputRequired()])
  hair_type = SelectField('Hair Type',
                          choices=[('Natural', 'Natural'),
                                   ('Relaxed', 'Relaxed'),
                                   ('Jerry Curled', 'Jerry Curled'),
                                   ('Bald', 'Bald')],
                          validators=[InputRequired()])
  
class DeleteCustomerForm(FlaskForm):
  id = StringField('Enter ID of Customer to Delete', validators=[InputRequired()])

class DeleteEmployeeForm(FlaskForm):
  id = StringField('Enter ID of Employee to Delete', validators=[InputRequired()])

class EditEmployeeForm(FlaskForm):
  id = StringField('Enter ID of Employee to Edit', validators=[InputRequired()])

class EditCustomerForm(FlaskForm):
  id = StringField('Enter ID of Customer to Edit', validators=[InputRequired()])
