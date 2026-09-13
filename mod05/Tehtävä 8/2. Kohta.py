nimet = set()

while True:
    nimi = input('Anna joku nimi listaan: ')

    if nimi == '':
        break

    if nimi in nimet:
        print('Aiemmin syötetty nimi')
    else:
        print('Uusi nimi')
        nimet.add(nimi)

print('\nSyötetyt nimet: ')

for x in nimet:
    print(x)