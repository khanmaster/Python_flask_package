# Installing flask package
## Use cases of flask
### Utilising Flask class for routing to launch the browser 

- Install flask package
- ``` pip install flask ```

### Moving onto building our web-app with flask
- step-1 Create package in pycharm
- step-2 Create app.py
- step-3 use the code below


``` python
# importing flask pakcage
from flask import Flask

app = Flask(__name__)
# creating an app instance

@app.route("/")
def index():
    return " Welcome to python flask web app"
# calling the method index at at the endpoint 
# index() method will return welcome page for 

@app.route("/hi/")
def who():
    return " Would you like to introduce yourself ? "

@app.route("/Hello/<username>/")
def greet(username):
    return f" Welcome to python flask web app dear ,{username}"

print(greet('shahrukh'))

```

- in pycharm terminal run
- ``` flask run ```
- You should see below outcome in pycharm termimal
```python
 Welcome to python flask web app dear ,shahrukh
 * Running on http://localhost:5000/ (Press CTRL+C to quit)

```
- Check your browser now
- ``` localhost:5000```
- You should see welcome page
- ```localhost:5000/hi ```
- change the address into your browser as above
- ```localhost:5000/Hi/Shahukh ```
- Finally check the last route if our app

# AMAZING!!! 
