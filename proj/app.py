# From the project folder, open this Python file in a terminal window
# Then visit localhost:5000 in a web browser

from flask import * # Install Python and Flask on your local machine
import sqlite3
import hashlib


# Create Flask
app = Flask(__name__)
# Custom key for the Flask app
app.secret_key = 'this is a key'
#app.permanent_session_lifetime = timedelta(minutes=5)


# Create database for user accounts and anything else
con = sqlite3.connect('data.db', check_same_thread=False, timeout=10000)


# Create a users table in the database
cur = con.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS Users (
     "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "firstname" TEXT NOT NULL,
    "lastname" TEXT NOT NULL,
    "phone" TEXT NOT NULL,
    "email"    TEXT NOT NULL,
    "password"    TEXT NOT NULL
);
''')

con.commit()

#SQL Funtions
#def AddUser(firstname_form, lastname_form, phone_form, email_form, password_form):
#    with con:
#        cur.execute("INSERT INTO Users (firstname, lastname, phone, email, password) VALUES (?, ?, ?, ?, ?)", (firstname_form, lastname_form, phone_form, email_form, password_form ))

#def DeleteUser(email_form):
#    with con:
#        cur.execute("DELETE FROM Users WHERE EMAIL = (?)", (email_form))

#def update(user, unit_user, unit_fp):
#    with con:
#        cur.execute("UPDATE FloorPlan SET currentUser = (?) WHERE unit_num = (?)", (user, unit_fp))
#        cur.execute("UPDATE Users SET unit_num = (?) WHERE email = (?)", (unit_user, user))
#        con.commit()

    #hardcoded for now
name = 'Guest'

@app.route('/')
def home():
    # Check if a user is currently logged in

    return render_template('index.html', usr = name)

#Details of Systems page
@app.route("/detailsSys/")
def detailsSys():

    return render_template('detailsSys.html', usr = name)

#login page the POST and GET methods are made clear here because we will be sending data
@app.route("/login/", methods=["POST", "GET"])
def login():
    #later this if will help us with db stuff
    if request.method == "POST":
        session.permanent = True
        e = request.form["email"]
        p = request.form["pass"]
        session["email"] = e
        session["pass"] = p

        return render_template('login.html')
    else:
        return render_template('login.html')

@app.route("/register/", methods=["POST", "GET"])
def register():
    #later this if will help us with db stuff
    if request.method == "POST":
        return render_template('register.html')
    else:
        return render_template('register.html')

@app.route("/safetyRelatedData/")
def safetyRelatedData():

    return render_template('safetyRelatedData.html')

if __name__ == '__main__':
    app.run(debug=True)
