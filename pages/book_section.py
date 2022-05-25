from pages.base_page import BasePage
from pages.locators import BookPageLocators
from pages.functions import scroll_shim
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookSection(BasePage):

    def click_book_this_room(self):
        self.driver.find_element(*BookPageLocators.BOOK_ROOM_BUTTON).click()

    def enter_firstname(self, name):
        self.driver.find_element(*BookPageLocators.FIRST_NAME).send_keys(name)

    def enter_lastName(self, lastName):
        self.driver.find_element(*BookPageLocators.LAST_NAME).send_keys(lastName)

    def enter_email(self, email):
        self.driver.find_element(*BookPageLocators.ROOM_EMAIL).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*BookPageLocators.ROOM_PHONE).send_keys(phone)

    def enter_date(self):
        start_date = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(BookPageLocators.START_DATE))
        end_date = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(BookPageLocators.END_DATE))
        scroll_shim(self.driver, start_date)
        sleep(2)
        action = ActionChains(self.driver)
        action.drag_and_drop(start_date, end_date).perform()

    def click_book_button(self):
        self.driver.find_element(*BookPageLocators.BOOK_BUTTON).click()


