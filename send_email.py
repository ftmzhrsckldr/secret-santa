from numpy.random import default_rng
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import sys
import csv


SMTP_MAIL = "smtp.gmail.com"
SMTP_PORT = 587
sender_email = "sender@mail.com"
password = input("Type your password and press enter: ")

csv_filename = 'sample_people_info.csv'
mail_subj = "CompanyName Secret Santa"


def send_mail(sender_email, from_password, receiver_mail, subject, person):
    try:
        mail = smtplib.SMTP(SMTP_MAIL, SMTP_PORT)
        mail.starttls()
        mail.login(sender_email, from_password)
        mail_msg = MIMEMultipart()
        mail_msg["From"] = sender_email
        mail_msg["To"] = receiver_mail
        mail_msg["Subject"] = subject

        mail_body = get_mail_body(
            person['name'], person['address'], person['tel'])

        body_text = MIMEText(mail_body, "html")
        mail_msg.attach(body_text)

        mail.sendmail(mail_msg["From"], mail_msg["To"], mail_msg.as_string())
        mail.close()

    except:
        print("Hata:", sys.exc_info()[0])


def get_mail_body(name, address, tel):

    with open('mail_body.html', 'r') as file:
        mail_body = file.read()

    mail_body = mail_body.replace('person_name', name)
    mail_body = mail_body.replace('person_address', address)
    mail_body = mail_body.replace('person_tel', tel)

    return mail_body


people = []
with open(csv_filename) as f:
    reader = csv.DictReader(f)
    people = list(reader)

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

    send_mail(sender_email, password,
              f"{recPerson['email']}", mail_subj, person)
    print(f"Mail was sent to: {recPerson['email']}")
