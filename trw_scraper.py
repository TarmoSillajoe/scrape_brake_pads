import unittest
from selenium.webdriver import Firefox, FirefoxOptions
from pathlib import Path


class TrwScraper():
    BASE_URL =  "https://www.trwaftermarket.com/en/catalogue/product/"
    DRIVER_PATH = Path.cwd() / "driver" / "geckodriver.exe"

    def __init__(self):

        options = FirefoxOptions()
        options.headless = True
       
        self.driver = Firefox(executable_path = self.DRIVER_PATH,options=options)
                #,options=options

        #self.driver.maximize_window()

    
    def scrape_product_data(self, product_number):
        #self.driver.maximize_window()
        url = f"https://www.trwaftermarket.com/en/catalogue/product/{product_number}/"
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="tabs"]//a[text()="OE Numbers & Linked Vehicles"]').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//div[@id="oe-numbers-accordion"]/h3').click()
        oe_table= self.driver.find_element_by_xpath('//div[@id="oe-numbers-accordion"]//table[@class="responsive"]')
        oe_table_rows = oe_table.find_elements_by_tag_name('tr')

        oe_list = []

        if len(oe_table_rows) < 2: return [{'product_number':product_number ,'make':None, 'oe_number':None}]

        for row in oe_table_rows[1:]:
            oe_dict = {'product_number': product_number, 'make':None, 'oe_number':None}  
            oe_dict['make'] = row.find_element_by_xpath('td[1]').text
            oe_dict['oe_number'] = row.find_element_by_xpath('td[2]').text

            oe_list.append(oe_dict)

        return oe_list


    def __del__(self):
        self.driver.close()
        print('Job done')