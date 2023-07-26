import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "yesjuan519@gmail.com"
    password = "vaittiaqqzzuyvig"
    # this is the gmail key for aps
    receiver = "yesjuan519@gmail.com"
    context = ssl.create_defult_context()
    message = """\
    Subject: Hi!
    How are you!
    Bye!
    """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email()