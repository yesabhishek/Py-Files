## -*- coding: utf-8 -*-
#"""
#Created on Tue Feb 25 18:10:13 2020
#
#@author: achoud3
#"""
#
#import urllib.request
#import re
#page = urllib.request.urlopen("https://www.google.com/").read().decode('utf-8')
#
## => via regular expression
#
#answer=re.findall("Google", page)
##['Shopping']
#
## => via string.find, returns the position ...
#page.find("Google")
#
#


#import urllib.request
#with urllib.request.urlopen('https://www.google.com/') as response:
#   html = response.read()
#   type(html)
#   html.find("Google")
#   

#import requests
#from bs4 import BeautifulSoup
# 
#def count_words(url, the_word):
#    r = requests.get(url, allow_redirects=False)
#    soup = BeautifulSoup(r.content, 'lxml')
#    words = soup.find(text=lambda text: text and the_word in text)
#    
#    print(words)
#    return len(words)
# 
# 
#def main():
#    url = 'https://www.google.com/'
#    word = 'Privacy'
#    count = count_words(url, word)
#    print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, word))
# 
#if __name__ == '__main__':
#    main()
#




#from bs4 import BeautifulSoup
#
#from urllib.request import urlopen
#url = urlopen("http://www.python.org")
#
#content = url.read().decode('utf-8')
#
#soup = BeautifulSoup(content,features="lxml")
#
#links = soup.findall("a")



#from bs4 import BeautifulSoup
#import re
#from urllib.request import urlopen
##html = '''\
##<p>Hello world and and python</p>
##<td>python is a good language</td>
##<td>not present in this text</td>
##<div>Hello from python</div>'''
# 
#url = urlopen("https://www.google.com/")
#
#content = url.read().decode('utf-8')
#
#soup = BeautifulSoup(url, 'lxml')
#the_word = 'Google'
#tags_found = soup.find_all(re.compile(".*"), text=lambda text: text and the_word in text)
#print(tags_found)
#print('-' * 15)
#print([s.text for s in tags_found])

from bs4 import BeautifulSoup

from urllib.request import urlopen 
url =urlopen("https://www.google.com/")

content = url.read()

soup = BeautifulSoup(content,features="lxml")

links = soup.find_all('div', 'Settings')
#for div in links:
#    if "class" in div:
#        if (div["class"]=="Google"):
#            print("yes")

print(links)

