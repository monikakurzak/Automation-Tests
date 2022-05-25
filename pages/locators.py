from selenium.webdriver.common.by import By
from nessesery_data import variables

class ContactPageLocators():

    #Locators used on Contact form
    SUBMIT_BUTTON = (By.ID, "submitContact")
    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    SUBJECT = (By.ID, "subject")
    DESCRIPTION = (By.ID, "description")

class BookPageLocators():

    #Locators used on Book form
    BOOK_ROOM_BUTTON = (By.XPATH, '//button[@class="btn btn-outline-primary float-right openBooking"]')
    FIRST_NAME = (By.XPATH, '//input[@class="form-control room-firstname"]')
    LAST_NAME = (By.XPATH, '//input[@class="form-control room-lastname"]')
    ROOM_EMAIL = (By.XPATH, '//input[@class="form-control room-email"]')
    ROOM_PHONE = (By.XPATH, '//input[@class="form-control room-phone"]')
    START_DATE = (By.XPATH, ("//div[contains(button,'"+str(variables.start_day)+"')]"))
    END_DATE = (By.XPATH, ("//div[contains(button,'"+str(variables.end_day)+"')]"))
    BOOKED_START_DAY = (By.XPATH, "//div[@class='col-sm-6 text-center'][contains(.,'"+str(variables.current_year)+"-"
                        +str(variables.current_month).zfill(2)+"-"+str(variables.start_day).zfill(2)+"')]")
    BOOKED_END_DAY = (By.XPATH, "//div[@class='col-sm-6 text-center'][contains(.,'"+str(variables.current_year)+"-"
                        +str(variables.current_month).zfill(2)+"-"+str(variables.end_day).zfill(2)+"')]")
    BOOK_BUTTON = (By.XPATH, '//button[@class="btn btn-outline-primary float-right book-room"]')




