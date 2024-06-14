from flask import Flask, render_template, request, redirect, jsonify
from flask_mail import Mail, Message
from waitress import serve
from mailjet_rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configuration for Flask-Mail
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Corrected the server address
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'cizzera@gmail.com'  # Your email
# app.config['MAIL_PASSWORD'] = 'micheal65'  # Your password (use environment variable for security)
mail_jetapi = 'cbdad0890ca8ff2407ee96c5597b707'
mail_jetapi_secret = '4a5bae96ce8b0db70ae19a0fde22423f'
mailjet = Client(auth=(os.getenv('mail_jetapi'), os.getenv('mail_jetapi_secret')), version= 'v3.1')
# mail = Mail(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sendEmail', methods=['POST'])
def sendEmail():
    name = request.form.get('name')
    sender_email = request.form.get('email')
    message = request.form.get('message')
    # msg = Message('New Form Submission', sender='cizzera@gmail.com', recipients=['cizzera@gmail.com'])
    # msg.body = f"Name: {name}\nEmail: {sender_email}\nMessage: {message}"
    data = {
        'Messages' : [
            {
                "From":{
                    "Email": "cizzera@gmail.com",
                    "Name": "Cizzar"
                },
                "To": [
                    {
                        "Email": "cizzera@gmail.com",
                        "Name": "Cizzar"
                    }
                ],
                "Subject": "New Form Submission",
                "TextPart": f"Name:{name}\nEmail:{sender_email}\nMessage: {message}",
            }
        ]
    }
    result =mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json)
    return redirect('/')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=200)
