from flask import Flask
from flask_mail import Mail
import os
import config

SECRET_KEY = os.urandom(32)

application = Flask(__name__)
application.config["debug"] = True
application.config['MAIL_SERVER']='smtp.gmail.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USERNAME'] = 'LearnHacktutoring@gmail.com'
application.config['MAIL_PASSWORD'] = 'LearnHack14!'
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True

application.config.from_object(config.Config)

mail = Mail(application)


from application import routes

# git clone https://github.com/ClackerWhacker/Tutoring_3.git