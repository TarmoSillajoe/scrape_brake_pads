import unittest
from selenium.webdriver import Firefox, FirefoxOptions
from pathlib import Path

class TrwScraper(unittest.TestCase):
    BASE_URL =  "https://www.trwaftermarket.com/en/catalogue/product/"
    DRIVER_PATH = Path.cwd() / "driver" / "geckodriver.exe"

    def __init__(self):

        options = FirefoxOptions()
        #options.headless = True
       
        self.driver = Firefox(executable_path = self.DRIVER_PATH)
                #,options=options

        self.driver.maximize_window()

    
    def scrape_product_data(self, product_number):
        
        url = f"https://www.trwaftermarket.com/en/catalogue/product/{product_number}/"
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="tabs"]//a[text()="OE Numbers & Linked Vehicles"]').click()
        self.driver.find_element_by_xpath('//div[@id="oe-numbers-accordion"]/h3').click()
        oe_table= self.driver.find_element_by_xpath('//div[@id="oe-numbers-accordion"]//table[@class="responsive"]')
        oe_table_rows = oe_table.find_elements_by_tag_name('tr')

        oe_list = []
        for row in oe_table_rows[1:]:
            oe_dict = {'product_number': product_number}
    
            oe_dict['make'] = row.find_element_by_xpath('td[1]').text
            oe_dict['oe_number'] = row.find_element_by_xpath('td[2]').text
            oe_list.append(oe_dict)

        return oe_list


    def __del__(self):
        self.driver.close()
        print('Job done')