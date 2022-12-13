# importing needed libraries
import pyotp
from flask import *
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
import random
from Crypto.Hash import SHA1

# configuring flask application
app = Flask(__name__)
mail=Mail(app)
app.config["SECRET_KEY"] = "APP_SECRET_KEY"

app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]='mangotree0867@gmail.com'
app.config['MAIL_PASSWORD']='ortnknimextqwrwa'                    #you have to give your app-password of gmail account
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
Bootstrap(app)

e_otp = "".join([str(random.randint(0,9)) for i in range(6)])

# creating empty list & reading in credentials from text file
email = []
file_in = open("emails.txt", "r")
e = file_in.readlines()
for line in e:
    email.append(line)
email = [item.strip() for item in email]
file_in.close()

# previously reading in from txt file without item.strip made its so that there was
# a "\n" at the end of each credential
pwd = []
file_in = open("pwd.txt", "r")
p = file_in.readlines()
for line in p:
    pwd.append(line)
pwd = [item.strip() for item in pwd]
file_in.close()

otpad = []
file_in = open("otp.txt", "r")
o = file_in.readlines()
for line in o:
    otpad.append(line)
otpad = [item.strip() for item in otpad]
file_in.close()

# homepage route
@app.route("/")
def index():
    return render_template("index.html")

# create account route

@app.route("/create/account/")
def create():
    return render_template("create.html")
    
# create account page route
@app.route("/create/account/" , methods=["POST"])
def create_form():
    user = request.form.get("username")
    pw = request.form.get("password")
    con_password = request.form.get("con_password")
    
    
    if user in email:
        flash("This email is already in use", "danger")
        return redirect(url_for("create"))
    
    
    else:
        if pw == con_password:
            email.append(user)

            #saves password as a hash
            pw_b = bytes(pw, "ascii")
            pw_h = SHA1.new(pw_b).hexdigest()
            pwd.append(pw_h)
            
            #sends 6-digit code to verify if the user actually has access to the email the user is writing
            cust_email = request.form.get("username")
            msg = Message(subject = "Email Verification", sender= "mangotree0867@gmail.com", recipients= [cust_email])
            msg.body="This is your verification code: " + str(e_otp)
            mail.send(msg)

            return redirect(url_for("registration_otp"))

        else:
            flash("The passwords do not match", "danger")
            return redirect(url_for("create"))
        

@app.route("/registration_otp/")
def registration_otp():
    return render_template("registration_otp.html")

@app.route("/registration_otp/", methods=["POST"])
def registration_otp_form():
    input_otp = request.form.get("e_otp")
    if(input_otp == e_otp):
        #writing credentials into textfile to be saved
        e = open("emails.txt", "w")
        for x in email:
            e.writelines("%s\n" % x)
        e.close()
    
        p = open("pwd.txt", "w")
        for y in pwd:
            p.writelines("%s\n" % y)
        p.close()
        return redirect(url_for("create_2fa"))
    
    else:
        flash("The 6-digit number does not match, Try again", "danger")
        return render_template("registration_otp.html")


# login page route
@app.route("/login/")
def login():
    return render_template("login.html")


# login form route
@app.route("/login/", methods=["POST"])
def login_form():
    
    # getting form data
    username = request.form.get("username")
    password = request.form.get("password")

    # authenticating submitted creds with demo creds
    # redirecting users to 2FA page when creds are valid
    if username in email:
        password_b = bytes(password, "ascii")
        password_h = SHA1.new(password_b).hexdigest()
        if password_h == pwd[email.index(username)]:
            return redirect(url_for("login_2fa", username = username))
        else:
		# inform users if creds are invalid
            flash("You have supplied invalid login credentials!", "danger")
            return redirect(url_for("login"))
    else:
        flash("This email does not exist", "danger")
        return redirect(url_for("login"))

# dont have access to OTP route
@app.route("/no/OTP/")
def no_OTP():
    return render_template("forgot.html")
    
@app.route("/no/OTP/", methods=["POST"])
def no_OTP_send():
    username = request.form.get("username")
    
    if username in email:
        secret = pyotp.random_base32()
        otpad[email.index(username)] = secret
        o = open("otp.txt", "w")
        for z in otpad:
            o.writelines("%s\n" % z)
        o.close()

        msg = Message(subject = "Email Verification", sender= "mangotree0867@gmail.com", recipients= [username])
        msg.body="This is your new Secret Token: " + str(secret)
        mail.send(msg)
        flash("Email has been sent" , "success")
        return redirect(url_for("login"))
        
    else: 
        flash("Email does not exist", "danger")
        return redirect(url_for("no_OTP"))
    
# create 2FA page route
@app.route("/create/2fa/")
def create_2fa():
    secret = pyotp.random_base32()
    
    return render_template("create_2fa.html", secret=secret)
    
@app.route("/create/2fa/", methods=["POST"])
def save_2fa():
    secret = request.form.get("secret")
    
    otpad.append(secret)
    o = open("otp.txt", "w")
    for z in otpad:
        o.writelines("%s\n" % z)
    o.close()
    
    flash("Account Created!" ,"success")
    return redirect(url_for("login"))




# 2FA page route
@app.route("/login/2fa/<username>")
def login_2fa(username):
    # generating random secret key for authentication
    secret = otpad[email.index(username)]
    return render_template("login_2fa.html", secret=secret)


# 2FA form route
@app.route("/login/2fa/<username>", methods=["POST"])
def login_2fa_form(username):
    # getting secret key used by user
    secret = request.form.get("secret")
    # getting OTP provided by user
    otp = int(request.form.get("otp"))

    # verifying submitted OTP with PyOTP
    if pyotp.TOTP(secret).verify(otp):
        # inform users if OTP is valid
        flash("The TOTP 2FA token is valid", "success")
        return redirect(url_for("login_2fa",username =username))
    else:
        # inform users if OTP is invalid
        flash("You have supplied an invalid 2FA token!", "danger")
        return redirect(url_for("login_2fa",username= username))


# running flask server
if __name__ == "__main__":
    app.run(debug=True)
