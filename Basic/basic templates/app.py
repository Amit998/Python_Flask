from flask import Flask,redirect,url_for,render_template

app=Flask(__name__)

a=True

# @app.route('/')
# def hello_world():
#     return 'Hello World'


@app.route('/<name>')
def home(name):
    return render_template("index.html",content=name,r=2,list=['test1','test2','test3'])


@app.route('/test')
def test():
    return render_template("new.html")
# def home():
#     return "Hello I AM <h1>AMIT DUTTA</h1>"

# @app.route('/<name>')
# def user(name):
#     return f"Hello {name}"


# @app.route('/admin')
# def admin():
#     if (a != False):
#         return redirect(url_for("user",name="amit"))


if __name__=="__main__":
    app.run(debug=True)