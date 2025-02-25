# tuple Neden Kullanılır?
# Verilerin değiştirilmesini istemiyorsan (immutable olması nedeniyle güvenlidir).
# Performans açısından daha hızlıdır (listelerden daha az bellek kullanır).
# Sabit veriler için idealdir, örneğin günler veya aylar

# Tuple ve List Arasındaki Farklar
# Özellik	Tuple	List
# Parantez	( )	[ ]
# Değiştirilebilir mi?	❌ Hayır (Immutable)	✅ Evet (Mutable)
# Hızlı mı?	✅ Daha hızlı	❌ Daha yavaş
# Boyutu değiştirilebilir mi?	❌ Hayır	✅ Evet
# Metotlar	Az metot (count, index)	Daha fazla metot (append, remove, pop, vb.)
# Eğer değiştirilebilir bir veri yapısına ihtiyacın varsa, liste kullanmalısın.

# Parantez ile tuple tanımlama
my_tuple = (1, 2, 3, 4, 5)

# Parantezsiz de tuple oluşturulabilir
my_tuple = 1, 2, 3, 4, 5  

# Tek elemanlı tuple oluştururken virgül olmalı
single_element_tuple = (10,)  # Virgül olmalı
not_a_tuple = (10)  # Bu bir int'tir

my_tuple = ('Esra', 'Özgür', 'Tarçın')

print(my_tuple[0])  # Çıktı: 'Esra'
print(my_tuple[1])  # Çıktı: 'Özgür'
print(my_tuple[-1])  # Çıktı: 'Tarçın' (Son eleman)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
result = t1 + t2
print(result)  # Çıktı: (1, 2, 3, 4, 5, 6)