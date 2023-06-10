#!/usr/bin/env python
# encoding: utf-8
# 使用import导入smtplib模块
import smtplib
# 使用from...import导入邮件协议的协议头模块
from email.header import Header
# 使用from...import导入邮件正文内容数据处理模块
from email.mime.text import MIMEText
# 使用from...import导入邮件发送多种形式内容模块
from email.mime.multipart import MIMEMultipart

# 使用with...as语句配合open()函数，以二进制只读"rb"打开文件，赋值给food_file
# 文件路径"/Users/yequ/美食排行.xlsx"
with open("/Users/yequ/美食排行.xlsx", "rb") as food_file:
    # 使用read()函数读取信息，赋值给food_content
    food_content = food_file.read()
# 使用MIMEText()函数，传入要发的附件food_content，设置邮件的编码为base64, 设置附件的内容编码为gb2312，赋值给att1
att1 = MIMEText(food_content, "base64", "gb2312")
# 设置附件的["Content-Type"]内容类型为application/octet-stream表示附件
att1["Content-Type"] = "application/octet-stream"
# 调用add_header()添加"Content-Disposition"，并设置"attachment"表示附件
# 设置附件名字为"美食排行.xlsx"
att1.add_header("Content-Disposition", "attachment", filename="美食排行.xlsx")

# 使用with...as语句配合open()函数，以二进制只读"rb"打开文件，赋值给view_file
# 文件路径"/Users/yequ/城市景点.xlsx"
with open("/Users/城市景点.xlsx", "rb") as view_file:
    # 使用read()函数读取信息，赋值给view_content
    view_content = view_file.read()
# 使用MIMEText()函数，传入要发的附件view_content，设置邮件的编码为base64, 设置附件的内容编码为gb2312，赋值给att2
att2 = MIMEText(view_content, "base64", "gb2312")
# 设置附件的["Content-Type"]内容类型为application/octet-stream表示附件
att2["Content-Type"] = "application/octet-stream"
# 调用add_header()添加"Content-Disposition"，并设置"attachment"表示附件
# 设置附件名字为"城市景点.xlsx"
att2.add_header("Content-Disposition", "attachment", filename="城市景点.xlsx")

# 使用MIMEMultipart()创建实例，用于构造附件，并赋值给message
message = MIMEMultipart()
# 使用attach()将附件att1设置到邮件内容里
message.attach(att1)
# 使用attach()将附件att2设置到邮件内容里
message.attach(att2)

# 邮箱服务器设置，赋值给mailHost
mailHost = "smtp地址"
# 邮箱账号设置，赋值给mailUser
mailUser = "发件人地址"
# 邮箱授权码设置，赋值给mailPass
mailPass = "此处为邮箱密码或者邮箱授权码"

# 使用smtplib.SMTP_SSL(服务器, 端口号),端口号为465，赋值给smtpObj
smtpObj = smtplib.SMTP_SSL(mailHost, 465)
# 使用login()函数传入邮箱账户和授权码，登录邮箱
smtpObj.login(mailUser, mailPass)

# 定义一个字典mail_dict={}
mail_dict = {"用户A": "此处为邮箱地址", "用户B": "此处为邮箱地址"}
# 使用items()函数将字典转成可遍历的列表，赋值给mail_list
mail_list = mail_dict.items()
# 使用for循环遍历列表中的每一项
for key, value in mail_list:
    # 使用MIMEText()设置邮件正文，赋值给mail_content
    mail_content = MIMEText(f"{key}同学，附件是今日北京和上海美食和景点信息，请查收！", "plain", "utf-8")
    # 使用格式化设置邮件发件人名称
    message['From'] = Header(f"发件人<{mailUser}>")
    # 使用格式化设置邮件收件人名称
    message['To'] = Header(f"{key}同学<{value}>")
    # 设置邮件主题 北京和上海旅游信息汇总
    message['Subject'] = Header("北京和上海旅游信息汇总")

    # 使用message.attach()函数上传邮件正文
    message.attach(mail_content)
    # 使用sendmail(发送人，收件人，message.as_string())发邮件
    smtpObj.sendmail(mailUser, value, message.as_string())
    # 获取姓名格式化输出"xx的邮件发送成功"
    print(f"{key}的邮件发送成功")
