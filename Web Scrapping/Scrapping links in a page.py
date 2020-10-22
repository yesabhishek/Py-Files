from bs4 import BeautifulSoup
import requests

#url = "https://www.tutorialspoint.com/index.htm"
url = "https://www.google.com"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')

#print(soup.title)

for link in soup.find_all('a'):
    print(link.get('href'))
