import smtplib
from email.mime.text import MIMEText
def send_mail(customer,dealer,rating,comment):
    port = 2525
    smtp_server = "smtp.mailtrap.io"
    login = "dcd2b30e4ce602"
    password = "6a65eb2be13d9a"
    message = f"<h3> New FEEDBACK Submission </h3><ul><li> customer : {customer} </li><li> dealer : {dealer} </li><li> Rating : {rating} </li><li> Comments : {comment} </li></ul>"
    sender_email = "email1@example.com"
    receiver_email = "email2@example.com"
    msg = MIMEText(message, "html")
    msg['Subject'] = "LEXUS FEEDBACK"
    msg["From"] = "sender_email"
    msg["To"] = "receiver_email"
    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
