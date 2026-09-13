lentokentät = {}

while True:
    print('\nValitse toiminto:')
    print('1 - Syötä uusi lentoasema')
    print('2 - Hae lentoaseman tiedot')
    print('3 - Lopeta')

    valinta = input('Valitse (1-3): ')

    if valinta == '1':
        icao = input('Anna lentokennän ICAO-koodi: ')
        nimi = input('Anna lentokennän nimi: ')

        lentokentät[icao] = nimi
        print(f'Lentokenttä {nimi} {icao} tallennettu')

    elif valinta == '2':
        icao = input('Anna haettavan lentokentän ICAO-koodi: ')

        if icao in lentokentät:
            print(f'ICAO-koodia {icao} vastaa lentokenttä: {lentokentät[icao]}')
        else:
            print(f'Lentokenttää ICAO-koodilla '{icao}' ei löytynyt.')

    elif valinta == '3':
        print('Kiitos ja näkemiin!')
        break

    else:
        print('Virheellinen valinta! Valitse 1, 2 tai 3.')