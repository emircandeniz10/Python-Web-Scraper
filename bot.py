import requests
from bs4 import BeautifulSoup
import time
import csv  # Yeni aletimiz: Tablo oluşturucu (Kurulum gerektirmez!)

url = "http://quotes.toscrape.com/"

print("🌐 Hedef siteye bağlanılıyor...")
time.sleep(1)

cevap = requests.get(url)
soup = BeautifulSoup(cevap.text, "html.parser")

sozler = soup.find_all("span", class_="text")
yazarlar = soup.find_all("small", class_="author")

print("✅ Veriler çekildi, şimdi dosyaya kaydediliyor...\n")
time.sleep(1)

# 'unlu_sozler.csv' adında bir dosya oluşturup içine giriyoruz
with open("unlu_sozler.csv", "w", encoding="utf-8-sig", newline="") as dosya:
    yazici = csv.writer(dosya)
    
    # Tablonun en üstüne başlıklarımızı (Kolon isimlerini) ekliyoruz
    yazici.writerow(["Söz", "Yazar"])
    
    # Sitedeki tüm sözleri ve yazarları tek tek alt satırlara yazıyoruz
    for i in range(len(sozler)):
        yazici.writerow([sozler[i].text, yazarlar[i].text])

print("🎉 İşlem tamam! VS Code'da sol tarafa bak, 'unlu_sozler.csv' dosyası seni bekliyor.")