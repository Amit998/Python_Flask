from flask import Flask,render_template,url_for,flash,redirect
from sqlalchemy.orm import backref
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SECRET_KEY']='c04921879357e963347c30054535420e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

# user_1=User(usename='Amit Dutta',email='damitlucky998@gmail.com',password='password')
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(60),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    content=db.Column(db.Text,nullable=False)

    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"


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
 


if __name__ == '__main__':
    app.run(debug=True)