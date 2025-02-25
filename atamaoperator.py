# x,y,z = 5, 10, 20

# print(x, y, z)



# kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir

# x, y, z'ye sırasıyla 2, 5, 10 değerlerini atıyoruz
x, y, z = 2, 5, 10

# numbers adında 5 sayılık bir tuple oluşturuluyor
numbers = 1, 5, 7, 10, 6

# Kullanıcıdan iki sayı alınıyor
a = int(input('1.sayı'))
b = int(input('2.sayı'))

# `a` ile `b`'nin çarpımı hesaplanır ve `x`, `y`, `z`'nin toplamı çıkarılır
result = (a * b) - (x+y+z)
print(result)  