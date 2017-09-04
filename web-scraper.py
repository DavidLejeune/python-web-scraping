import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

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

print("Finding all the nav's")
print("---------------------")
nav = soup.nav
print(nav)
print("")
