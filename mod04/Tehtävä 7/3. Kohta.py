def funktio(gallon):
    return gallon * 3.785

while True:
    gallona = float(input('Anna gallona määrä: '))

    luku = funktio(gallona)
    
    if gallona < 0:
        break

    print(f'Antamasi gallona määrä litroina: {luku: .3f}')
