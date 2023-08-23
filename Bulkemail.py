import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login("your email", "your email password")
subject="Error"
body = "Test Mail"
message="subject:{}\n\n{}".format(subject, body)
listadd=['person1',
         'person2'] #people you want to send the  mail to
ob.sendmail('sender email', listadd, message)
print("Email Sent")
ob.quit()