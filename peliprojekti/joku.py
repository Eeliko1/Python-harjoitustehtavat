Nimi = input('Mikä on nimesi: ')

while True:
    Ikä = int(input('Mikä on ikäsi: '))

    if Ikä < 12:
        print('Olet liian nuori. Ohjelma sammuu')
        break

    print('Tervetuloa!')

    # Tää sammuttaa pelin, pistä pohjalle
