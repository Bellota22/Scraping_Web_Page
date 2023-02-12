import requests
from bs4 import BeautifulSoup

url = 'https://www.pagina12.com.ar/'
p12 = requests.get(url)

s = BeautifulSoup(p12.text, 'lxml')

nav_sections = s.find( 'ul', attrs = {'class': 'main-sections'}).find_all('li')
nav_sections_urls = [nav_sections[i].a.get('href') for i in range(len(nav_sections))]


def get_links_from_sections(section):

    sec = requests.get(section)
    s_sec = BeautifulSoup(sec.text, 'lxml')

    try:
        art_principal = s_sec.find('div', attrs = {'class':'article-item__content' }).find('a')
        art_principal_url = section + art_principal.get('href')
    except Exception as e:
        print('This happen:\n')
        print(e)

    try:
        art_secondary = s_sec.find_all('h3', attrs = {'class':'h2'})
        art_secondary_urls = [ section + art_secondary[i].a.get('href') for i in range(len(art_secondary))] 
    except Exception as e:
        print('This happen:\n')
        print(e)

    try: 
        art_terciary = s_sec.find_all('h4', attrs = {'class':'h2'})
        art_terciary_urls = [ section + art_terciary[i].a.get('href') for i in range(len(art_terciary))]
    except Exception as e:
        print('This happen:\n')
        print(e)

    urls_el_pais =[ art_principal_url , art_secondary_urls , art_terciary_urls]

    return urls_el_pais

urls_all_section = []

for i in range(3):

    links = get_links_from_sections(nav_sections_urls[i])
    urls_all_section.append(links)

print(urls_all_section)