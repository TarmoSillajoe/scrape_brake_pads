from trw_scraper import TrwScraper

scraper = TrwScraper()
mylist = scraper.scrape_product_data('GDB5019')
print(mylist)