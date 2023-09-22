﻿# coding=utf-8
import time
import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题
import os


def send_mail(latest_report):
    f = open(latest_report, "rb")
    mail_content = f.read()
    f.close()
    smtpserver = "smtp.163.com"
    # 发送邮箱用户名密码
    user = "nancyrm2018@163.com"
    password = "输入自己的密码"
    # 发送和接收邮箱
    sender = "nancyrm2018@163.com"
    receivers = ["nancyrm2018@126.com", "88886666@qq.com"]
    # 发送邮件主题和内容
    subject = "API 自动化测试报告"
    # HTML邮件正文
    msg = MIMEText(mail_content, "html", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender
    msg["To"] = ",".join(receivers)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    # HELO 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("Send email start...")
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    print("Email send end!")


def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + "\\" + fn))
    print("The latest report is:" + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file
