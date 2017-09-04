import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

'''
print(soup)  # soup will give a nicely arranged html (clean)
print(sauce) # sauce will add a ton of tabs and newlines (not clean)
'''

print("Testing html element TITLE")
print(soup.title)
print(soup.title.name)
print(soup.title.string) # = print(soup.title.text)
