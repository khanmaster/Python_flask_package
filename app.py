from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return " Welcome to python flask web app"

@app.route("/hi/")
def who():
    return " who are you?"

@app.route("/Hello/<username>")
def greet(username):
    return f" Welcome to python flask web app,{username}"

print(greet('shah'))