from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return " Welcome to python flask web app"

@app.route("/hi/")
def who():
    return " Would you like to introduce yourself ? "

@app.route("/Hello/<username>/")
def greet(username):
    return f" Welcome to python flask web app dear {username}"

print(greet('shahrukh'))