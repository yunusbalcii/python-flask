from flask import Flask, render_template, send_from_directory,request
from flask_mail import Mail,Message
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/images/<path:filename>')
def download_file(filename):
    directory = os.path.join(os.getcwd(), 'images')
    return send_from_directory(directory, filename)

@app.route('/send_email', methods=['POST'])
def send_email():
    #from input
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    subject = f'Flask Contact Form {email}'
    body = f'Name: {name}\nEmail: {email}\nMessage: {message}'

    msg = Message(subject, recipients=email)
    msg.body = body
    mail.send(msg)
    return 'Email sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
