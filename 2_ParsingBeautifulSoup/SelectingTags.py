import requests
from bs4 import BeautifulSoup

url = 'https://www.pagina12.com.ar/'
p12 = requests.get(url)

# Call the function and select a parser 'lxml'
# Separate the large text in parts
s = BeautifulSoup(p12.text, 'lxml')

# print(s.prettify())

# find the tag (ul) with attrs {class:value}
# Then getting the names with find_all
list_nav = s.find('ul', attrs={'class':'main-sections' }).find_all('a')
print(list_nav)
# soup.find('nav', attrs={'id':'header-main-nav'})