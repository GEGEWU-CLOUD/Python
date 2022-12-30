import smtplib
from smtplib import SMTP_SSL           # 用于加密邮件内容 防止中途被人截获
from email.mime.image import MIMEImage # 用于发送正文带图片的邮件
from email.mime.text import MIMEText   # 用于构造邮件的正文
from email.mime.multipart import MIMEMultipart     # 把邮件的各个部分装在一起 是邮件的主题
from email.header import Header                    # 邮件头（包括邮件标题 收件人）
from email.mime.application import MIMEApplication # 用于发送附件

host_server = 'smtp.qq.com'              # qq邮箱的smtp服务器地址 端口465下方登录时填写
sender_sina_mail = '***@qq.com'    # 发件人邮箱
receiver = ['***@qq.com'] #,['******@qq.com']  # 收件人邮箱 （可以写成一样的） 以逗号分隔可以写多个
pwd = 'bryatscojpvpbcec'                               # 邮箱授权码 不是密码


#构造一封邮件的时候需要先填写发件人和收件人
mail_title = 'python自动化办公'                                               # 邮箱标题
mail_content = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
<p>图片演示：</p>
<p><img decoding="async" src="cid:image1"></p>
"""  # 邮件的html正文内容

#初始化邮件主体
msg = MIMEMultipart()                          # 邮件主体 刚才我们已经构建了 邮件的发收 等下面只需要装入主体即可
msg["Subject"] = Header(mail_title, 'utf-8')   # 使用Header将邮件标题处理成可识别的utf-8格式 "Subject" 邮件主题
msg["From"] = sender_sina_mail                 # 寄件人
msg["To"] = Header("测试邮箱", 'utf-8')         # 显示收件人此处可自定义
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))  # 邮件正文内容以无格式添加进整个邮件的主体
'''
附件部分
Content-Disposition() 内容设置 设置的内容attachmen 附件  filename给它重命名
'''
attachment = MIMEApplication(open('./py测试目录/客户1-价格通知.docx', 'rb').read())         # 打开附件 rb  r-read b-以二进制打开文件 不加则以字符串打开
attachment.add_header('Content-Disposition', 'attachment', filename='客户1-价格通知.docx') # 给附件改名字
msg.attach(attachment)  #添加附件
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

#登录邮箱服务器并且发送邮件
try:
    smtp = SMTP_SSL(host_server, 465)   # SSL登录
    smtp.set_debuglevel(0)              # 开启smtp的dbug 关闭调试改成0 
    #smtp.ehlo(host_server, 465)        # 根服务器=打个招呼说我们要连接确定一下状态 建议加上比如Gmail就必须要有这个才能连接到smtp服务器
    smtp.login(sender_sina_mail, pwd)   # 发件人密码登录
    smtp.sendmail(sender_sina_mail, receiver, msg.as_string()) # 发件人收件人 以及邮件的主体
    smtp.quit() #退出邮箱
    print("邮件发送成功")
except smtplib.SMTPException:      #捕获smtp的异常
    print("Error: 无法发送邮件")
