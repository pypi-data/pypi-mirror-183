import win32com.client as win32
import logging, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
from os import makedirs, getcwd

makedirs("./logs", exist_ok=True)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('./logs/email.log')
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.debug("-------Starting Execution-------")

def sendMailViaOutlook(subject:str, recipients:str, body:str, cc_recipients:str="", bcc_recipients:str="", attachments_path_li:list[str]=None, send:bool=True) -> None:
    """Opens an outlook instance with the given information and sends the email. Attachment path should be given as relative to the current directory"""
    try:
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.Subject = subject
        mail.To = recipients
        mail.CC = cc_recipients
        mail.BCC = bcc_recipients
        for attachment_path in attachments_path_li:
            attachment = mail.Attachments.Add(getcwd() + f"{attachment_path}")
        mail.HTMLBody = body
    except Exception as e:
        logger.critical("Failed to compose email:")
        logger.critical(e, exc_info=True)

    if send==True: 
        try:
            mail.Send()
            logger.info("Email successfully sent")
        except:
            logger.error("Failed  to send email")
    else:
        logger.info("Email not sent but got details successfully")
    

def unattended_send_email(subject:str, body:str, mail_type:str, username:str, passwd:str, to:str, cc:str="", bcc:str="", files:list[str]=None) -> None:
    """Sends an email via smtp authentication so no local application required. """
    type_mail = {
        'error':r'****ERROR**** :: ',
        'success':r'Successful run :: ',
        'warning':r'Warning/Info :: ',
        'none':r''
    }
    sub_prefix = type_mail[mail_type]

    server = 'smtp.outlook.com'
    port = '587'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = sub_prefix+subject
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