from flask import Blueprint, render_template, request, make_response, redirect
akkaynt = Blueprint('akkaynt', __name__)

@akkaynt.route("/akkaynt/reg")
def start():
    return render_template("akkaynt.html")