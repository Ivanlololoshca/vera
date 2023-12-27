from flask import Flask
from regist import regist
from menu import menu

app = Flask(__name__)
app.register_blueprint(regist)
app.register_blueprint(menu)
