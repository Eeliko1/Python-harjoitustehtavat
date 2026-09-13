import random

# Pelinimen vaihto funktio
def nimen_vaihto():
    uusi_nimi = input('Uusi nimi: ')
    print(f'Pelinimesi on vaihdettu! Uusi pelinimesi on {uusi_nimi}.')
    return uusi_nimi

# Nopan heitto funktio
def nopan_heitto():
    noppa = random.randint(1, 6)
    print(f'NOPPA: Heitit luvun {noppa}!')

def nayta_status(nimi):
    print(f'STATUS: Pelaaja: {nimi}')

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
        print('status  - Näytä pelaajan tiedot')
        print('lopeta  - Sulje peli')
        print('noppa   - Heitä noppaa')
        print('uusi nimi   - Vaihda pelinimesi')

        komento = input('\nAnna komento: ')

        #Komennot
        if komento == 'lopeta':
            print(f'Kiitos pelaamisesta {nimi}!')
            break

        elif komento == 'status':
            nayta_status()

        elif komento == 'noppa':
            nopan_heitto()

        elif komento == 'uusi nimi':
            nimen_vaihto()

        else:
            print('Tuntematon komento. Yritä uudelleen.')

