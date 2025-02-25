# sehirler = ['kocaeli','istanbul']
# plakalar = [41,34]

# print(plakalar[sehirler.index('istanbul')])

# plakalar = {'kocaeli' : 41, 'istanbul' : 34}

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])
# plakalar['ankara'] = 6
# print(plakalar)

# users = {
#     'esrakarakaya': 2,
#     'özgürçokçeken': 3
# }

# print(users['esrakarakaya'])

ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532525252'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '8585855454'
    }
}

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyad: ")
phone = input("Öğrenci telefon: ")

# Yeni öğrenciyi ekle
ogrenciler[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}

print(ogrenciler)
