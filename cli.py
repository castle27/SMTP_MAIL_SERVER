import smtplib
import email.utils
from email.mime.text import MIMEText
import sys



# Create the message

msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', 'recipient@example.com'))


print "abcd"
msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
msg['Subject'] = 'Simple test message'
print "1"


server = smtplib.SMTP("127.0.0.1", 1025)
server.set_debuglevel(True) # show communication with the server
try:
    server.sendmail('author@example.com', ['recipient@example.com'], msg.as_string())
finally:
    server.quit()
