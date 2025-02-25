# **Python'da `if` Koşul Yapısı**

# `if` yapısı, programın belirli bir koşula göre farklı işlemler yapmasını sağlar. Eğer belirtilen koşul **doğru (`True`)** ise, `if` bloğunun içindeki kod çalıştırılır. Eğer koşul **yanlış (`False`)** ise, `if` bloğundaki kod atlanır.

# ---

# **`if` Kullanımı**
# ```python
# if koşul:
#     # Koşul doğruysa çalışacak kod bloğu

sayi = 10

if sayi > 5:
    print("Sayı 5'ten büyüktür.")



if koşul:
    # Koşul doğruysa çalışacak kod
else:
    # Koşul yanlışsa çalışacak kod


sayi = 3

if sayi > 5:
    print("Sayı 5'ten büyüktür.")
else:
    print("Sayı 5'ten küçük veya eşittir.")


if koşul1:
    # Koşul1 doğruysa çalışacak kod
elif koşul2:
    # Koşul2 doğruysa çalışacak kod
else:
    # Hiçbir koşul doğru değilse çalışacak kod


sayi = 5

if sayi > 10:
    print("Sayı 10'dan büyüktür.")
elif sayi == 5:
    print("Sayı 5'e eşittir.")
else:
    print("Sayı 10'dan küçük ve 5'e eşit değildir.")
