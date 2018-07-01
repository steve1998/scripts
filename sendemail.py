# sends email using gmail
# please turn off your less secure apps blocker!
# no subject lines yet

import smtplib

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

user = input("Enter your gmail username: ")
password = input("Enter your gmail password: ")
target = input("Enter the email address you want to send your message to: ")


while True:
    msg = message()
    print(msg)
    co = input("If message is true, type in yes: ")

    if co == "yes":
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.connect("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, target, msg)
        break

print("Email sent!")
server.quit()
