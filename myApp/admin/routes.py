from flask import render_template, Blueprint, flash, redirect, url_for
from myApp.users.forms import LoginForm
from myApp.models import User, Post


admin = Blueprint('admin', __name__)

@admin.route('/admin', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == 'haider@admin.com' and password == '17352015':
            flash("Admin is correct", 'success')
            users = User.query.all()
            data = dict()
            for user in users:
                post = len(list(Post.query.filter_by(author=user)))
                key = user.username
                temp_dict = dict()
                temp_dict['user'] = user
                temp_dict['post'] = post
                data[key] = temp_dict
                print(data)
            return render_template('admin_panel.html', title='Amin Panel', users=users, admin=True)
        else:
            flash("Admin is not correct", 'info')
    return render_template('login.html', title='Admin Panel', form=form, admin=True)
