#coding: utf-8
import logging
import smtplib
from time import strftime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='Email_Task.log',
                    filemode='w')

#logging.debug('This is debug message')



sender = 'cgzx1634@163.com'
#receiver = '137746731@qq.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'cgzx1634@163.com'
password = '****************'

msgRoot = MIMEMultipart('related')
msgRoot['From'] = 'cgzx1634@163.com <cgzx1634@163.com>'
msgRoot['To'] = '1192702592@qq.com <1192702592@qq.com>'
msgRoot['Subject'] = '豆瓣租房信息更新' + str(strftime("_%Y_%m_%d"))

filename = '/Users/biwangshen/gitDocuments/douban/' + str(strftime("_%Y_%m_%d")) + ".txt"
docname = str(strftime("%Y_%m_%d")) + ".txt"
att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename=' + docname
msgRoot.attach(att)

try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', 25)
    smtp.login(username, password)
    smtp.sendmail(sender, ['1192702592@qq.com'], msgRoot.as_string())
    logging.info('Send email success')
except Exception as e:
    logging.warning('erro' + str(e))
smtp.quit()