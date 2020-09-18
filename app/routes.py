
from flask import render_template, flash, redirect
from flask_login import current_user, login_user, login_required

from app import app, db

from app.forms import LoginForm, ContactForm

from app.models import User, Message

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Iblog')

@app.route('/adm', methods=['GET', 'POST'])
def login_adm():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return(render_template('login_page.html', title='Login', form=form, error="Wrong pass or Username"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse (next_page).netloc != '':
            next_page = url_for('index')
        return redirect('/')
    return(render_template('login_page.html', title='Login', form=form))

@app.route('/db_content')
@login_required
def show_db():
    return render_template("db_content.html", title='Database')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/cantactme', methods=['GET', 'POST'])
def contact_view():
    form = ContactForm()
    if form.validate_on_submit():
        message = Message(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(message)
        db.session.commit()
        return redirect('/')
    return  render_template('contact_me.html', title='contact me', form=form)

@app.route('/messages')
def messages_view():
    return render_template('messages.html')

