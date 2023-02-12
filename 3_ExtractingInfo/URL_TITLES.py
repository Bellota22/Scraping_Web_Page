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

def get_links_from_section(section):

    sec = requests.get(section)
    s_sec = BeautifulSoup(sec.text, 'lxml')


    art_principal = s_sec.find('div', attrs = {'class':'article-item__content' }).find('a')
    art_principal_url = section + art_principal.get('href')
    # print (art_principal)

    art_secondary = s_sec.find_all('h3', attrs = {'class':'h2'})
    art_secondary_urls = [ section + art_secondary[i].a.get('href') for i in range(len(art_secondary))] 
    # print(art_secondary_urls)

    art_terciary = s_sec.find_all('h4', attrs = {'class':'h2'})
    art_terciary_urls = [ section + art_terciary[i].a.get('href') for i in range(len(art_terciary))]

    # print(art_terciary_urls)

    urls_el_pais =[ art_principal_url , art_secondary_urls , art_terciary_urls]

    return urls_el_pais

# print(get_links_from_section(nav_urls[2]))


urls_all_section = []

for i in range(3):

    links = get_links_from_section(nav_urls[i])
    urls_all_section.append(links)

print(urls_all_section)