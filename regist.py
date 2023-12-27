from flask import Blueprint, render_template, request, make_response, redirect
import psycopg2

regist = Blueprint("regist", __name__)


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


@regist.route("/regist/osebe")
def start():
    return render_template("osebe.html")


@regist.route("/regist/register", methods=["GET", "POST"])
def registerPage():
    errors = []
    if request.method == "GET":
        return render_template("register.html", errors=errors)

    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template("register.html", errors=errors)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"select username from users where username = '{username}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")
        cur.close()
        conn.close()
        return render_template("register.html", errors=errors)

    cur.execute(f"insert into users (username, password) values ('{username}','{password}');")

    conn.commit()
    cur.close()
    conn.close()

    return redirect("/regist/osebe")

@regist.route("/regist/zaregist", methods=['GET', 'POST'])

def start_zaregist():
    if request.method == 'POST':
        name = request.form.get('name')
        service = request.form.get('service')
        experience = request.form.get('experience')
        price = request.form.get('price')
        about = request.form.get('about')

       
        return render_template("zaregist.html", name=name, service=service, experience=experience, price=price, about=about)

   
    return render_template("zaregist.html")

@regist.route("/regist/glavmen")
def glavmen():
    return render_template("glavmen.html")

@regist.route("/regist/1")
def start_1():
    return render_template("1.html")
    
@regist.route("/regist/2")
def start_2():
    return render_template("2.html")

@regist.route("/regist/3")
def start_3():
    return render_template("3.html")

@regist.route("/regist/4")
def start_4():
    return render_template("4.html")

@regist.route("/regist/5")
def start_5():
    return render_template("5.html")

@regist.route("/regist/6")
def start_6():
    return render_template("6.html")

@regist.route("/regist/7")
def start_7():
    return render_template("7.html")

@regist.route("/regist/8")
def start_8():
    return render_template("8.html")

@regist.route("/regist/9")
def start_9():
    return render_template("9.html")

@regist.route("/regist/10")
def start_10():
    return render_template("10.html")

@regist.route("/regist/11")
def start_11():
    return render_template("11.html")

@regist.route("/regist/12")
def start_12():
    return render_template("12.html")

@regist.route("/regist/13")
def start_13():
    return render_template("13.html")

@regist.route("/regist/14")
def start_14():
    return render_template("14.html")

@regist.route("/regist/15")
def start_15():
    return render_template("15.html")

@regist.route("/regist/16")
def start_16():
    return render_template("16.html")


    

