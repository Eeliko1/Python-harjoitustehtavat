luku = int(input('Anna kokonaisluku: '))

if luku <= 1:
    alkuluku = False
else:
    alkuluku = True
    for x in range(2, luku):
        if luku % x == 0:
            alkuluku = False
            break

if alkuluku:
    print(f'Lukusi {luku} on alkuluku')
else: 
    print(f'Lukusi {luku} ei ole alkuluku')