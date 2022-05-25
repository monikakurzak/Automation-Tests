import unittest
from tests.test_contact import ContactTests
from tests.test_book import BookTests


tests_contact = unittest.TestLoader().loadTestsFromTestCase(ContactTests)
tests_book = unittest.TestLoader().loadTestsFromTestCase(BookTests)

tests_for_run = [
    tests_contact,
    tests_book
]

test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)