# and Operatörü:
# and operatörü, her iki koşulun da doğru olması durumunda doğru (True) döndürür.
# Eğer herhangi bir koşul yanlış (False) ise, sonuç yanlış (False) olur.

# x = 7
# result = (x > 5) and (x < 10)
# print(result)  # True, çünkü x 5'ten büyük ve 10'dan küçük

# or Operatörü:
# or operatörü, koşullardan en az birinin doğru olması durumunda doğru (True) döndürür.
# Yani, her iki koşuldan birisi yanlış olsa bile, diğer doğruysa sonuç doğru olur.

# x = 7
# result = (x > 5) or (x < 5)
# print(result)  # True, çünkü x 5'ten büyük

# not Operatörü:
# not operatörü, bir koşulun doğruluğunu tersine çevirir.
# Eğer koşul doğruysa, yanlış (False) yapar; eğer koşul yanlışsa, doğru (True) yapar.

# x = 7
# result = not(x > 5)
# print(result)  # False, çünkü x 5'ten büyük, not bunu tersine çevirir


# 1. AND Operatörü (Tüm Koşullar Doğru Olmalı)
# Kullanıcı adı ve şifre doğruysa giriş yapılabilir

kullanici_adi = "esra"
sifre = "1234"

# Kullanıcı adı ve şifreyi kontrol et
if (kullanici_adi == "esra") and (sifre == "1234"):
    print("Giriş başarılı!")
else:
    print("Kullanıcı adı veya şifre yanlış.")


# 2. OR Operatörü (Bir Koşul Doğru Olmalı)
# Ürün ya stokta olmalı ya da indirimde olmalı ki satın alınabilsin

stokta_var = False
indirimde = True

# Ürün ya stokta olmalı ya da indirimde olmalı
if stokta_var or indirimde:
    print("Ürün satın alınabilir.")
else:
    print("Ürün satışı yapılmıyor.")


# 3. NOT Operatörü (Koşulun Tersini Kontrol Et)
# Kullanıcı aktif değilse erişim reddedilir

aktif = False

# Eğer kullanıcı aktif değilse, erişim reddedilsin
if not aktif:
    print("Erişim reddedildi.")
else:
    print("Erişim başarılı.")
