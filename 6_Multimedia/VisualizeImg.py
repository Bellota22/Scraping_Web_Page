import requests
from bs4 import BeautifulSoup
from IPython.display import Image # Para poder visualizar imagenes en py

url = 'https://www.pagina12.com.ar'
p12 = requests.get(url)

s = BeautifulSoup(p12.text, 'lxml')

nav_sections = s.find( 'ul', attrs = {'class': 'main-sections'}).find_all('li')
nav_sections_urls = [nav_sections[i].a.get('href') for i in range(len(nav_sections))]


def get_links_from_sections(section):

    sec = requests.get(section)
    s_sec = BeautifulSoup(sec.text, 'lxml')

    try:
        art_principal = s_sec.find('div', attrs = {'class':'article-item__content' }).find('a')
        art_principal_url = url + art_principal.get('href')
    except Exception as e:
        print('This happen:\n')
        print(e)

    try:
        art_secondary = s_sec.find_all('h3', attrs = {'class':'h2'})
        art_secondary_urls = [ url + art_secondary[i].a.get('href') for i in range(len(art_secondary))] 
    except Exception as e:
        print('This happen:\n')
        print(e)

    try: 
        art_terciary = s_sec.find_all('h4', attrs = {'class':'h2'})
        art_terciary_urls = [ url + art_terciary[i].a.get('href') for i in range(len(art_terciary))]
    except Exception as e:
        print('This happen:\n')
        print(e)

    urls_section =[]
    urls_section.append(art_principal_url)
    urls_section.extend(art_secondary_urls)
    urls_section.extend(art_terciary_urls)

    return urls_section

url_notas = get_links_from_sections(nav_sections_urls[0])

url_first_note = url_notas[0]
# print(url_notas[0])

try:
    nota = requests.get(url_first_note)
    if nota.status_code == 200:
        s_nota = BeautifulSoup(nota.text, 'lxml')
        # Extraemos el titulo
        titulo = s_nota.find('div', attrs = {'class': 'col 2-col'}).find('h1')
        # print(titulo.text)
        fecha = s_nota.find('time').get('datetime')
        # print(fecha)
        volanta = s_nota.find('h3', attrs = {'class':'h4'}).text
        # print(volanta)
        cuerpo = s_nota.find('div', attrs = {'class':'article-text'}).find_all('p')
        articulo_text = ''
        for texto in cuerpo:
            articulo_text += texto.text
        print(articulo_text)
except Exception as e:
    print('Error')
    print(e)


# Extracting the image
def extracting_img_from_note(note):
    try:
        img = requests.get(note)

        if img.status_code == 200:
            s_img = BeautifulSoup(img.text,'lxml')

            imagen = s_img.find('div', attrs= {'class':'image-wrapper'}).find('img')
        
            imagen_url = imagen.get('src')

            imagen_py = requests.get(imagen_url)

            Image(imagen_py.content) # Para poder mostrar desde consola
            
            return imagen_url
           
    except Exception as e:
        print('Error manito \n')
        print(e)





# urls_all_section = []

# for i in range(len(nav_sections_urls)):

#     links = get_links_from_sections(nav_sections_urls[i])
#     urls_all_section.extend(links)

# print(urls_all_section)


