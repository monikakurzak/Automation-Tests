from pages.base_page import BasePage
from pages.locators import ContactPageLocators


class ContactSection(BasePage):

    def enter_name(self, name):
        self.driver.find_element(*ContactPageLocators.NAME).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*ContactPageLocators.EMAIL).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*ContactPageLocators.PHONE).send_keys(phone)

    def enter_subject(self, subject):
       self.driver.find_element(*ContactPageLocators.SUBJECT).send_keys(subject)

    def enter_description(self, message):
       self.driver.find_element(*ContactPageLocators.DESCRIPTION).send_keys(message)

    def click_submit(self):
        self.driver.find_element(*ContactPageLocators.SUBMIT_BUTTON).click()

