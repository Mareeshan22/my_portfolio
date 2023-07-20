from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Set up the email details
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email
    msg["To"] = "mareeshan22022001@gmail.com"  # Replace with your desired email address
    msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login("mareeshan22022001@gmail.com", "jzlqdnfksdgdzyxn")  # Replace with your email credentials
            smtp.send_message(msg)
    except smtplib.SMTPException:
        return "Error: Failed to send email"
    
    return "Email sent successfully!"

if __name__ == '__main__':
    app.run()
    app.static_folder = 'static'

