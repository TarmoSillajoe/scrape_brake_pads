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
# product_oe_refs_link = driver.find_element_by_link_text("OE Numbers & Linked Vehicles")
# product_oe_refs_link.click()
#driver.close()


# //*[@id="ui-id-30"]

# 'a[contains(@class, "ui-tabs-anchor")]'
# "OE Numbers & Linked Vehicles"
