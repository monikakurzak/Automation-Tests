from selenium import webdriver
import unittest
from pages.book_section import BookSection
from pages.contact_section import ContactSection


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://automationintesting.online/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.book_section = BookSection(self.driver)
        self.contact_section = ContactSection(self.driver)

    def tearDown(self):
        self.driver.quit()
