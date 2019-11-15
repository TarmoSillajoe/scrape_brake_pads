from trw_scraper import TrwScraper
import csv
import pandas as pd


#GDB5008
scraper = TrwScraper()

scraped_data = []

products_list = [
    'GDB5019'
    ,'GDB5008'
    ,'GDB5005'
                ]

for product in products_list:
    product_data = scraper.scrape_product_data(product)
    scraped_data += product_data


df = pd.DataFrame(scraped_data)
df.to_csv('C:/Users/tarmos/Downloads/trw.csv', sep='\t', index=False)

