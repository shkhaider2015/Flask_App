from flask import Flask, render_template, url_for

app = Flask(__name__)

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
