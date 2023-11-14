from email.message import EmailMessage
from pass2 import password  #confidential
import ssl
import smtplib

email_sender = 'polushyn.stas@gmail.com'
email_password = password

email_receiver = 'fisoge6230@rdluxe.com'

subject = 'This is my first try of making Email sender'
body = """When you read this message, remember you are the best 😎 """
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())






