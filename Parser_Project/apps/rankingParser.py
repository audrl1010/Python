import requests
from bs4 import BeautifulSoup
 
html = requests.get('http://www.melon.com/chart/index.htm'.encode('cp949')).text
soup = BeautifulSoup(html, 'html.parser')
 
tag_list = soup.select('#chartListObj tr .wrap_song_info a[href*=playSong]'.encode('cp949'))
 
for idx, tag in enumerate(tag_list, 1):
    print(idx, tag.text)
