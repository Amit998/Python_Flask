from flask import render_template,url_for,flash,redirect
from app.forms import RegistrationForm,LoginForm
from app.models import User,Post
from app import app
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
    form=RegistrationForm()
    if(form.validate_on_submit()):
        flash(f'Account  created for {form.username.data} !','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Login',form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if(form.validate_on_submit()):
        if (form.email.data ==  "damitlucky998@gmail.com" and form.password.data =="damitlucky998@gmail.com"):
            flash(f'Welcome back Amit!','success')
            return redirect(url_for('home'))
        else:
            flash(f'login unsuccessfull please check username and password','danger')
    return render_template('login.html',title='Login',form=form)
 
