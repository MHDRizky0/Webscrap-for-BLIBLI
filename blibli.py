import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas as pd# specify the url

def product_search(keyword):
  url = ('https://www.blibli.com/backend/search/products?page=1&start=0&searchTerm={}&intent=true&merchantSearch=true&multiCategory=true&customUrl=&sort=0&category=AN-1000001&category=HA-1000002&channelId=web&showFacet=true').format(keyword)

  #Setting for Headless Browser
  options=Options()
  options.headless= True 
  driver = webdriver.Firefox(options=options)
  print('Browser Initialize: retrieving data, wait for a moment')

  driver.get(url) #Accessing Web
  html = driver.page_source # Get HTML

  #Converting HTML into Json
  soup = BeautifulSoup(html, 'lxml')
  for p in soup.find_all("div", {"id": "json"}):
    page_json = p.get_text()
    data = json.loads(page_json)

  #Get selected data
  data_barang = pd.DataFrame()
  for post in data['data']['products']:
    brand = post['brand'].upper()
    product_name = post['name']
    disc_price = post['price']['minPrice']
    discoutn = str(post['price']['discount']) + '%'
    rating = post['review']['rating']
    reviewer = post['review']['count']
    data_barang = data_barang.append({'Brand':brand, 'Product Name':product_name, 'Price':disc_price, 'Discount':discoutn, 'Rating':rating, 'Reviewer':reviewer}, ignore_index=True)
  data_barang.to_csv('data_smartphone.csv', mode='a', index=False, header=False) #Convert into csv file

  #Closing Headless Browser in 5 Second
  time.sleep(5)
  driver.quit()
  
  print(data_barang)

keyword = input("Type the keyword you want to search: ")
product_search(keyword)