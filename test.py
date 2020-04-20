"""
Sanity check for webdriver
"""

import unittest
from selenium import webdriver

class TestTemplate(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_google_search_divs(self):
        try:
            self.driver.get('https://www.google.com/')
            divs = self.driver.find_elements_by_tag_name('div')
            if (len(divs)==0):
                self.fail('No divs found!')
        except Exception as ex:
            self.fail(ex)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)