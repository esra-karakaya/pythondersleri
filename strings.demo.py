website = "http://www.esracokceken.com" 

course = "python kursu: baştan sona python programlama rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
result = len(course)
length = len(website)

# 2- 'website' içinden www karakterlerini alın.
result = website [7:10]

# 3- 'website' içinden com karakterlerini alın.
result = website [24:27]
result = website[-3:]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result= course[:15]  # İlk 15 karakter
result = course[-15:] 

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::-1]

name, surname, age, job = 'Esra', 'Çokçeken', 23, 'data analyst'
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Esra Çokçeken, yaşım 23 ve mesleğim data analyst'
result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"
# burada f-string kullanmadan aynı sonucu elde etmek için + operatörünü ve str() fonksiyonunu kullanmak gerekirdi:
# örnek result = "Benim adım " + name + " " + surname + ", yaşım " + str(age) + " ve mesleğim " + job
# Bu kod da çalışır ama daha uzun ve okunması zor bir yöntemdir.

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin
result = "Hello world".replace("w", "W")

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result = 'abc' *3
print(result)