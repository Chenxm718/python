#!/usr/bin/env python
# coding: UTF-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['from'] = 'xxxx@163.com'
msg['to'] = 'xxx@mtime.com'
msg['subject'] = 'python sub'
content = ''''' 
    你好， 
            这是一封自动发送的邮件。 

        www.ustchacker.com 
'''
txt = MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('xx@163.com', 'pwd')
smtp.sendmail('xxxx@163.com', 'xxxx@mtime.com', str(msg))
smtp.quit()
