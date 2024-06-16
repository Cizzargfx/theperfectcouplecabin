from flask import Flask, render_template, request, redirect, jsonify
from flask_mail import Mail, Message
from waitress import serve
# from mailjet_rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['SECRET_KEY'] = '62c32dd6514c1e835031eaf7a9d9f1adf4004714cc8be2f8'
app.config['MAIL_SERVER'] = 'smtp.office365.com'  # Corrected the server address
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('email')  # Your email
app.config['MAIL_PASSWORD'] = os.getenv('password')  # Your password (use environment variable for security)

app.config['MAIL_DEFAULT_SENDER'] = os.getenv('email')
mail = Mail(app)

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
    msg = Message('New Form Submission', sender=os.getenv('email'), recipients=[os.getenv('email')])
    msg.body = f"Name: {name}\nEmail: {sender_email}\nMessage: {message}"

    try:
        mail.send(msg)
        return "Email sent..."
    except Exception as e:
        print(e)
        return f"The Email not sent {e} "


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=200)
