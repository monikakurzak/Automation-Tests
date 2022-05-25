from tests.base_test import BaseTest
from nessesery_data import randomData, variables


class ContactTests(BaseTest):

        def testContactHappyPath(self):
                """
                TC 001 : Happy path
                """
                contact_section = self.contact_section
                random_name = randomData.name
                contact_section.enter_name(random_name)
                contact_section.enter_email(randomData.email)
                contact_section.enter_phone(randomData.phone)
                contact_section.enter_subject(randomData.subject)
                contact_section.enter_description(randomData.message)
                contact_section.click_submit()
                self.assertTrue(variables.confirmation + random_name in self.driver.page_source)

        def testContactNoNameEntered(self):
                """
                TC 002 : User does not enter name
                """
                contact_section = self.contact_section
                contact_section.enter_email(randomData.email)
                contact_section.enter_phone(randomData.phone)
                contact_section.enter_subject(randomData.subject)
                contact_section.enter_description(randomData.message)
                contact_section.click_submit()
                self.assertTrue(variables.alertNoNameEntered in self.driver.page_source)

        def testContactPhoneTooShort(self):
                """
                TC 003 : User enter too short phone number
                """
                contact_section = self.contact_section
                contact_section.enter_name(randomData.name)
                contact_section.enter_email(randomData.email)
                contact_section.enter_phone(randomData.phoneTooShort)
                contact_section.enter_subject(randomData.subject)
                contact_section.enter_description(randomData.message)
                contact_section.click_submit()
                self.assertTrue(variables.alertPhoneTooShort in self.driver.page_source)



