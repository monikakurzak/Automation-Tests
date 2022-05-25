from pages.locators import BookPageLocators
from tests.base_test import BaseTest
from nessesery_data import randomData, variables


class BookTests(BaseTest):

        def testBookHappyPath(self):
                """
                TC 001 : Happy path
                """
                book_section = self.book_section
                book_section.click_book_this_room()
                book_section.enter_firstname(randomData.name)
                book_section.enter_lastName(randomData.lastName)
                book_section.enter_email(randomData.email)
                book_section.enter_phone(randomData.phone)
                book_section.enter_date()
                book_section.click_book_button()
                self.driver.find_element(*BookPageLocators.BOOKED_START_DAY)
                self.driver.find_element(*BookPageLocators.BOOKED_END_DAY)

        def testBookNoDate(self):
                """
                TC 002 : User does not choose date
                """
                book_section = self.book_section
                book_section.click_book_this_room()
                book_section.enter_firstname(randomData.name)
                book_section.enter_lastName(randomData.lastName)
                book_section.enter_email(randomData.email)
                book_section.enter_phone(randomData.phone)
                book_section.click_book_button()
                self.assertTrue(variables.alertNoDateEntered in self.driver.page_source)
