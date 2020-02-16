## Auto_E-Mail_Sender-by-Python
### Introduction
- my_pass: 
   
    + 使用腾讯的代理服务器发送需要16位发件人邮箱授权码（不同于登录密码）  
    + 对于腾讯企业邮箱，需要先绑定微信，再申请授权码 
    
- 服务端配置的两种方法：

    - server = smtplib.SMTP_SSL(smtp_server, 465) #失败，原因不明
    - server = smtplib.SMTP(smtp_server, 25) #成功

### Figure
![result](/illustration/3.png)

### Reference
- 廖雪峰python: [SMTP发送邮件](https://www.liaoxuefeng.com/wiki/897692888725344/923057144964288)
- 菜鸟教程: [Python3 SMTP发送邮件](https://www.runoob.com/python3/python3-smtp.html)
- 简书: [python 使用腾讯企业邮箱发送邮件](https://www.jianshu.com/p/d5d9e52d6d2d)

