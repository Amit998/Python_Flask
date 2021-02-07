import os
import secrets
from PIL import Image

from flask import render_template,url_for,flash,redirect,request,abort
from flask_login.utils import login_required
from wtforms import form
from app.forms import RegistrationForm,LoginForm,UpdateAccountForm,PostForm
from app.models import User,Post
from app import app,db,bcrypt
from flask_login import login_user,current_user,logout_user
# user_1=User(usename='Amit Dutta',email='damitlucky998@gmail.com',password='password')





@app.route('/')
@app.route('/home')
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
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

    print(current_profile_image,'current image name')
    
    if (os.path.exists(f"app/static/image/Profile_Default/{current_profile_image}")):
        if ( current_profile_image != "default.jpg"  ):
            os.remove(f"app/static/image/Profile_Default/{current_profile_image}")
        else:
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


@app.route('/post/new',methods=['GET','POST'])
@login_required
def new_post():
    print('new_post')
    form=PostForm()
    if (form.validate_on_submit()):
        # print('clicked')
        post=Post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your Post Has been created!','success')
        return redirect(url_for('home'))
    return render_template('create_post.html',title='Account',form=form)

@app.route('/post/<int:post_id>',methods=['GET','POST'])
def post(post_id):
    # print(post_id)
    post=Post.query.get_or_404(post_id)
    print(post,'this is post')
    return render_template('post.html',title=post.title,post=post,legend='New Post')

@app.route('/update_post/<int:post_id>/update_post',methods=['GET','POST'])
@login_required
def update_post(post_id):
    # print(post_id)
    post=Post.query.get_or_404(post_id)
    print(post,'this is post')
    if (post.author != current_user  ):
        abort(403)
    form=PostForm()
    if (form.validate_on_submit()):
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()
        flash("your post has been updated!",'success')
        return redirect(url_for('post',post_id=post.id))
    elif (request.method == 'GET'):
        form.title.data=post.title
        form.content.data=post.content
    return render_template('create_post.html',title='Update Post',form=form,legend='Update Post')



@app.route('/post/<int:post_id>/delete',methods=['GET','POST'])
def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    print(post,'this is post')
    if (post.author != current_user  ):
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Post Has Been deleted succesfully','success')

    return redirect(url_for('home'))



@app.route('/user/<string:username>')
def user_posts(username):
    page=request.args.get('page',1,type=int)
    user=User.query.filter_by(username=username).first_or_404()

    posts=Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page,per_page=5)
    return render_template("user_post.html",posts=posts,user=user)

