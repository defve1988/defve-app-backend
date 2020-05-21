from bs4 import BeautifulSoup
import requests



def video_title(url):
    source= requests.get(url).text
    print(source)
    soup=BeautifulSoup(source,'lxml')
    div_s = soup.findAll('div')
    Title = div_s[1].find('span',class_='watch-title').text.strip()
    return Title,url
