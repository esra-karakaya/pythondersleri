# Girilen 2 sayıdan hangisi büyüktür

# a = int(input('a: '))
# b = int(input('b: '))

# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür: {result}')

# Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# vize1 = float(input('1.vize '))
# vize2 = float(input('2.vize '))
# final = float(input('final '))

# ortalama = ((vize1 + vize2) * 0.6) + (final * 0.4)

# print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz : {ortalama>=50}')

# vize1 = float(input('1. Vize: '))
# vize2 = float(input('2. Vize: '))
# final = float(input('Final: '))

# ortalama = ((vize1 + vize2) * 0.6) + (final * 0.4)
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
# # Geçti veya Kaldı yazdırmak için ternary if kullanıyoruz
# durum = "Geçti" if ortalama >= 50 else "Kaldı"

# print(f'Not ortalamanız: {ortalama} ve dersten geçme durumunuz: {durum}')

# Girilen bir sayının tek mi çift mi olduğunu yazdırın

# sayi = int(input('sayı'))

# tekcift = (sayi % 2 == 0 )

# print(f'girilen sayi cift olma durumu:{tekcift}')
 
# sayi = int(input('Sayı: '))  # Kullanıcıdan bir sayı al

# if sayi % 2 == 0:
#     print(f'Girilen sayı {sayi} çifttir.')
# else:
#     print(f'Girilen sayı {sayi} tektir.')

# Girilen bir sayının negatif pozitif durumunu yazdırın

# sayi = int(input('Sayı: '))  # Kullanıcıdan bir sayı al

# if sayi > 0:
#     print('Girilen sayı pozitiftir.')
# elif sayi < 0:
#     print('Girilen sayı negatiftir.')
# else:
#     print('Girilen sayı sıfırdır.')

# Parola ve email bilgisini isteyip doğruluğunu kontrol edin 

# (email: email@esrakarakaya.com parola:abc123)


# Kullanıcı bilgileri
email = 'email.esrakarakaya.com'
password = 'abc123'

# Kullanıcıdan giriş bilgilerini al
girilenEmail = input('Email: ')
girilenPassword = input('Parola: ')

# Email doğrulama
if girilenEmail == email:
    # Parola doğrulama
    if girilenPassword == password:
        print('Giriş yapabilirsiniz.')  # Her şey doğru
    else:
        print('Parola yanlış.')  # Parola yanlış
else:
    print('Email kullanılmıyor.')  # Email yanlış

