import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login('officialrekhaid05@gmail.com', '342cs12020')

# sending the mail
s.sendmail('officialrekhaid05@gmail.com', 'hiroshi.tsutsui415@gmail.com', 'This is sent from Python with smptlib')

# terminating the session
s.quit()