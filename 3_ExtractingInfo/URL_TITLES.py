import requests
from bs4 import BeautifulSoup

url = 'https://www.pagina12.com.ar'
p12 = requests.get(url)

s = BeautifulSoup(p12.text, 'lxml')

# List items
nav = s.find('ul', attrs= {'class':'main-sections'}).find_all('li')

nav_urls = [nav[i].a.get('href') for i in range(len(nav))]
# extracting the first link of the first element
# nav_url = nav[0].a.get('href')

# print(nav_urls)

nav_titles = [nav[j].a.get_text() for j in range(len(nav))]
# extracting the first title of the first element
# nav_title = nav[0].a.get_text()

# print(nav_titles)


# Doing request at the first linnk, then we need to parse again
# because we are in another webpage

sec = requests.get(nav_urls[0])
s_sec = BeautifulSoup(sec.text, 'lxml')


art_principal = s_sec.find('div', attrs= {'class':'article-item__content' }).find('a')
art_principal_url = url+art_principal.get('href')
# print (art_principal_url)

art_secondary = s_sec.find_all('h3')
print(art_secondary)
# art_secondary_url= url+art_secondary.get('href')
# print(art_secondary_url)