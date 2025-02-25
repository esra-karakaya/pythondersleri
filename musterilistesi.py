musteriAdi = 'Esra'
musteriSoyadi = 'Karakaya'
musteriAdiSoyadi = musteriAdi + '' + musteriSoyadi
musteriCinsiyet = True #erkek
musteriTcKimlik = '1313131313131'
musteriDogumYili = '2001'
musteriAdres = 'istanbul'
musteriYasi = 23

# Aşağıdaki siparişlerin toplam bilgisi nedir?
# sipariş 1 = 110 tl 
# sipariş 2 = 1220 tl 
# sipariş 3 = 599 tl 

order1 = 110
order2 = 1220
order3 = 599

total = order1 + order2+ order3
print("total:", total)

# Sipariş ve müşteri bilgilerini ekleyerek yazdırma
print(f"Müşteri: {musteriAdiSoyadi}")
print(f"Toplam Sipariş Tutarı: {total} TL")
print(f"Sipariş 1: {order1} TL")
print(f"Sipariş 2: {order2} TL")
print(f"Sipariş 3: {order3} TL")


