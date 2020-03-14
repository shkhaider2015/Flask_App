from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f6cd85d264d6ceb0ad9a11d7be35a930'

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