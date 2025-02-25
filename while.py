#while döngüsü, belirtilen koşul sağlandığı sürece çalışan bir döngüdür.

# For Döngüsü	                                        While Döngüsü
# Belirli bir koleksiyonun elemanlarını işler.	    Koşul sağlandığı sürece çalışır.
# Kaç kez çalışacağı önceden bellidir.	            Kaç kez çalışacağı önceden belli olmayabilir.
# for i in range(5): gibi sayaç kullanır.            while i < 5: gibi şart kullanır.

x=0

while x < 100:
    print(x)
    x = x + 1

print('bitti...')