import unittest
from selenium.webdriver import Firefox, FirefoxOptions
from pathlib import Path
import requests

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TrwScraper():
    BASE_URL =  "https://www.trwaftermarket.com/en/catalogue/product/"
    DRIVER_PATH = Path.cwd() / "driver" / "geckodriver.exe"

    def __init__(self):

        options = FirefoxOptions()
        options.headless = True
        self.driver = Firefox(executable_path = self.DRIVER_PATH, options=options)
                #,options=options

        #self.driver.maximize_window()

    
    def scrape_product_data(self, product_number):
        print(f'scraping {product_number}')
        url = f"https://www.trwaftermarket.com/en/catalogue/product/{product_number}/"

        oe_list = []
        if not self.page_exists(url): return [{'product_number':product_number ,'make':None, 'oe_number':None}]

        self.driver.get(url)
        self.driver.implicitly_wait(20)

        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabs"]//a[text()="OE Numbers & Linked Vehicles"]'))).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="oe-numbers-accordion"]//h3'))).click()
        oe_table= self.driver.find_element_by_xpath('//div[@id="oe-numbers-accordion"]//table[@class="responsive"]')
        oe_table_rows = oe_table.find_elements_by_tag_name('tr')


        if len(oe_table_rows) < 2: return [{'product_number':product_number ,'make':None, 'oe_number':None}]

        for row in oe_table_rows[1:]:
            oe_dict = {'product_number': product_number, 'make':None, 'oe_number':None}  
            oe_dict['make'] = row.find_element_by_xpath('td[1]').text
            oe_dict['oe_number'] = row.find_element_by_xpath('td[2]').text

            oe_list.append(oe_dict)

        return oe_list


    def page_exists(self, url):
        request = requests.get(url, allow_redirects=False)  
        if request.status_code == 200: return True
        return False


    def __del__(self):
        self.driver.close()
        print('Job done')