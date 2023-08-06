import imaplib
import smtplib
from datetime import date, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Config:
    def __init__(self, report_email: str, email_password: str):
        try:
            self.__mailConnection = imaplib.IMAP4_SSL('imap.gmail.com', 993)
            self.__mailConnection.login(report_email, email_password)
        except Exception as e:
            raise e

    def is_mail_present(self, subject: str, look_back_period: int = 0):
        try:
            self.__mailConnection.select("Inbox")
            look_back_date = date.today() - timedelta(days=look_back_period)
            look_back_date = look_back_date.strftime('%d-%b-%Y')
            typ, msgs = self.__mailConnection.search(None, '(SINCE "' + look_back_date + '" SUBJECT ' + subject + ')')
            msgs1 = msgs[0].split()
            if len(msgs1) > 0:
                return True
            else:
                return False
        except Exception as e:
            raise e


def send_email(user_name: str, password: str, subject: str, msg_body: str, recipient_list: str):
    try:
        msg = MIMEMultipart('alternative')
        date_time_obj = date.today()
        rec = ', '.join(recipient_list)
        msg['Subject'] = subject + " " + str(date_time_obj)
        msg['From'] = user_name
        msg['To'] = rec
        part2 = MIMEText(msg_body, 'html')
        msg.attach(part2)
        mail_service = smtplib.SMTP('smtp.gmail.com', 587)
        mail_service.starttls()
        mail_service.login(user_name, password)
        mail_service.send_message(msg)
        mail_service.quit()
        return 'Success'
    except Exception as e:
        print(f"Exception occurred while sending email.\n{e}")
        return 'Failed'
