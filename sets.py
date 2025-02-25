# Python'da set (küme), sırasız ve benzersiz öğeler içeren bir veri yapısıdır.
# Set'ler {} veya set() kullanılarak oluşturulur ve aynı öğeden birden fazla içermez.
# Liste ve tuple gibi koleksiyonlardan farklı olarak, set'ler indekslenemez ve değiştirilemez elemanlar içerir.

# Set’in Özellikleri
# Benzersiz Öğeler: Aynı öğeden birden fazla içermez.
# Sırasızdır: Öğeler belirli bir sıraya sahip değildir.
# Değiştirilebilir (Mutable): Yeni öğeler eklenip çıkarılabilir.
# Farklı Veri Türleri İçerebilir: Ancak sadece değiştirilemez (immutable) türdeki veriler eklenebilir (sayılar, stringler, tuple'lar gibi).

# Set Kullanım Alanları
# Benzersiz Öğeler Tutma: Bir listedeki tekrar eden elemanları kaldırmak için.
# Matematiksel Küme İşlemleri: Kesişim, birleşim gibi işlemler için.
# Hızlı Üyelik Kontrolleri: in operatörü ile veri aramak listelere göre daha hızlıdır.

# İndekslenebilir ve İndekslenemez Veri Yapıları
# ✔ İndekslenebilir: Liste (list), Tuple (tuple), String (str)
# ❌ İndekslenemez: Set (set), Sözlük (dict – anahtar üzerinden erişilir)

# İndekslenemez (Unindexed) demek, bir veri yapısındaki öğelere belirli bir sıra numarası (indeks) kullanarak erişilemeyeceği anlamına gelir. 
# Python'da listeler ve tuple'lar gibi veri yapıları indekslenebilirken, set (küme) indekslenemez.

# fruits = {'orange', 'apple', 'banana'}
# #print(fruits[0] indekslenemez)
# for x in fruits:
#     print(x)

# mylist = [1, 2, 3, 3, 4]
# print(mylist)
# print(set(mylist))
# set listeden tekrar edenleri kaldırır

