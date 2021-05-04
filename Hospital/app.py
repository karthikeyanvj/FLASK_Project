import time

from flask import Flask, render_template, request, flash, session, url_for, redirect
from flask_mysqldb import MySQL
from time import *

hospital = Flask(__name__)
hospital.secret_key = "#gydgvdsfkgdfw4587yt45g"

hospital.config['MYSQL_HOST'] = 'localhost'
hospital.config['MYSQL_USER'] = 'root'
hospital.config['MYSQL_PASSWORD'] = ''
hospital.config['MYSQL_DB'] = 'hospital'

mysql = MySQL(hospital)
print("success")


@hospital.route("/")
def home_page():
    return render_template("home.html")


@hospital.route("/admin_page")
def admin_page():
    return render_template("admin_homepage.html")


@hospital.route("/admin_login_data", methods=["POST"])
def admin_login_data():
    error_message = ''
    UNAME = "admin"
    PASSWORD = "123456"
    if request.method == "POST":
        uname = request.form.get("username")
        password = request.form.get("password")
        if len(uname) == 0 and len(password) == 0:
            error_message = "Username and password is empty "
        elif len(uname) == 0:
            error_message = "Username is empty"
        elif len(password) == 0:
            error_message = "Password is empty"
        else:
            if uname != UNAME or password != PASSWORD:
                error_message = "Invalid Login Credentials"
            else:
                return render_template("admin_main_page.html")

    return render_template('admin_homepage.html', error=error_message)


@hospital.route("/add_doctor")
def add_doctor():
    return render_template('add_doctor.html')


@hospital.route("/add_doctor_data", methods=["POST", "GET"])
def add_doctor_data():
    if request.method == "POST":
        dc_name = request.form.get("dc_name")
        dc_exp = request.form.get("dc_exp")
        dc_speciality = request.form.get("dc_speciality")
        dc_gender = request.form.get("dc_gender")
        cur = mysql.connection.cursor()
        sql = "INSERT INTO doctordetail(name,experience,speciality,gender) VALUES (%s,%s,%s,%s)"
        val = (dc_name, dc_exp, dc_speciality, dc_gender)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        flash("Doctor Added Successfully")
    return redirect(url_for("add_doctor"))


@hospital.route("/dc_login", methods=["POST", "GET"])
def dc_login():
    return render_template("doctor_login.html")


@hospital.route("/dc_login_data", methods=["POST", "GET"])
def dc_login_data():
    error_message = ''
    if request.method == "POST":
        dc_id = request.form.get("dc_id")
        dc_name = request.form.get("dc_name")
        if len(dc_id) == 0 and len(dc_name) == 0:
            error_message = "ID and Doctor name is empty "
        elif len(dc_id) == 0:
            error_message = "Doctor ID is empty"
        elif len(dc_name) == 0:
            error_message = "Doctor name is empty"
        else:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM DOCTORDETAIL WHERE doctorid=%s and name=%s", (dc_id, dc_name))
            data = cur.fetchone()
            rowcount = cur.rowcount
            if rowcount < 1:
                error_message = "Incorrect ID or name..Please retry"
            else:
                return redirect("appointment")
        return render_template("doctor_login.html", error=error_message)


@hospital.route("/new_patient")
def new_patient():
    return render_template("new_patient.html")


@hospital.route("/add_patient_data", methods=["POST", "GET"])
def add_patient_data():
    if request.method == "POST":
        pt_name = request.form.get("pt_name")
        pt_age = request.form.get("pt_age")
        ph_number = request.form.get("ph_number")
        pt_gender = request.form.get("pt_gender")
        cur = mysql.connection.cursor()
        sql = "INSERT INTO patientdetail (pt_name,pt_age,ctnumber,pt_gender) VALUES (%s,%s,%s,%s)"
        val = (pt_name, pt_age, ph_number, pt_gender)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        flash("Successfully Registered..Thankyou")
    return redirect("new_patient")


@hospital.route("/patient_login")
def pt_login():
    return render_template("pt_login.html")


@hospital.route("/pt_login_data", methods=["POST", "GET"])
def pt_login_data():
    error_message = ''
    if request.method == "POST":
        pt_id = request.form.get("pt_id")
        pt_name = request.form.get("pt_name")
        if len(pt_id) == 0 and len(pt_name) == 0:
            error_message = "ID and Patient name is empty "
        elif len(pt_id) == 0:
            error_message = "Patient ID is empty"
        elif len(pt_name) == 0:
            error_message = "Patient name is empty"
        else:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM PATIENTDETAIL WHERE patientid=%s and pt_name=%s", (pt_id, pt_name))
            data = cur.fetchone()
            rowcount = cur.rowcount
            if rowcount < 1:
                error_message = "Incorrect ID or name..Please retry"
            else:
                return render_template("appt_booking.html")
        return render_template("pt_login.html", error=error_message)


@hospital.route("/booking")
def booking_page():
    return render_template("appt_booking.html")


@hospital.route("/appt_data", methods=["POST", "GET"])
def booking_data():
    if request.method == "POST":
        pt_id = request.form.get("pt_id")
        pt_name = request.form.get("pt_name")
        pt_age = request.form.get("pt_age")
        gender = request.form.get("gender")
        date = request.form.get("date")
        appt_time = request.form.get("time")
        symptoms = request.form.get("symptoms")
        cur = mysql.connection.cursor()
        sql = "INSERT INTO appointment (pt_id,pt_name,pt_age,gender,visit_date,timing,symptoms) VALUES (%s,%s,%s,%s," \
              "%s,%s,%s) "
        val = (pt_id, pt_name, pt_age, gender, date, appt_time, symptoms)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        flash("Appointment Booked..Thankyou")
    return redirect("booking")


@hospital.route("/appointment_view")
def view_appointment():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM appointment")
    data = cur.fetchall()
    return render_template("appt_display.html", data=data)


@hospital.route("/appointment")
def admin_view_appointment():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM appointment")
    data = cur.fetchall()
    return render_template("admin_apptdisplay.html", data=data)


@hospital.route("/delete_appt/<string:pt_id>", methods=["POST", "GET"])
def delete_appt(pt_id):
    flash("Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM appointment where pt_id=%s", (pt_id,))
    mysql.connection.commit()
    cur.close()
    return redirect("/appointment")


@hospital.route("/update_appt")
def update_appt():
    return render_template("update_appt.html")


@hospital.route("/update_apptdata", methods=["POST", "GET"])
def update_apptdata():
    if request.method == "POST":
        pt_id = request.form["pt_id"]
        date = request.form["date"]
        time = request.form["time"]
        cur = mysql.connection.cursor()
        cur.execute("UPDATE appointment SET visit_date=%s,timing=%s WHERE pt_id=%s", (date, time, pt_id,))
        flash("Updated Successfully")
        mysql.connection.commit()
        cur.close()
        return redirect("update_appt")


@hospital.route("/edit_doctor")
def edit_doctor():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM doctordetail")
    data = cur.fetchall()
    return render_template("doctorslist.html", data=data)


@hospital.route("/delete_doctor/<string:doctorid>", methods=["POST", "GET"])
def delete_doctor(doctorid):
    flash("Doctor Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM doctordetail where doctorid=%s", (doctorid,))
    mysql.connection.commit()
    cur.close()
    return redirect("/edit_doctor")


@hospital.route("/update_doctor")
def update_doctorpage():
    return render_template("update_doctor.html")


@hospital.route("/update_dcdata", methods=["POST", "GET"])
def update_dcdata():
    if request.method == "POST":
        dc_id = request.form["dc_id"]
        dc_name = request.form["dc_name"]
        dc_exp = request.form["dc_exp"]
        speciality = request.form["speciality"]
        cur = mysql.connection.cursor()
        cur.execute("UPDATE doctordetail SET name=%s,experience=%s,speciality=%s WHERE doctorid=%s",
                    (dc_name, dc_exp, speciality, dc_id,))
        flash("Updated Successfully")
        mysql.connection.commit()
        cur.close()
        return redirect("update_doctor")


@hospital.route("/pharmacy", methods=["POST", "GET"])
def pharmacy_page():
    return render_template("pharmacy_home.html")


@hospital.route("/pharma_data", methods=["POST", "GET"])
def pharma_data():
    if request.method == "POST":
        medicine_name = request.form.get("medicine_name")
        expiry_date = request.form.get("expiry_date")
        manf_date = request.form.get("manf_date")
        availability = request.form.get("availability")
        cur = mysql.connection.cursor()
        sql = "INSERT INTO medicine (medicine_name,expiry_date,manf_date,availability) VALUES (%s,%s,%s,%s)"
        val = (medicine_name, expiry_date, manf_date, availability)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        flash("Medicine ADDED")
    return redirect("pharmacy")


@hospital.route("/medicine_list")
def medicine_list():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM medicine")
    data = cur.fetchall()
    return render_template("medicine_list.html", data=data)


if __name__ == "__main__":
    hospital.run(debug=True)
