
import smtplib
import time

me_email = "1ZHURIC2@hdsb.ca"
send_email = "1YAOETH2@hdsb.ca"

file_reader = open("password.txt", "r")

me_password = file_reader.read()

print(me_password)

message = "zimbabwe"

email_count = 0

while (True):
    
    print("Iterating...")
    smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtpObj.starttls()

    smtpObj.login(me_email,me_password)
    smtpObj.sendmail(me_email,send_email,message)
    smtpObj.quit()   
    
    email_count += 1
    
    print(email_count)
    print("Message sent!")
    
    time.sleep(3) # change rate of fire here