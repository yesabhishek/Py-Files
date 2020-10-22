from bs4 import BeautifulSoup
import requests

""" source = requests.get('https://en.wikipedia.org/wiki/Mahatma_Gandhi').text

soup = BeautifulSoup(source,'lxml')

#print(soup.prettify)

article = soup.find('div',class_='mw-parser-output')
title = article.h3.span.text
summary = article.text

print(title)  """



#print(soup.prettify)


""" title = soup.find('div', class_='label-counter')
print(title.text,"\n") """ 


""" source = requests.get('https://en.wikipedia.org/wiki/Mahatma_Gandhi').text

soup = BeautifulSoup(source,'lxml')
updated = soup.find('div', class_='content-inner')
print(updated)

 """

Total_cases = soup.find('div',class_='maincounter-number')
summary = Total_cases.text

print("Total Cases all over the World",summary) 

