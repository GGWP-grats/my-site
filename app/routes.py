
from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from app import app, db

from app import forms

from app.models import User, Message

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Iblog')

@app.route('/adm', methods=['GET', 'POST'])
def login_adm():
    if current_user.is_authenticated:
        return redirect('/')
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return(render_template('login_page.html', title='Login', form=form, error="Wrong pass or Username"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return(render_template('login_page.html', title='Login', form=form))

@app.route('/regadm', methods=['GET', 'POST'])
def register_adm():
    if current_user.is_authenticated:
        return redirect('/')
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/adm')
    return render_template('registration.html', form=form, title='say something')

@app.route('/contact', methods=['GET', 'POST'])
def contact_view():
    form = forms.ContactForm()
    if form.validate_on_submit():
        message = Message(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(message)
        db.session.commit()
        return redirect('/')
    return  render_template('contact_me.html', title='contact me', form=form)


@app.route('/messages')
@login_required
def messages_view():
    messages = Message.query.all()
    return render_template('messages.html', messages=messages)

