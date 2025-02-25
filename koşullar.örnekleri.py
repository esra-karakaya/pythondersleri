#1- kullanıcılardan isim, yaş ve eğitim bilgilerini isteyip ehliyet
# alabilme durumunu kontrol ediniz. Ehliyet alma koşulu
# en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

# isim = input("İsminiz: ")
# yas = int(input("Yaşınız: "))
# egitim = input("Eğitim durumunuz: ").lower()  # Kullanıcının girdisini küçük harfe çeviriyoruz

# if yas >= 18:
#     if egitim == "lise" or egitim == "üniversite":  # Karşılaştırma için '==' kullanılıyor
#         print(f"{isim}, ehliyet alabilirsiniz.")
#     else:
#         print(f"{isim}, ehliyet alamazsınız. Eğitim durumunuz yetersiz.")
# else:
#     print(f"{isim}, ehliyet alamazsınız. Yaşınız tutmuyor.")


#2- bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya
# göre not aralığına karşılık gelen not bilgisini yazdırınız.
# 0-24 = 0
# 25-44 = 1
# 45-54 = 2
# 55-69 = 3
# 70-84 = 4
# 85-100 = 5

# def not_hesapla():
#     try:
#         # Kullanıcıdan notları al
#         yazili1 = float(input("1. Yazılı notunuzu girin: "))
#         yazili2 = float(input("2. Yazılı notunuzu girin: "))
#         sozlu = float(input("Sözlü notunuzu girin: "))

#         # Notların geçerli olup olmadığını kontrol et
#         if not (0 <= yazili1 <= 100 and 0 <= yazili2 <= 100 and 0 <= sozlu <= 100):
#             print("Hata: Notlar 0 ile 100 arasında olmalıdır.")
#             return  # Fonksiyonu sonlandır
        
#         # Ortalamayı hesapla
#         ortalama = (yazili1 + yazili2 + sozlu) / 3

#         # Not aralıklarına göre puanı belirle
#         not_araligi = {
#             (0, 24): 0,
#             (25, 44): 1,
#             (45, 54): 2,
#             (55, 69): 3,
#             (70, 84): 4,
#             (85, 100): 5
#         }

#         not_bilgisi = next((puan for aralik, puan in not_araligi.items() if aralik[0] <= ortalama <= aralik[1]), "Geçersiz not")

#         # Sonucu ekrana yazdır
#         print(f"Ortalamanız: {ortalama:.2f} - Notunuz: {not_bilgisi}")

#     except ValueError:
#         print("Hata: Lütfen geçerli bir sayı girin.")

# # Fonksiyonu çağır
# not_hesapla()


#3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki
# bilgilere göre hesapla
# 1. bakım = 1.yıl
# 2. bakım = 2.yıl
# 3. bakım = 3.yıl
# süre hesabını alınan gün ay yıl bilgisine göre gün bazlı hesapla
# datetime modülünü kullanmak gerekli

from datetime import datetime

gun = int(input("Aracın trafiğe çıkış günü: "))
ay = int(input("Aracın trafiğe çıkış ayı: "))
yil = int(input("Aracın trafiğe çıkış yılı: "))

trafik_cikis = datetime(yil, ay, gun)

bugun = datetime.now()

gecen_sure = bugun - trafik_cikis
gecen_gun = gecen_sure.days

if gecen_gun < 365:
    print("1. bakım zamanı")
elif 365 <= gecen_gun < 730:
    print("2. bakım zamanı")
elif 730 <= gecen_gun < 1095:
    print("3. bakım zamanı")
else:
    print("Bakım süresi geçmiş, en kısa sürede servise gidin!")

