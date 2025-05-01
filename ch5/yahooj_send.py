import smtplib, ssl
from email.mime.text import MIMEText
import my_yahooj_account as yahooj


def send_test_email():
    msg = make_mime_text(
        mail_to = yahooj.account,
        subject = 'メールの送信テスト',
        body = 'こんにちは、メッセージは届きましたか？')
    send_yahooj_mail(msg)


def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, 'plain')
    msg['Subject'] = subject
    msg['To'] = mail_to
    msg['From'] = yahooj.account
    return msg

def send_yahooj_mail(msg):
    server = smtplib.SMTP_SSL(
        'smtp.mail.yahoo.co.jp',465,
        context = ssl.create_default_context())
    server.login(
        yahooj.account,
        yahooj.password
    )
    server.send_message(msg)

if __name__ == '__main__':
    send_test_email()
    print('ok.')