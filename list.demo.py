names = ['Özgür', 'Esra', 'Tarçın']
years = [2001, 2001, 2021]

# "Gamze" ismini listenin sonuna ekleyiniz
names.append('Gamze') 
print(names)

# "Yıldız" ismini listenin başına ekleyiniz.
names.insert(-1, 'Yıldız')
print(names)

# Yıldız ismini listeden siliniz.
names.remove('Yıldız')
print(names)

years.sort()
print(years)

markalar = []
marka = input("marka: ")
markalar.append(marka)
print(markalar)
