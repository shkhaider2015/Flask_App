from flask import render_template, url_for, flash, redirect
from myApp import app
from myApp.forms import RegistrationForm, LoginForm
from myApp.models import User, Post


posts = [
    {
        'author' : 'Shakeel haider',
        'title' : 'Blog Post 1',
        'content' : 'First post Content',
        'date_posted' : '7 April 2020'
    },
    {
        'author' : 'Dawood Khan',
        'title' : 'Blog Post 2',
        'content' : 'Second post Content',
        'date_posted' : '8 April 2020'
    }
]

##decorator
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)



@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"You have been logged in", 'success')
            return redirect(url_for('home'))
        else:
            flash("Check username and password", 'danger')
    return render_template('login.html', title='login', form=form)