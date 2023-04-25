from flask import Flask,render_template,redirect,url_for,request, make_response, session,abort



app = Flask(__name__)


def get_current_username():
    email = ""
    login_auth = False
    if 'email' in session:
        email = session['email']
        login_auth = True

    return email,login_auth


@app.route("/")
def home():
    email,login_auth =get_current_username()
    return render_template("index.html",email=email,login_auth=login_auth)


@app.route("/iletisim")
def contact():
    email,login_auth =get_current_username()
    return render_template("contact.html",email=email,login_auth=login_auth)


@app.route("/hakkimda")
def about():
    email,login_auth =get_current_username()
    return render_template("about.html",email=email,login_auth=login_auth)

@app.route("/giris",methods=['POST'])
def login():
    if request.method == 'POST':
        if request.form:
            if 'email' and 'password' in request.form:
                userMail = request.form['email']
                userPass = request.form['password']
                if userMail == 'admin@gmail.com' and userPass == 'admin':
                    session['email']=userMail
                    return redirect(url_for('home'))
                else:
                    return redirect(url_for('login'))
        abort(400)    
    email,login_auth =get_current_username()

    return render_template("login.html",email=email,login_auth=login_auth)