from flask_wtf import FlaskForm

from flask_wtf.file import FileField,FileAllowed

from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Email, Length,EqualTo, ValidationError
from app.models import User,Post
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=4,max=200)])
    email=StringField('Email',validators=[DataRequired(),Email(),Length(min=4,max=60)])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=4,max=60)])
    confirm_password=PasswordField( 'Confirm Password',validators=[DataRequired(),EqualTo('password'),Length(min=4,max=60)])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if (user):
            raise ValidationError('That Username is already taken,please select diffrent')

    def validate_email(self,email):
        email=User.query.filter_by(email=email.data).first()
        if (email):
            raise ValidationError('That Email is already taken, please select diffrent')



class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email(),Length(min=4,max=40)])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8,max=40)])
    remember=BooleanField('Remem ber Me')
    submit=SubmitField('Sign Up')

class UpdateAccountForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=4,max=200)])
    email=StringField('Email',validators=[DataRequired(),Email(),Length(min=4,max=60)])
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')

    def validate_username(self,username):
        if (username.data != current_user.username):
            user=User.query.filter_by(username=username.data).first()
            if (user):
                raise ValidationError('That Username is already taken,please select diffrent')

    def validate_email(self,email):
        if (email.data != current_user.email):
            email=User.query.filter_by(email=email.data).first()
            if (email):
                raise ValidationError('That Email is already taken, please select diffrent')

