import os
import secrets
from PIL import Image

from flask import render_template,url_for,flash,redirect,request
from flask_login.utils import login_required
from app.forms import RegistrationForm,LoginForm,UpdateAccountForm
from app.models import User,Post
from app import app,db,bcrypt
from flask_login import login_user,current_user,logout_user
# user_1=User(usename='Amit Dutta',email='damitlucky998@gmail.com',password='password')


posts=[
    {
        'author':'Amit Dutta',
        "title":"Blog Post 1",
        "content":"First Post Content",
        'Date_posted':'April 20,2018'
    },
    {
        'author':'Amit Dutta',
        "title":"Blog Post 1",
        "content":"First Post Content",
        'Date_posted':'April 20,2018'
    }


]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",posts=posts)


@app.route('/about')
def about():
    return render_template("about.html",title="About")


@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))


    form=RegistrationForm()
    if(form.validate_on_submit()):
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your Account hasbeen created','success')


        # flash(f'Account  created for {form.username.data} !','success')
        return redirect(url_for('login'))
        # return redirect(url_for('home'))
    return render_template('register.html',title='Login',form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form=LoginForm()
    if(form.validate_on_submit()):
        user=User.query.filter_by(email=form.email.data).first()
        if (user and bcrypt.check_password_hash(user.password,form.password.data)):
            login_user(user,remember=form.remember.data) 
            next_page=request.args.get('next')
            print(next_page)
    
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'login unsuccessfull please check email and password','danger')

    return render_template('login.html',title='Login',form=form)
 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))

def save_picture(form_picture,current_profile_image):
    print(form_picture,current_profile_image)
    random_hex=secrets.token_hex(8)
    f_name,f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+f_ext
    picture_path=os.path.join(app.root_path,'static/image/Profile_Default/',picture_fn)

    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    if (os.path.exists(f"app/static/image/Profile_Default/{current_profile_image}")):
        os.remove(f"app/static/image/Profile_Default/{current_profile_image}")
        
   
        return picture_fn


@app.route('/account',methods=['GET','POST'])
@login_required
def account():
    # print('in account')
    form=UpdateAccountForm()
    # print(current_user.image_file,'this is the name')
    if(form.validate_on_submit()):
        # print(form.picture.data)
        if(form.picture.data ):
            current_profile_image=current_user.image_file
            picture_file=save_picture(form.picture.data,current_profile_image)
            current_user.image_file=picture_file

        # print('in account')
        current_user.username=form.username.data
        current_user.email=form.email.data
        print(current_user.username,form.username.data)
        db.session.commit()
        flash(f'Your Account has been updated','success')
        return redirect(url_for('account'))
    elif(request.method == 'GET'):
        form.username.data=current_user.username
        form.email.data=current_user.email
    image_file=url_for('static',filename='image/Profile_Default/'+current_user.image_file)
    return render_template("account.html",title='Account',image_file=image_file,form=form)


