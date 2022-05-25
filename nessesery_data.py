from faker import Faker
import calendar
from datetime import date
import random

class randomData():

    fake = Faker()
    name = fake.first_name()
    lastName = fake.last_name()
    email = fake.email()
    phone = fake.msisdn()
    phoneTooShort = fake.country_calling_code()
    subject = fake.pystr(5,10)
    message = fake.pystr(20)

class variables():

    confirmation = "Thanks for getting in touch "
    alertNoNameEntered = "nie może być odstępem"
    alertPhoneTooShort = "wielkość musi należeć do zakresu od 11 do 21"
    alertNoDateEntered = "nie może mieć wartości null"
    current_year = date.today().year
    current_month = date.today().month
    month_length = calendar.monthrange(current_year, current_month)[1]
    start_day = random.randint(1, month_length - 2)
    end_day = random.randint(start_day + 1, month_length - 1)


