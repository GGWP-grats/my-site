from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Iblog')

@app.route('/adm', methods=['GET', 'POST'])
def login_adm():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/')
    return(render_template('login_page.html', title='Login', form=form))
