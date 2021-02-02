from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Email, Length,EqualTo


class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=4,max=200)])
    email=StringField('Email',validators=[DataRequired(),Email(),Length(min=4,max=40)])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=4,max=40)])
    confirm_password=PasswordField( 'Confirm Password',validators=[DataRequired(),EqualTo('password'),Length(min=4,max=20)])
    submit=SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email(),Length(min=4,max=40)])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8,max=40)])
    remember=BooleanField('Remem ber Me')
    submit=SubmitField('Sign Up')
