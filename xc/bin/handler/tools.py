import smtplib
import traceback
from constant import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 


def send_email_v2(subject, content, to):
     msg = MIMEMultipart()
     msg_content = MIMEText(content, _subtype='plain', _charset='utf-8')
     msg.attach(msg_content)

     msg['to'] = to
     msg['from'] = SENDER_EMAIL_ADDR
     msg['subject'] = subject
     try:
         server = smtplib.SMTP(timeout=SENDER_EMAIL_TIMTOUT)
         server.connect(SENDER_HOST, SENDER_PORT)
         server.login(SENDER, SENDER_PASS)
         server.sendmail(msg['from'], to, msg.as_string())
         server.quit()
         print 'success send'
         return True
     except Exception, e:
         print traceback.format_exc()
         print 'fail send'
         return False
