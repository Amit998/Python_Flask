
from flask import render_template,url_for,flash,redirect,request,abort,Blueprint
from app.posts.form import PostForm
# Check
from app.models import Post
from app import db
from flask_login import current_user,login_required

posts=Blueprint('posts',__name__)


@posts.route('/post/new',methods=['GET','POST'])
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
        return redirect(url_for('main.home'))
    return render_template('create_post.html',title='Account',form=form)

@posts.route('/post/<int:post_id>',methods=['GET','POST'])
def post(post_id):
    # print(post_id)
    post=Post.query.get_or_404(post_id)
    print(post,'this is post')
    return render_template('post.html',title=post.title,post=post,legend='New Post')

@posts.route('/update_post/<int:post_id>/update_post',methods=['GET','POST'])
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
        return redirect(url_for('posts.post',post_id=post.id))
    elif (request.method == 'GET'):
        form.title.data=post.title
        form.content.data=post.content
    return render_template('create_post.html',title='Update Post',form=form,legend='Update Post')



@posts.route('/post/<int:post_id>/delete',methods=['GET','POST'])
def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    print(post,'this is post')
    if (post.author != current_user  ):
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Post Has Been deleted succesfully','success')

    return redirect(url_for('main.home'))






