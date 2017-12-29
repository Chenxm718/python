#!/usr/bin/env python
# coding: UTF-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:

    """
      this is send  email class

    """

    def init_smtp_obj(self):
        smtpObj = smtplib.SMTP("smtp.163.com")
        return smtpObj

    def send_email(self, from_address, to_address, context, subject, from_sub, to_sub):
        message = MIMEMultipart()
        txt = MIMEText(context)
        message.attach(txt)
        message['from'] = from_sub
        message['to'] = to_sub
        message['subject'] = subject

        try:
            smtp = self.init_smtp_obj()
            smtp.login('xxxx@163.com', 'pwd')
            smtp.sendmail(from_address, to_address, str(message))
            print("email send ok !")
            smtp.quit()
        except smtplib.SMTPException:
            raise smtplib.SMTPException

s_email = SendEmail()
s_email.send_email('xxxx@163.com', 'xxxx@mtime.com',
                   'zhong jin chi', 'subOffice', 'xxxx@163.com',
                   'xxx@mtime.com')
