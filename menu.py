from flask import Blueprint, render_template, request, make_response, redirect
menu = Blueprint('menu', __name__)

@menu.route("/")
@menu.route("/menu")
def start():
    return render_template("bavito.html")

