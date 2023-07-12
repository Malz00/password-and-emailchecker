import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'malcolm malz'
email['to'] = 'malcolmibrahim31@gmail.com'
email['subject']='you are really studying keep up the work'

email.set_content(html.substitute({'name':'diza',}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=25) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('malcolm1ibrahim@gmail.com', 'ivfwyqwkggimgsvn')
    smtp.send_message(email)
    print('all good boss')


