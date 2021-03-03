# From the project folder, open this Python file in a terminal window
# Then visit localhost:5000 in a web browser

from flask import * # Install Python and Flask on your local machine
#import sqlite3
#import hashlib


# Create Flask
app = Flask(__name__)

# Custom key for the Flask app
app.secret_key = 'this is a key'


# Create database for user accounts and apartment units and anything else
#con = sqlite3.connect('data.db', check_same_thread=False, timeout=10000)


# Create a users and floorplan table in the database
#cur = con.cursor()

#cur.execute(''' CREATE TABLE IF NOT EXISTS Users (
#     "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#    "firstname" TEXT NOT NULL,
#    "lastname" TEXT NOT NULL,
#    "phone" TEXT NOT NULL,
#    "email"    TEXT NOT NULL,
#    "password"    TEXT NOT NULL
#);
#''')

#con.commit()

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


app = Flask(__name__)


@app.route('/')
def home():

    # Check if a user is currently logged in
#    if session.get('loggedin') == True:
#        print("logged in = " + str(session['loggedin']) + "    " + str(session['user_email']))
#        pass
#    else:
        # Session variables
#        session['loggedin'] = False
#        session['user_email'] = ""


    #msg = "Hello World!"
    #return render_template('index.html', user=session['user_email'])
    return render_template('index.html')

if __name__ == '__main__':
    app.run() 
