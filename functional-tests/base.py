import sys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                cls.is_live_server_test = True
                break
        else:
            cls.is_live_server_test = False
            super(FunctionalTest, cls).setUpClass()
            cls.server_url = cls.live_server_url
        
    @classmethod
    def tearDownClass(cls):
        if not cls.is_live_server_test:
            super(FunctionalTest, cls).tearDownClass()
    
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')
