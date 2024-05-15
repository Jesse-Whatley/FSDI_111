from flask import Flask        # from flask module import the Flask class

app = Flask(__name__)          # create an instance of Flask(now an object)

@app.get("/")                  # Flask decorator that allows us to define routes
def index():                   # view function
    me = {                     # python dictionary (key-value pairs)
        "first_name": "Jesse",
        "last_name": "Whatley",
        "hobbies": "Crochet",
        "is_online": True
    }
    return me                  #returning a dictionary in flask converts it to JSON