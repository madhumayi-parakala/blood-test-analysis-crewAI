from flask import Flask
from flask_mail import Mail, Message
import os

# Initialize Flask and Flask-Mail
app = Flask(__name__)
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'true'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'true'

mail = Mail(app)

def send_email(recipient, recommendations, articles):
    """
    Sends an email with health recommendations and related articles.

    Parameters:
    - recipient: The email address of the recipient.
    - recommendations: Health recommendations to include in the email.
    - articles: List of relevant articles to include in the email.
    """
    subject = "Your Health Analysis Results"
    body = f"""
    Dear User,

    Here are your health recommendations based on your blood test results:

    {recommendations}

    Additionally, here are some articles that may be helpful for you:
    {articles}

    Best regards,
    Your Health Advisor
    """

    msg = Message(subject, recipients=[recipient])
    msg.body = body

    try:
        with app.app_context():
            mail.send(msg)
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {str(e)}")
