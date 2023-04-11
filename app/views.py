from datetime import date
import os
from app import app, db, login_manager
from flask import render_template, request, redirect, send_from_directory, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
#from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from app.model import EmployeeProfile, CustomerProfile, AppointmentProfile
from app.forms import LoginForm, AddEmployeeForm, AddAppointmentForm, AddCustomerForm, DeleteCustomerForm, DeleteEmployeeForm, EditEmployeeForm, EditCustomerForm


###########################################################################################################################
## Normal Routes ##
###########################################################################################################################
@app.route('/')
def home():
    events = []
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

###########################################################################################################################
## From Routes ##
###########################################################################################################################

@app.route('/add_employee', methods=['POST', 'GET'])
@login_required
def add_employee():
    form = AddEmployeeForm()

    if form.validate_on_submit() and request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        gender = form.gender.data
        username = form.username.data
        password = form.password.data

        #add to database
        employee = EmployeeProfile(request.form['first_name'], request.form['last_name'], request.form['age'], request.form['gender'], request.form['username'], request.form['password'])
        db.session.add(employee)
        db.session.commit()

        #flash and redirect
        flash('Employee was sucessfully added', 'success')
        return redirect(url_for('all_employees'))
    return render_template('addEmployee.html', form=form)

@app.route('/all_employees')
@login_required
def all_employees():
    all_employee = db.session.execute(db.select(EmployeeProfile)).scalars()
    if all_employee is not None:
        return render_template('allEmployees.html', all_employee=all_employee)
    flash('No Employee to display', 'error')
    return redirect(url_for('add_employee'))


@app.route('/add_customer', methods=['POST', 'GET'])
@login_required
def add_customer():
    form = AddCustomerForm()

    if form.validate_on_submit() and request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        email = form.email.data
        hair_type = form.hair_type.data
        date_added = date.today()

        #add to database
        customer = CustomerProfile(request.form['first_name'], request.form['last_name'], request.form['phone_number'], request.form['email'], request.form['hair_type'], date_added)
        db.session.add(customer)
        db.session.commit()

        #flash and redirect
        flash('Customer was sucessfully added', 'success')
        return redirect(url_for('all_customers'))
    return render_template('addCustomer.html', form=form)

@app.route('/all_customers')
@login_required
def all_customers():
    all_customer = db.session.execute(db.select(CustomerProfile)).scalars()
    if all_customer is not None:
        return render_template('allCustomers.html', all_customer=all_customer)
    flash('No Customer to display', 'error')
    return redirect(url_for('add_customer'))

@app.route('/add_appointment', methods=['POST', 'GET'])
@login_required
def add_appointment():
    form = AddAppointmentForm()

    form.customer_id.query = Cust
    if form.validate_on_submit and request.method == 'POST':
        id = form.id.data
        customer_id = form.customer_id.data
        title = form.ttle.data
        status = form.status.data
        start_date = form.start_date.data
        start_time = form.start_time.data
        end_time = form.end_time.data

        appointment = AppointmentProfile(request.form['customer_id'], request.form['title'], request.form['status'], request.form['start_date'],
                                         request.form['start_time'], request.form['end_time'])
        db.session.add(appointment)
        db.session.commit()

        flash('Appointment was successfully created', 'success')
        return redirect(url_for('home'))
    return render_template('addAppointment.html', form = form)

###########################################################################################################################
##Login and Logout User ##
###########################################################################################################################
@app.route('/login', methods=['POST', 'GET'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = db.session.execute(db.select(EmployeeProfile).filter_by(username=username)).scalar()
        if user is not None and check_password_hash(user.password, password):

        # Gets user id, load into session
            login_user(user)
            flash(f'User {username} has successfully logged in!!!')
            return redirect(url_for("all_customers"))
        else:
            flash(f'User {username} was not logged in !!')
            return redirect(url_for('home'))
    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are successfully logged out')
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(EmployeeProfile).filter_by(id=id)).scalar()



  ######################################################################
###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
