from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm



app=Flask(__name__)

app.config['SECRET_KEY']='c04921879357e963347c30054535420e'


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