
import smtplib
import time

# Read sender email info
file_reader = open("sender.txt", "r")
me_email = file_reader.read()

# Read sender password
file_reader = open("password.txt", "r")
me_password = file_reader.read()

# Read email recipients as array
file_reader = open("recipients.txt", "r")
file_length = file_reader.readlines()

rec_emails = []

for i in file_length:
    rec_emails.append(i)
    
text_subject = "Cuts hurt kids"
text_message = "Please do not cut teachers and education for Ontario. We as students are fighting for the employment and rights of our teachers. Cuts hurt kids."
    
message = 'Subject: {}\n\n{}'.format(text_subject, text_message)

email_count = 0

while (True):
    
    # Iterate through recipient list and send an email to each address
    for k in range(0, len(rec_emails)):

        print("Iterating...")        
        send_email = rec_emails[k]
        
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpObj.starttls()

        smtpObj.login(me_email,me_password)
        smtpObj.sendmail(me_email,send_email,message)
        smtpObj.quit()   
    
        email_count += 1
    
        print(email_count)
        print("Message sent!")
    
        #time.sleep() # change rate of fire here