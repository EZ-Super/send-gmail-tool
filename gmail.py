import smtplib #訊息物件
import email.message
account = str(input('請輸入帳號: '))
password = str(input('請輸入密碼: '))
TO = str(input("請輸入收件人帳號:"))
text = str(input("請輸入文字內容:"))
num = int(input("請輸入傳送次數:"))

msg=email.message.EmailMessage()
msg["From"]=account #寄件人
msg["To"]=TO #收件人
msg["Subject"]="=W=別裝B了" #標題
msg.set_content(text) #寄送純文字內容
server=smtplib.SMTP_SSL("smtp.gmail.com",465) #到網路上搜尋gmail smtp
server.login(account,password) #帳號密碼
x = 1
print(text + "  ->已傳送")
while (x <= num):
    x = x +1
    print( x )
    server.send_message(msg)

server.close()