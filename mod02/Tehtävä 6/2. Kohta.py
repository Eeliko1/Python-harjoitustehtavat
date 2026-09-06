luvut = []

while True:
    luku = input('Anna lukuja: ')
    if luku == '':
        break

    luvut.append(float(luku))

luvut.sort(reverse=True)

viisi = luvut[:5]

print('\nViisi suurinta lukua suurimmasta alkaen: ')
for luku in viisi:
    print(luku)