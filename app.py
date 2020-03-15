from flask import Flask, render_template, url_for, flash, redirect
from flask-sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f6cd85d264d6ceb0ad9a11d7be35a930'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),  nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.rlationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User('{self.title}, {self.date_posted}')"


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



if __name__ == '__main__':
    app.run(debug=True)