from flask import Blueprint, render_template, request, redirect
import psycopg2

zaregist = Blueprint("zaregist", __name__)

def dbConnect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='RGZ',
        user='postgres',
        password='postgres',
        port='5433'
    )
    return conn

def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@zaregist.route("/regist/zaregist", methods=["GET", "POST"])
def registerProfile():
    if request.method == "GET":
        return render_template("zaregist.html")  # Замените на ваш шаблон

    username = request.form.get("username")
    name = request.form.get("name")
    service = request.form.get("service")
    experience = request.form.get("experience")
    price = request.form.get("price")
    numberc = request.form.get("numberc")
    maillc = request.form.get("maillc")
    about = request.form.get("about")

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_profiles (username, name, service, experience, price, numberc, maillc, about)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """, (username, name, service, experience, price, numberc, maillc, about))

    conn.commit()
    cur.close()
    conn.close()

    return redirect('/regist/zaregist')