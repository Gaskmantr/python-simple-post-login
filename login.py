import requests
from bs4 import BeautifulSoup as bs

giris_url = "https://emlaksitem.com/giris-yap"
with requests.Session() as s:
    giris_sayfasi = s.get(giris_url)

    soup = bs(giris_sayfasi.text,'html.parser')
    token = soup.find(attrs={'name': '_token'}).get("value")


    bilgiler = {
        'email' : 'ad',
        'password': 'sifre',
        '_token' : token
    }

    giris_yap = s.post(giris_url,data=bilgiler)
    panel = s.get("https://emlaksitem.com/panel/uyelik-bilgileri")

    if 'Bana Özel' in panel.text:
        print("Giriş yapıldı")
