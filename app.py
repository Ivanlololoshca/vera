from flask import Flask 
app = Flask (__name__)

@app.route("/")
@app.route("/index")
def start():
    return " " 

@app.route("/menu")
def menu():
    return " "
    