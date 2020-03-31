import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from myApp import app, mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    
    # Resize image
    output_size = (124, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    
    # save image
    i.save(picture_path)
        
    return picture_fn


def send_reset_email(user): 
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
        sender='noreply@demo.com',
        recipients=[user.email])
    
    msg.body = f''' to reset your password, visit the following link
    {url_for('reset_token', token=token, _external=True)}
    if you did not make this request then simply ignore this email

    '''
    mail.send(msg)