# From the project folder, open this Python file in a terminal window
# Then visit localhost:5000 in a web browser

from flask import * # Install Python and Flask on your local machine

app = Flask(__name__)


@app.route('/')
def hello_world():

    msg = "Hello World!"
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run() 
