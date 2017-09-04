import bs4 as bs
import urllib.request
import pandas as pd

# sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce, 'lxml')

'''
print(soup)  # soup will give a nicely arranged html (clean)
print(sauce) # sauce will add a ton of tabs and newlines (not clean)
'''

# print("Testing html element TITLE")
# print("--------------------------")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string) # = print(soup.title.text)
# print("")
#
#
# print("Print first paragraph element")
# print("-----------------------------")
# print(soup.p)
# print("")
#
# print("Print all paragraph elements")
# print("----------------------------")
# print(soup.find_all('p'))
# print("")
#
#
# print("Print all paragraph elements with FOR loop")
# print("------------------------------------------")
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)
# print("")
#
# print("Getting all the text")
# print("--------------------")
# print(soup.get_text())
# print("")
#
# print("Finding all the links")
# print("---------------------")
# for url in soup.find_all('a'):
#     print(url.get('href'))
# print("")

# print("Finding all the nav's")
# print("---------------------")
# nav = soup.nav
# print(nav)
# print("")
#
#
# print("Finding all the nav's links")
# print("---------------------------")
# for url in nav.find_all('a'):
#     print(url.get('href'))
# print("")
#
# print("Getting the body text")
# print("---------------------")
# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)
# print("")
#
#
# print("Getting the text of multiple tags")
# print("---------------------------------")
# for div in soup.find_all('div' , class_='body'):
#     print(div.text)
# print("")


# print("Working with table")
# print("------------------")
# # possible ways of retrieving the table :
# table = soup.table
# table = soup.find('table')
#
# table_rows = table.find_all('tr')
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)

# print("Pandas listing all the dataframes")
# print("---------------------------------")
# dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/' , header=0)
# for df in dfs:
#     print(df)

# sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
# soup = bs.BeautifulSoup(sauce, 'xml')
#
# print("Sitemaps (maps of all urls of page)")
# print("-----------------------------------")
# for url in soup.find_all('loc'):
#     print(url.text)

# scrape dynamically changing content of website
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface')
soup = bs.BeautifulSoup(sauce, 'lxml')
js_test = soup.find('p' , class_='jstest')
print(js_test.text)
