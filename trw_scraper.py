from selenium.webdriver import Firefox, FirefoxOptions
from pathlib import Path


webdriver= Path.cwd() / "driver" / "geckodriver.exe"
options = FirefoxOptions()
options.headless = True

driver = Firefox(options=options, executable_path=webdriver)

PRODUCT_NUMBER = 'GDB5019'
url = f"https://www.trwaftermarket.com/en/catalogue/product/{PRODUCT_NUMBER}/"
driver.get(url)
# product_details_link = driver.find_element_by_xpath('*[@id="catalogue-search-results"]/div[contains(@class, "product-details")]/a[contains(@href, "en/catalogue/product/GDB5005/")]')
# product_details_link.click()
oe_refs = driver.find_element_by_xpath('//*[@id="tabs"]//a[text()="OE Numbers & Linked Vehicles"]')
oe_refs.click()

driver.find_element_by_xpath('//div[@id="oe-numbers-accordion"]/h3').click()
oe_table= driver.find_element_by_xpath('//div[@id="oe-numbers-accordion"]//table[@class="responsive"]')
oe_table_rows = oe_table.find_elements_by_tag_name('tr')

oe_list = []
for row in oe_table_rows[1:]:
    oe_dict = {'product_number': PRODUCT_NUMBER}
    
    oe_dict['make'] = row.find_element_by_xpath('td[1]').text
    oe_dict['oe_number'] = row.find_element_by_xpath('td[2]').text
    oe_list.append(oe_dict)

print(oe_list)

driver.close()