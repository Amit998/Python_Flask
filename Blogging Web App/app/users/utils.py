import os
import secrets
from PIL import Image
from flask_mail import Message
from flask import url_for
from app import mail

from flask import current_app



def save_picture(form_picture,current_profile_image):
    print(form_picture,current_profile_image)
    random_hex=secrets.token_hex(8)
    f_name,f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+f_ext
    picture_path=os.path.join(current_app.root_path,'static/image/Profile_Default/',picture_fn)

    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    print(current_profile_image,'current image name')
    
    if (os.path.exists(f"app/static/image/Profile_Default/{current_profile_image}")):
        if ( current_profile_image != "default.jpg"  ):
            os.remove(f"app/static/image/Profile_Default/{current_profile_image}")
        else:
            return picture_fn


def send_rest_email(user):
    token=user.get_reset_token()
    msg=Message('Password Reset Request',
    sender='noreply@demo.com',
    recipients=[user.email])
    msg.body=f'''
            To Reset Your Password,Visit The Following Link:
            {url_for('reset_token',token=token,_external=True)}

            If You do not Make This Request Then Simply Ignore This Email and no change 
    
    '''
    print('sending mail',msg)
    mail.send(msg)