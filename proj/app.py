# From the project folder, open this Python file in a terminal window
# Then visit localhost:5000 in a web browser

from flask import * # Install Python and Flask on your local machine
from datetime import timedelta
import sqlite3
import hashlib


# Create Flask
app = Flask(__name__)
# Custom key for the Flask app
app.secret_key = "this is a key"
#app.permanent_session_lifetime = timedelta(minutes=5)


#################################### Database Functions ################################################
# Create database for user accounts and anything else
con = sqlite3.connect('data.db', check_same_thread=False, timeout=10000)

# Create a users table in the database
cur = con.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS Users (
     "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "firstname" TEXT NOT NULL,
    "lastname" TEXT NOT NULL,
    "email"    TEXT NOT NULL,
    "password"    TEXT NOT NULL
);
''')

con.commit()

#SQL Funtions
def AddUser(firstname_form, lastname_form, email_form, password_form):
    with con:
        cur.execute("INSERT INTO Users (firstname, lastname, email, password) VALUES (?, ?, ?, ?)", (firstname_form, lastname_form, email_form, password_form ))
        con.commit()

def FindPass(email_form):
    with con:
        row = cur.execute("SELECT password FROM Users WHERE email =?", (email_form,)).fetchall()
        con.commit()
        password_form = ''.join(row[0])
    return password_form

def FindName(email_form):
    with con:
        row = cur.execute("SELECT firstname FROM Users WHERE email =?", (email_form,)).fetchall()
        con.commit()
        firstname_form = ''.join(row[0])
    return firstname_form

#def DeleteUser(email_form):
#    with con:
#        cur.execute("DELETE FROM Users WHERE EMAIL = (?)", (email_form))

#hardcoded for now
#name will be stored by the session and passed to the pages
guest = 'Guest'

######################################## Login and Resister ###########################################

@app.route('/', methods =["GET", "POST"])
def loginDemo():
    if request.method == "POST":
        email = request.form.get("email")
        passwrd = request.form.get("password")
        print("Password found is: " + FindPass(email))
        if request.form.get("signin-btn") == "access" and passwrd == FindPass(email):
            session["user"] = FindName(email)
            return redirect(url_for("home"))
    else:
        if "user" in session:
            user = session["user"]
            return redirect(url_for("userInfo"))

    return render_template('signin.html')

@app.route('/up', methods =["GET", "POST"])
def signupDemo():
    if request.method == "POST" and request.form.get("signup-btn") == "access":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("signup-email")
        passwrd = request.form.get("signup-password")
        session["user"] = fname
        AddUser(fname, lname, email, passwrd)
        return redirect(url_for("home"))

    else:
        if "user" in session:
            user = session["user"]
            return redirect(url_for("userInfo"))

    return render_template('signin.html')

#login page the POST and GET methods are made clear here because we will be sending data
#@app.route("/login/", methods=["POST", "GET"])
#def login():
    #later this if will help us with db stuff
#    if request.method == "POST":
#        session.permanent = True
#        e = request.form["email"]
#        p = request.form["pass"]
#        session["email"] = e
#        session["pass"] = p
#
#        with con:
#            cur = con.cursor()
#            p2 = cur.execute("SELECT " + password + "FROM Users where " + email + "=?", (e,)).fetchall()
#            con.close()
#
#            if p2 == p:
#                print("Successful login")
#
#        return render_template('login.html')
#    else:
#        return render_template('login.html')
#
#@app.route("/register/", methods=["POST", "GET"])
#def register():
#    #later this if will help us with db stuff
#    if request.method == "POST":
#        return render_template('register.html')
#    else:
#        return render_template('register.html')



########################################## Home ########################################################

@app.route("/home/")
def home():
    if "user" in session:
        user = session["user"]
        return render_template('index.html', usr = user)

    else:
        return render_template('index.html', usr = guest)

########################################## User Info ########################################################
@app.route("/userInfo/")
def userInfo():
    if "user" in session:
        user = session["user"]
        return render_template('userInfo.html', usr = user)
    else:
        return redirect(url_for('loginDemo'))

######################################## Details of Systems ##############################################
#Details of Systems main page
@app.route("/detailsSys/")
def detailsSys():
    if "user" in session:
        user = session["user"]
        return render_template('detailsSys.html', usr = user)

    else:
        return render_template('detailsSys.html', usr = guest)


######################################## Safety Related Data #############################################
#Safety Related Data main page
@app.route("/safetyRelatedData/")
def safetyRelatedData():
    if "user" in session:
        user = session["user"]
        return render_template('safetyRelatedData.html', usr = user)

    else:
        return render_template('safetyRelatedData.html', usr = guest)

#Safety Related Data/ Add Data to Table page
@app.route("/safetyRelatedData/addDataToTable/")
def addDataToTable():
    if "user" in session:
        user = session["user"]
        return render_template('addDataToTable.html', usr = user)

    else:
        return render_template('addDataToTable.html', usr = guest)

#Safety Related Data/ Change Access Permissions page
@app.route("/safetyRelatedData/changeAccessPerms/")
def changeAccessPerms():
    if "user" in session:
        user = session["user"]
        return render_template('changeAccessPerms.html', usr = user)

    else:
        return render_template('changeAccessPerms.html', usr = guest)

#Safety Related Data/ Save Details to The Database page
@app.route("/safetyRelatedData/saveDetailsToDB/")
def saveDetailsToDB():
    if "user" in session:
        user = session["user"]
        return render_template('saveDetailsToDB.html', usr = user)

    else:
        return render_template('saveDetailsToDB.html', usr = guest)


######################################## Safety Analysis Tool ############################################
#Safety Analysis Tool main page
@app.route("/safetyAnalysisTool/")
def safetyAnalysisTool():
    if "user" in session:
        user = session["user"]
        return render_template('safetyAnalysisTool.html', usr = user)

    else:
        return render_template('safetyAnalysisTool.html', usr = guest)

@app.route("/safetyAnalysisTool/uploadExistingSys/")
def uploadExistingSys():
    if "user" in session:
        user = session["user"]
        return render_template('uploadExistingSys.html', usr = user)

    else:
        return render_template('uploadExistingSys.html', usr = guest)

@app.route("/safetyAnalysisTool/addNewSys/")
def addNewSys():
    if "user" in session:
        user = session["user"]
        return render_template('addNewSys.html', usr = user)

    else:
        return render_template('addNewSys.html', usr = guest)

@app.route("/safetyAnalysisTool/loadFromDB/")
def loadFromDB():
    if "user" in session:
        user = session["user"]
        return render_template('loadFromDB.html', usr = user)

    else:
        return render_template('loadFromDB.html', usr = guest)

@app.route("/contact/")
def contact():
    return render_template('contact.html')

########################################### Logout ######################################################
@app.route("/logout/")
def logout():
    if "user" in session:
        user = session["user"]
        flash("Logout Successful", "info")
    session.pop("user", None)
    return redirect(url_for('loginDemo'))
############################################ End ########################################################

if __name__ == '__main__':
    app.run(debug=True)
