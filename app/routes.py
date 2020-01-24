from app import app, mail
from flask import render_template, url_for, request,redirect, flash
from flask_mail import Message
from app.forms import Email
from threading import Thread
# from .decorators import async


data = []

# @async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")    

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = Email()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["number"]
        msg = request.form["msg"]
        msg_email = Message(subject="Lesson", sender="LearnHackTutoring@gmail.com", recipients=["CMboyns14@hotmail.com", "harrison.boyns@hotmail.com"])
        msg_email.body = msg + "\n" + email + "\n" + phone + "\n" + name
        mail.send(msg_email)
        thr = Thread(target=send_async_email, args=[app, msg])
        thr.start()
        flash("Thanks for the Email! We will get back to you soon!")

        return redirect(url_for("home"))

    return render_template("contact.html", form=form)   


@app.route("/<user>", methods=["GET"])
def user(user):
    return render_template("user.html", user=user)   

@app.route("/faq", methods=["GET"])
def faq():
    return render_template("faq.html")   

@app.route("/hackers", methods=["GET"])
def hackers():
    return render_template("hackers.html") 

@app.errorhandler(404)
def fileNotFound(e):
    return (render_template("404.html"), 404)

@app.errorhandler(404)
def serverError(e):
    return (render_template("505.html"), 505)