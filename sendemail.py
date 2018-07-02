# sends email using gmail, outlook (you have to type in the full smtp server yourself)
# list of smtp smtp servers:
# google: smtp.gmail.com
# outlook: smtp.live.com
# office365: smtp.office365.com
# yahoo: smtp.mail.yahoo.com
# check this link for more: https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html
# please turn off your less secure apps blocker!
# no subject lines yet

import smtplib
import getpass

def message():
    check = 1
    while True:
        print("Enter your message (if finished press enter): ")
        try:
            line = input()
        except EOFError:
            break

        if check == 1:
            total = line + " "
            check = 0
        else:
            total = total + line + " "

        if not line:
            return total
            break

smtpserver = input("Enter your email server: ")
port = input("Enter port number for server: ")
user = input("Enter your username: ")
password = getpass.getpass()
target = input("Enter the email address you want to send your message to: ")


while True:
    msg = message()
    print(msg)
    co = input("If message is true, type in yes: ")

    if co == "yes":
        server = smtplib.SMTP(smtpserver, port)
        server.connect(smtpserver, port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, target, msg)
        break

print("Email sent!")
server.quit()
