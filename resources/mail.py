from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from logger import logger
import smtplib
from email.message import EmailMessage


def send_message(p_message):
    try:
        msg = MIMEMultipart()

        password = ""
        msg['From'] = ""
        msg['To'] = ""
        msg['Subject'] = ""

        msg.attach(MIMEText(p_message, 'plain'))
        server = smtplib.SMTP('')
        server.starttls()
        server.ehlo()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("successfully sent email to %s:" % (msg['To']))

    except TypeError as err:
        logger.error("[mail.py] - TypeError: " + str(err))
    except ValueError as err:
        logger.error("[mail.py] - ValueError: " + str(err))
    except KeyError as err:
        logger.error("[mail.py] - KeyError: " + str(err))
