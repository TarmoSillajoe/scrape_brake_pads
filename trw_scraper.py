from selenium.webdriver import Chrome
from pathlib import Path

webdriver= Path.cwd() / "driver" / "chromedriver.exe"
driver = Chrome(webdriver)

url = "https://www.trwaftermarket.com/en/catalogue/product/GDB5005/"
driver.get(url)
# product_details_link = driver.find_element_by_xpath('*[@id="catalogue-search-results"]/div[contains(@class, "product-details")]/a[contains(@href, "en/catalogue/product/GDB5005/")]')
# product_details_link.click()
oe_refs = driver.find_element_by_xpath('//*[@id="tabs"]//a[text()="OE Numbers & Linked Vehicles"]')
oe_refs.click()

oe_accordion_header = driver.find_element_by_xpath('//div[@id="oe-numbers-accordion"]//h3')
oe_accordion_header.click()
