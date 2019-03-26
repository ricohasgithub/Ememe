import smtplib

me_email = ""
send_email = ""

me_password = ""

message = ""

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()

smtpObj.login(me_email,me_password)
smtpObj.sendmail(me_email,send_email,message)
smtpObj.quit()