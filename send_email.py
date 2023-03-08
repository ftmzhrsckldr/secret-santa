from numpy.random import default_rng

import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
import sys
import inspect
import os
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


sender_email = "sample_sender@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test-2"
message["From"] = sender_email
message["To"] = receiver_email


SMTP_MAIL = "smtp.gmail.com"
SMTP_PORT = 587

def send_mail(from_email, from_password, to_mail, subject, mail_text):
    try:
        mail = smtplib.SMTP(SMTP_MAIL, SMTP_PORT)
        mail.ehlo()
        mail.starttls()
        mail.login(from_email, from_password)
        mesaj = MIMEMultipart()
        mesaj["From"] = from_email  # Gönderen
        mesaj["To"] = to_mail  # Alıcı
        mesaj["Subject"] = subject   # Konusu

        body = get_mail_body(mail_text)

        body_text = MIMEText(body, "html")
        mesaj.attach(body_text)

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        mail.close()

    except:
        print("Hata:", sys.exc_info()[0])


def get_mail_body(body_text):
    body = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title></title>
                    </head>
                <body> 
                    <p>{body_text}</p>
                </body>
            </html>
            """
    return body


people = [
    {
        "name": "Person 0",
        "email": "person@company.com.tr",
        "tel": "0123456789",
        "adress": "address info"
    },
    {
        "name": "Person 1",
        "email": "person1@company.com.tr",
        "tel": "0123456789",
        "adress": "address info"
    },
    {
        "name": "Person 2",
        "email": "person2@company.com.tr",
        "tel": "0123456789",
        "adress": "address info"
    },
]

COUNT_OF_PEOPLE = len(people)


def random_arr():
    rng = default_rng()
    numbers = rng.choice(COUNT_OF_PEOPLE, size=COUNT_OF_PEOPLE, replace=False)
    person = rng.choice(people, size=COUNT_OF_PEOPLE, replace=False)
    return numbers


def random_pep():
    rng = default_rng()
    person = rng.choice(people, size=COUNT_OF_PEOPLE, replace=False)
    return person


def is_same(random_nums, random_peps):
    for i in range(len(random_nums)):
        if people.index(random_peps[i]) == random_nums[i]:
            return True
    return False


random_numbers = random_arr()
random_people = random_pep()

while is_same(random_numbers, random_people):
    random_numbers = random_arr()
    random_people = random_pep()

for i in range(COUNT_OF_PEOPLE):
    person = people[list(random_numbers)[i]]
    recPerson = random_people[i]

    send_mail(sender_email, password, f"{recPerson['email']}",
              "CompanyName Secret Santa", f'''
            <div id="particles-js" class="snow"></div>
	        <div class="trees">
	        <div class="tree">
		    <img src="https://ih1.redbubble.net/image.1894189567.3099/pp,840x830-pad,1000x1000,f8f8f8.jpg" width="200px">
	        </div>
		    <div class="merry">
			<h1>Happy New Year</h1>
		    </div>
            </div>
            <pre>
            Happy New Year. The information of the lucky person you will give a gift is below: 
            ##############################################################################
                Name: {person['name']}, 
                Address: {person['adress']},
                Tel: {person['tel']}
            ##############################################################################
            <pre>
            ''')
    print(f"Mail was sent to: {recPerson['email']}")
