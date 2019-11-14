from selenium.webdriver import Chrome
from pathlib import Path


webdriver= Path.cwd() / "driver" / "chromedriver.exe"
driver = Chrome(webdriver)
driver.maximize_window()

url = "https://www.trwaftermarket.com/en/catalogue/product/GDB5005/"
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
    print(row.find_element_by_xpath('td[1]').text + ' '+ row.find_element_by_xpath('td[2]').text )

driver.close()