# Python
常用python脚本
前言：

导入库

import smtplib
from smtplib import SMTP_SSL            # 用于加密邮件内容 防止中途被人截获
from email.mime.text import MIMEText    # 用于构造邮件的正文
from email.mime.image import MIMEImage # 用于发送正文带图片的邮件
from email.mime.multipart import MIMEMultipart     # 把邮件的各个部分装在一起 是邮件的主题
from email.header import Header                    # 邮件头（包括邮件标题 收件人）
from email.mime.application import MIMEApplication # 用于发送附件

为python自带库：

构建邮件是需要指定邮箱smtp服务器地址：
host_server = 'smtp.qq.com'       #qq邮箱的smtp服务器地址 端口465下方登录时填写
sender_sina = '***@qq.com'  #为发件人邮箱
pwd = 'bryatscojpvpbcec'          #邮箱授权码 不是密码

构建邮件时 需要有发件人 收件人 邮箱标题 邮箱正文内容
#构造一封邮件的时候需要先填写发件人和收件人
sender_sina_mail = '***@qq.com'                           # 发件人邮箱
receiver = ['***@qq.com'],['***@qq.com']          # 收件人邮箱 （可以写成一样的）
mail_title = 'python自动化办公'                                  # 邮箱标题
mail_content = '你好， 这是使用python登录 qq邮箱的测试:https://www.python.org'  # 邮件的正文内容

构建邮件时需要初始化邮件主体 将基础信息填入 邮件主体
msg = MIMEMultipart()                          # 定义邮件主体
msg["Subject"] = Header(mail_title, 'utf-8')   # 使用Header将邮件标题 处理成可识别的utf-8格式 "Subject" 邮件主题
msg["From"] = sender_sina_mail                 # 寄件人
msg["To"] = Header("测试邮箱", 'utf-8')                #  收件人 自定义
msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))  # 邮件正文内容以无格式添加进整个邮件的主体

msg["Subject"] ： 邮件主题
msg["From"]    ： 寄件人邮件来自哪儿
msg["To"]      ：收件人自定义 
msg.attach(MIMEText（）） ：邮件正文


smtp库构建完成主题后登录邮箱发送
#登录邮箱服务器
smtp = SMTP_SSL(host_server, 465)   # SSL登录
smtp.login(sender_sina, pwd)        # 发件人密码登录
smtp.sendmail(sender_sina_mail, receiver, msg.as_string()) # 发件人收件人 以及邮件的主体
smtp.quit() #退出邮箱

SMTP_SSL()        :  SSL方式登录       
smtp.login()    : 发件人密码登录
smtp.sendmail()  : 发送邮件
smtp.quit()     ：退出邮箱

注：此时发送普通邮件结束

MIMEApplication库附件部分：

'''
附件部分
Content-Disposition() 内容设置 设置的内容attachmen 附件  filename给它重命名
'''
attachment = MIMEApplication(open('./py测试目录/客户1-价格通知.docx', 'rb').read())         # 打开附件 rb  r-read b-以二进制打开文件 不加则以字符串打开
attachment.add_header('Content-Disposition', 'attachment', filename='客户1-价格通知.docx') # 给附件改名字
msg.attach(attachment)  #添加附件

###此时完成附件添加###


mail_content = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
<p>图片演示：</p>
<p><img decoding="async" src="cid:image1"></p>
"""  # 邮件的html正文内容

'''
发送正文带图片的邮件
'''
# 指定图片为当前目录
fp = open('1.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close() 

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

###此时完成附件添加###
