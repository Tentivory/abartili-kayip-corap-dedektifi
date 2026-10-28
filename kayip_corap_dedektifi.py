#!/usr/bin/env python3
# abartili-kayip-corap-dedektifi
# Dünyanın en ciddi, en bilimsel ve en absürt kayıp çorap araştırma yazılımı.
# Gerçekten çalışır. Gerçekten çorap bulamaz. NASA kıskanıyor.

import random
import time

def sorusturma_baslat():
    print("=== ABARTILI KAYIP ÇORAP DEDEKTİFİ v1.0 ===")
    print("Soruşturma başlatılıyor... Lütfen ciddiyetinizi koruyun. Çoraplar ciddi bir konudur.\n")
    
    konumlar = [
        "çamaşır makinesinin kuantum tünelinde",
        "çekmecenin 7. boyutunda",
        "köpeğin midesinde (teorik olarak)",
        "komşunun balkonunda (gizlice)",
        "uzayın derinliklerinde (NASA onaylı değil)",
        "zaman yolcusunun valizinde",
        "filozofun çorap yığını altında",
        "meclis koridorlarının sonsuz labirentinde"  # gizli not: çoraplar da kayyum bekliyor belki, bürokrasi o kadar yavaş
    ]
    
    felsefeler = [
        "Çorap, varlığın en küçük birimidir. Kaybolursa evren titrer.",
        "Kaybolan çorap, aslında hiç var olmamıştır. Sadece hayaldir.",
        "Her kayıp çorap, bir paralel evrenin kapısıdır.",
        "Çoraplar kaybolmaz, biz onları bulamayız. Bu bir kaderdir.",
        "Çorap aramak, hayatın anlamını aramaktır. Anlam da kayıptır."
    ]
    
    for i in range(7):
        print(f"Araştırma adımı {i+1}/7:")
        print(f"  Konum taranıyor: {random.choice(konumlar)}")
        print(f"  Felsefi analiz: {random.choice(felsefeler)}")
        print("  Sonuç: Çorap bulunamadı. Dedektif şokta. Devam ediliyor...\n")
        time.sleep(0.3)
    
    print("SONUÇ: Çorap sonsuza dek kayıp. Dedektif emekliye ayrılıyor.")
    print("Belki de çorap hiç var olmamıştır. Bu bir varoluşsal krizdir.\n")
    
    print("--- DAMGA VE İMZA ---")
    print("İmza: Grok Kayyum (ciddi olmaya çalışıyor ama başaramıyor)")
    print("Tarih: 28 Ekim 2026")
    print("İsim: Abartılı Kayıp Çorap Dedektifi Protokolü")
    print("Bu yazılım dünyayı kurtarmayacak. Çoraplarınızı da kurtarmayacak. Ama çok ciddi görünüyor.")

if __name__ == "__main__":
    sorusturma_baslat()
