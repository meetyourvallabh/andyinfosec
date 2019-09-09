from flask import Flask, render_template, request, flash, redirect, url_for, session, send_from_directory
from flask_mail import Mail, Message
from random import *




app = Flask(__name__)



app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'developer@makeyourown.club'
app.config['MAIL_PASSWORD'] = 'myocoo@123'




mail = Mail(app)




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/training-programs/")
def training_programs():
    return render_template("training-programs.html")

@app.route("/contact-us/")
def contact_us():
    return render_template("contact-us.html")

@app.route("/about-us/")
def about_us():
    return render_template("about.html")

@app.route("/security-operation-center-expert/")
def security_operation_center_expert():
    return render_template("security-operation-center-expert.html")

@app.route("/web-application-security-expert/")
def web_application_security_expert():
    return render_template("web-application-security-expert.html")

@app.route("/cyber-security-for-beginners/")
def cyber_security_for_beginners():
    return render_template("cyber-security-for-beginners.html")

@app.route("/training-programs/web-application-security-expert/")
def web_application_security_expert1():
    return render_template("web-application-security-expert1.html")

@app.route("/certified-cyber-security-professional/")
def certified_cyber_security_professional():
    return render_template("certified-cyber-security-professional.html")


@app.route("/privacy-policy/")
def privacy_policy():
    return render_template("privacy-policy.html")


@app.route("/enroll-now/")
def enroll_now():
    return render_template("enroll.html")


@app.route("/faq/")
def faq():
    return render_template("faq.html")

@app.route("/why-andy-infosec/")
def why_andy_infosec():
    return render_template("why-andy-infosec.html")

@app.route("/customized-schedule/")
def customized_schedule():
    return render_template("customized-schedule.html")


@app.route("/when-can-i-start/")
def when_can_i_start():
    return render_template("when-can-i-start.html")

@app.route("/thank-you/")
def thank_you():
    return render_template("thank-you.html")

@app.route("/fees-payment/")
def fees_payment():
    return render_template("fees-payment.html")

@app.route("/services/")
def services():
    return render_template("services.html")

@app.route("/research/")
def research():
    return render_template("research.html")

@app.route("/send_contact",methods = ['POST'])
def send_contact():
    if request.method == 'POST':
        msg = Message('Andy InfoSec: New Inquiry request', sender='developer@makeyourown.club', recipients=['andyinfosec0@gmail.com','info@andyinfosec.com'])
        msg_string = '<h4> There is an new inquiry request.</h4> <br> <h2><bold>Name : </bold>'+ request.form['name'] +' </h2><h2><bold>Phone : </bold>'+ request.form['phone'] +' </h2><h2><bold>Email : </bold>'+ request.form['email'] +' </h2><h2><bold>Query regarding : </bold>'+ request.form['query'] +' </h2><h2><bold>Message : </bold>'+ request.form['message'] +' </h2>'
        msg.body = msg_string
        msg.html = msg.body
        mail.send(msg)
    return redirect(url_for('thank_you'))

@app.route("/send_enrollment",methods = ['POST'])
def send_enrollment():
    if request.method == 'POST':
        msg = Message('Andy InfoSec: New Enrollment request', sender='developer@makeyourown.club', recipients=['andyinfosec0@gmail.com','info@andyinfosec.com'])
        msg_string = '<h4> There is an new enrollment request.</h4> <br> <h2><bold>Name : </bold>'+ request.form['fname'] +' '+ request.form['lname'] +' </h2><h2><bold>Phone : </bold>'+ request.form['phone'] +' </h2><h2><bold>Email : </bold>'+ request.form['email'] +' </h2><h2><bold>Training program : </bold>'+ request.form['training_program'] +' </h2><h2><bold>Mode of training : </bold>'+ request.form['training_mode'] +' </h2>'
        msg.body = msg_string
        msg.html = msg.body
        mail.send(msg)
    return redirect(url_for('fees_payment'))

@app.route('/page-sitemap.xml/')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/page-sitemap.html/')
def page_sitemap():
    return render_template("sitemap-page.html")

@app.route('/offer/')
def offer():
    return render_template("offer.html")

@app.errorhandler(404)
def error404(error):
    return render_template("error404.html"), 404

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug='true')