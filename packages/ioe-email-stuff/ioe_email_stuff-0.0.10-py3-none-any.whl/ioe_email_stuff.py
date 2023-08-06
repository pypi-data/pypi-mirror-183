import logging, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
from os import makedirs

makedirs("./logs", exist_ok=True)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('./logs/email.log')
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.debug("-------Starting Execution-------")

def send_email(subject:str, body:str, username:str, passwd:str, to:str, cc:str="", bcc:str="", files:list[str]=None) -> None:
    """Sends an email via outlook smtp authentication """

    server = 'smtp.outlook.com'
    port = '587'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = to
    msg['CC'] = cc
    msg['BCC'] = bcc
    msg.attach(MIMEText(body, 'html'))
    
    for f in files or []:
        with open(f, "rb") as file:
            part = MIMEApplication(file.read(), Name=basename(f))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    try:
        with smtplib.SMTP(server, port) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(username, passwd)
            smtp.sendmail(username, to, msg.as_string())
            logger.info("Sent unattended email")
            smtp.quit()
    except Exception as e:
        logger.critical("Failed to send unattended mail")
        logger.critical(e, exc_info=True)

logger.debug("-------Finished Execution-------")