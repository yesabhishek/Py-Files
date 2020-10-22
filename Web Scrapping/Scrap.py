# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import pandas as pd


with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml') 

    
""" print(soup.prettify) """

""" match = soup.title.text """
""" match = soup.find('div', class_='footer').text
    print(match) """

""" 
article = soup.find('div',class_='article')
title = article.h2.text
summary = article.text
 """
""" 
table = soup.table
table_rows = soup.find_all('tr') """
#print(table_rows)

#print(title,summary)

""" for tr in table_rows:
    td = tr.find_all('td')
    row = [ i.text for i in td ]
    print(row)
 """


dfs = pd.read_html('simple.html')
for df in dfs:
    print(df)
