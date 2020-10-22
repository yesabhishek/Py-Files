# importing libraries 
from bs4 import BeautifulSoup as BS 
import requests 

source = requests.get('https://www.moneycontrol.com/commodity/gold-price.html').text
soup = BS(source,'lxml')


title = soup.find('h1',class_='FL')
date = soup.find('div', class_= 'gre12')
price = soup.find('div', class_= 'FL brdr PR20 rd_13')

print(title.text,",",date.text)
print(price.text)

