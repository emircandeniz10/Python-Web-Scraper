# 🕸️ Python Web Scraper V2.0 (SQL Database Entegrasyonlu)

Bu proje, internet üzerindeki bir web sitesinden (quotes.toscrape.com) veri çeken ve bu verileri **otomatik olarak bir SQLite Veritabanına** kaydeden gelişmiş bir Python botudur.

## 🚀 Versiyon 2.0 Güncellemeleri ve Yetenekleri
* **SQLite3 Entegrasyonu:** Veriler artık basit bir Excel dosyası yerine, çok daha hızlı ve güvenli olan ilişkisel bir veritabanına (`.db`) kaydedilmektedir.
* **Otomatik Tablo Kurulumu:** Kod çalıştığında veritabanı dosyası yoksa sıfırdan oluşturur, `unlu_sozler` tablosunu otomatik inşa eder ve ID, Yazar, Söz sütunlarını ayarlar.
* **HTML Parsing:** BeautifulSoup4 ile karmaşık web elementleri saniyeler içinde ayrıştırılır.

## 🛠️ Kullanılan Teknolojiler
* **Python 3**
* **Requests & BeautifulSoup4** (Web Scraping için)
* **SQLite3** (Veritabanı yönetimi - Python dahili kütüphanesi)
* **DB Browser for SQLite** (Verileri görselleştirmek için)

## 📁 Nasıl Çalıştırılır?
1. Kütüphaneleri kurun: `pip install requests beautifulsoup4`
2. `bot.py` dosyasını çalıştırın. 
3. Proje klasörünüzde otomatik olarak `bot_verileri.db` dosyası oluşacak ve tüm veriler ID'lenmiş şekilde içine yazılacaktır.

---
**Contact & Freelance Inquiries:** 📧 canemo509@gmail.com | 💼 [LinkedIn Profilim](https://www.linkedin.com/in/emircan-deniz-a018b33b8/)
