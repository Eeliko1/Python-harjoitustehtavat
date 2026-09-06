import random

nimi = input('Mikä on nimesi: ')
ikä = int(input('Mikä on ikäsi: '))

# Iän tarkistus
if ikä < 12:
    print('Olet liian nuori. Ohjelma sammuu.')
else:
    print('Tervetuloa!')

    #Päävalikko
    while True:
        print('\n--- Päävalikko ---')
        print("status  - Näytä pelaajan tiedot")
        print("lopeta  - Sulje peli")
        print("noppa   - Heitä noppaa")

        komento = input('\nAnna komento: ')

        #Komennot
        if komento == 'lopeta':
            print(f'Kiitos pelaamisesta {nimi}!')
            break
        elif komento == 'status':
            print(f'STATUS: Pelaaja: {nimi}')
        elif komento == 'noppa':
            noppa = random.randint(1, 6)
            print(f'NOPPA: Heitit luvun {noppa}!')
        else:
            print('Tuntematon komento. Yritä uudelleen.')