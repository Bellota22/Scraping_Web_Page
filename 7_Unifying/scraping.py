import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.pagina12.com.ar'
def get_url_sections(url):
    try:
        p12 = requests.get(url)
        if p12.status_code == 200:
            s = BeautifulSoup(p12.text, 'lxml')

            nav_sections = s.find('ul', attrs = {'class': 'main-sections'}).find_all('li')
            nav_sections_url = [nav_sections[i].a.get('href') for i in range(len(nav_sections))]
            return nav_sections_url
    except Exception as e:
        print("There was an error getting the url's")
        print(e)

urls_sections =get_url_sections(url)

def get_urls_notes(urls_sections):
    try:
        sec = requests.get(urls_sections)
        if sec.status_code == 200:
            s_sec = BeautifulSoup(sec.text, 'lxml')
            
            art = s_sec.find_all('div', attrs= {'class' : 'article-item__header'})
            art_urls = [url+art[i].a.get('href') for i in range(len(art))]
            return art_urls

    except Exception as e:
        print('There was an error getting the info')
        print(e)

urls_each_note = get_urls_notes(urls_sections[0])

def get_info_notes(urls_each_note):
    try:
        note = requests.get(urls_each_note)
        if note.status_code == 200:
            s_note = BeautifulSoup(note.text, 'lxml')
            info_dict = {}

            volanta = s_note.find('div', attrs= {'class': '2-col'}).find('h3')
            info_dict['volanta'] = volanta.text

            
            title = s_note.find('div', attrs= {'class': '2-col'}).find('h1')
            info_dict['title'] = title.text

            date = s_note.find('time').get('datetime')
            info_dict['date'] = date

            body = s_note.find('div', attrs= {'class' : 'article-main-content'}).find_all('p')

            body_text = ''
            for text in range(len(body)):
                body_text += body[text].text
            
            info_dict['body'] = body_text

            info_dict['url'] = urls_each_note

            img = s_note.find('div', attrs= {'class': 'image-wrapper'}).find('img').get('src')
            info_dict['image'] = img

            return info_dict

    except Exception as e:
        print('There was an error in the data extraction')
        print(e)

dict_each_note = get_info_notes(urls_each_note[0])

# print(dict_each_note)

def get_all_notes_info(url):
    try:
        urls_sections = get_url_sections(url)

        all_notes_info = []
        for section_url in urls_sections:
            urls_each_note = get_urls_notes(section_url)
            for note_url in urls_each_note:
                note_info = get_info_notes(note_url)
                all_notes_info.append(note_info)

        return all_notes_info
    except Exception as e:
        print('There was an error getting all notes information')
        print(e)

all_notes_info = get_all_notes_info(url)

df = pd.DataFrame(all_notes_info)
df.to_csv('Notas Pagina12.csv')
df.head()