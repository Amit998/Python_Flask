from flask import Flask,redirect,url_for,render_template,request,session,flash
from  datetime import timedelta

app=Flask(__name__)
app.secret_key="hello"
app.permanent_session_lifetime=timedelta(seconds=20)



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login',methods=["POST","GET"])
def login():
    if (request.method == "POST"):
        session.permanent=True
        user=request.form["nm"]
        session['user']=user
        # print(session)
        flash("Login Succesfully")
        return redirect(url_for("user"))
    elif("user" in session):
        flash("Already Logged in")
        return redirect(url_for("user"))

    return render_template("login.html")

@app.route('/user')
def user():
    if "user" in session:
        user=session["user"]
        print(user)
        return render_template("user.html",user=user)
    else:
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    if "user" in session:
        user=session["user"]
        flash(f"You Have Been Logged out {user} ","info")
    session.pop("user",None)
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)