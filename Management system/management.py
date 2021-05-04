from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL

management = Flask(__name__)
management.secret_key = "dxfssfgcdgfdfdsfsfsfjsfshfsdhg"

management.config['MYSQL_HOST'] = 'localhost'
management.config['MYSQL_USER'] = 'root'
management.config['MYSQL_PASSWORD'] = ''
management.config['MYSQL_DB'] = 'kar'

mysql = MySQL(management)
print("success")


@management.route("/")
def home():
    return render_template("home_page.html")

@management.route("/home1")
def home1():
    return render_template("test.html")



@management.route("/staff")
def staff_page():
    return render_template("staff_login.html")


@management.route("/student")
def student_page():
    return render_template("student_login.html")


@management.route("/add_mark")
def add_mark():
    return render_template("marks.html")


@management.route("/admin")
def admin_page():
    return render_template("register.html")


@management.route("/staff_login_data", methods=['POST', 'GET'])
def stafflogin():
    error_message = ''
    UNAME = "staff"
    PASSWORD = 12345
    if request.method == 'POST':
        uname = request.form.get('username')
        password = request.form.get('password')
        if len(uname) == 0 and len(password) == 0:
            error_message = "Username and password is empty "
        elif len(uname) == 0:
            error_message = "Username is empty"
        elif len(password) == 0:
            error_message = "Password is empty"
        else:
            if uname != UNAME and password != PASSWORD:
                error_message = "Invalid Login Credentials"
            else:
                return render_template("marks.html")
    return render_template('staff_login.html', error=error_message)


@management.route("/student_login_data", methods=['POST', 'GET'])
def studentlogin():
    error_message = ''
    if request.method == "POST":
        id = request.form['st_id']
        cls = request.form['st_class']
        if len(id) == 0 and len(cls) == 0:
            error_message = "ID and class is empty "
        elif len(id) == 0:
            error_message = "ID is empty"
        elif len(cls) == 0:
            error_message = " Class is empty"
        else:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM marks WHERE id = %s AND class = %s", (id, cls))
            data = cur.fetchall()
            countRows = cur.rowcount
            if countRows < 1:
                error_message = "Invalid Login credentials"
            else:
                return render_template('dashboard.html', user=data, id=id, cls=cls)

    return render_template("student_login.html", error=error_message)


@management.route("/register_data", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        id = request.form['id']
        name = request.form['name']
        cls = request.form['class']
        cur = mysql.connection.cursor()
        sql = "INSERT INTO STUDENT_DETAILS(id,name,class) VALUES (%s,%s,%s)"
        val = (id, name, cls)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        flash("Successfully added")
    return render_template('display.html')


@management.route("/marks", methods=['post', 'get'])
def marks():
    if request.method == "POST":
        id = request.form['id']
        st_name = request.form['st_name']
        subject = request.form['subject']
        marks = request.form['marks']
        cls = request.form['class']
        cur = mysql.connection.cursor()
        sql = "INSERT INTO marks (id,name,subject,marks,class) VALUES (%s,%s,%s,%s,%s)"
        val = (id, st_name, subject, marks, cls)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        flash("Marks added successfully")
    return render_template("display1.html")


if __name__ == "__main__":
    management.run(debug=True, use_reloader=True)
