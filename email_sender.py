import smtplib
import os
import time
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
SENDER_EMAIL = os.getenv("EMAIL_USER")
SENDER_PASSWORD = os.getenv("EMAIL_PASS")

def send_email(to_email, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        time.sleep(2)  # Prevents rate-limiting
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

        server.quit()
        return True
    except Exception as e:
        return str(e)
