# Send email with python to yourself or a recpient
import smtplib

import config


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.YOUR_EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.YOUR_EMAIL_ADDRESS, config.RECPIENT_EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Test subject"
msg = "Hello there, how are you today?"

send_email(subject, msg)