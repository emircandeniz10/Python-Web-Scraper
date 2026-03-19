# 🕸️ Python Web Scraper (Veri Kazıma Botu)

Bu proje, internet üzerindeki bir web sitesinden (quotes.toscrape.com) otomatik olarak veri çeken ve bu verileri düzenli bir tablo (CSV) formatında kaydeden bir Python botudur. 

## 🚀 Projenin Amacı ve Yetenekleri
Zaman alan manuel veri kopyalama işlemlerini otomatize etmek için geliştirilmiştir. Bot çalıştığında:
* Hedef web sitesine saniyeler içinde bağlanır.
* Sayfadaki HTML yapılarını analiz eder (BeautifulSoup kullanarak).
* İstenilen spesifik verileri (Ünlü sözler ve yazarları) ayıklar.
* Çekilen tüm verileri otomatik olarak `unlu_sozler.csv` adlı bir Excel/Tablo dosyasına kaydeder.

## 🛠️ Kullanılan Teknolojiler
* **Python 3**
* **Requests:** Web sitelerine HTTP istekleri göndermek için.
* **BeautifulSoup4 (bs4):** Karmaşık HTML kodlarını parse edip okumak için.
* **CSV:** Çekilen verileri tablo formatında dışa aktarmak için (Python dahili kütüphanesi).

## 📁 Nasıl Çalıştırılır?
1. Bilgisayarınızda Python'un kurulu olduğundan emin olun.
2. Gerekli kütüphaneleri kurmak için terminale `pip install requests beautifulsoup4` yazın.
3. `bot.py` dosyasını çalıştırın. Veriler anında aynı klasördeki `.csv` dosyasına kaydedilecektir.

---
**Contact & Freelance Inquiries:** 📧 canemo509@gmail.com | 💼 [LinkedIn Profilim](https://www.linkedin.com/in/emircan-deniz-a018b33b8/)
