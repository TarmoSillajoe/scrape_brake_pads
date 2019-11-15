from trw_scraper import TrwScraper
import csv
import pandas as pd
import requests

#GDB5008
scraper = TrwScraper()

scraped_data = []

df_parts = pd.read_csv('part_numbers.csv')
print(df_parts.columns)

for product in df_parts['part_number'].unique():
    product_data = scraper.scrape_product_data(product)
    scraped_data += product_data


df = pd.DataFrame(scraped_data)
df.to_csv('C:/Users/tarmos/Downloads/trw.csv', sep='\t', index=False)
