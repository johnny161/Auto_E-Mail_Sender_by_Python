import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr

my_sender = 'xiexj6@mail2.sysu.edu.cn'    # 发件人邮箱账号
my_pass = 'ovAgy9838gAgW9F2'              # 16位发件人邮箱授权码，非登录密码
my_user = ''      # 收件人邮箱账号，我这边发送给自己

# 构建正文
mail_msg = """
<p>
    您好：
    <br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DCABES2020即将举办，特此向您发出投稿邀请，会议网址为<a href="http://dcabes2020.jiangnan.edu.cn">http://dcabes2020.jiangnan.edu.cn</a> 详情请见附件《征稿通知》。
</p>
"""

# 构造一个邮件体：
msg = MIMEMultipart()
msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))
msg['From'] = formataddr(["dcabes2020", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
msg['Subject'] = "第十九届“分布式计算及其应用”国际研讨会"  # 邮件的主题，也可以说是标题

# 构造附件
file = "./Dcabes2020.7z"
part_attach = MIMEApplication(open(file, 'rb').read())  # 打开附件
part_attach.add_header('Content-Disposition', 'attachment', filename=file)  # 为附件命名
msg.attach(part_attach)

server = smtplib.SMTP("smtp.exmail.qq.com", 25)  # 服务端配置
server.login(my_sender, my_pass)  # 登陆服务器


def mail(my_user):
    ret=True
    msg['To'] = my_user  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    try:
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 发送邮件:括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret


# 读邮箱列表
users = []
with open('email.txt', 'r') as f:
    for line in f:
        users.append(line.strip('\n').split(','))

success = 0
for user in users:
    print(user[0], end='') # 先打印邮箱进行测试
    ret = mail(user[0])
    if ret:
        success += 1
        print(" 邮件发送成功")
    else:
        print(" 邮件发送失败")

print("总邮件数：", len(users))
print("成功发送：", success)
server.quit()  # 关闭连接