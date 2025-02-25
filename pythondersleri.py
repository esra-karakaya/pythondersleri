# Python'a Yeni Başlayanlar İçin Temel Konular

# 1️⃣ Değişkenler ve Veri Türleri
name = "Esra"  # String (Metin)
age = 22  # Integer (Tam sayı)
height = 1.65  # Float (Ondalıklı sayı)
is_student = True  # Boolean (True / False)

# 2️⃣ Tip Dönüşümü (Casting)
number = "25"  # String olarak tanımlandı
number = int(number)  # String -> Integer dönüşümü
print(number + 5)  # 30 olur

# 3️⃣ String İşlemleri
text = "Hello, World!"
print(text.upper())  # BÜYÜK HARF
print(text.lower())  # küçük harf
print(text.title())  # İlk harfler büyük
print(text.replace("World", "Esra"))  # Kelime değiştirir

# String slicing (Metni Parçalama)
print(text[0:5])  # 'Hello'
print(text[::-1])  # Tersten yazdırma

# 4️⃣ Listeler (List)
numbers = [1, 2, 3, 4, 5]  # Liste tanımlama
names = ["Esra", "Ahmet", "Mehmet"]
print(names[0])  # 'Esra' (İlk eleman)
numbers.append(6)  # Listeye eleman ekleme

# 5️⃣ Koşullu İfadeler (if-else)
age = 18
if age >= 18:
    print("Ehliyet alabilirsin.")
else:
    print("Ehliyet alamazsın.")

# 6️⃣ Döngüler (Loops)
# for döngüsü ile sayı yazdırma
for i in range(5):  # 0'dan 4'e kadar döner
    print(i)

# Liste içinde dönme
fruits = ["Elma", "Armut", "Muz"]
for fruit in fruits:
    print(fruit)

# while döngüsü
x = 0
while x < 5:
    print(x)
    x += 1

# 7️⃣ Fonksiyonlar (Functions)
def selamla(isim):
    print(f"Merhaba, {isim}!")

selamla("Esra")

# 8️⃣ Hata Yönetimi (try-except)
try:
    num = int(input("Bir sayı gir: "))
    print(10 / num)
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")
except ValueError:
    print("Geçerli bir sayı gir!")

