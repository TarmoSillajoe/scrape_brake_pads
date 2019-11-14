from trw_scraper import TrwScraper
import csv
import pandas as pd

scraper = TrwScraper()
mylist = scraper.scrape_product_data('GDB5019')
print(mylist)
mylist += scraper.scrape_product_data('GDB5008')
print(mylist)

# scraped_data = []

# products_list = ['GDB5019']

# for product in products_list:
#     scraped_data += scraper.scrape_product_data('product')


# df = pd.DataFrame(scraped_data)
# df.to_csv('C:/Users/tarmos/Downloads/trw.csv', sep='\t')

