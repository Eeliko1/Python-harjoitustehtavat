import os
import random
from peli.luokat import Pelaaja, Roska
from peli.maailma import luo_pelimaailma
from peli.tallennus import (
    luo_oletustiedostot_tarvittaessa,
    lue_tekstitiedosto,
    tallenna_peli,
    lataa_peli,
    poista_tallennus
)

# Pelinimen vaihto
def nimen_vaihto(pelaaja):
    uusi_nimi = input('Uusi nimi: ')
    pelaaja.nimi = uusi_nimi
    print(f'Pelinimesi on vaihdettu! Uusi pelinimesi on {pelaaja.nimi}.')

# Nopan heitto
def nopan_heitto():
    noppa = random.randint(1, 6)
    print(f'NOPPA: Heitit luvun {noppa}!')

# Status näyttö
def nayta_status(pelaaja):
    print('\n--- STATUS ---')
    print(f'Pelaaja: {pelaaja.nimi}')
    print(f'Nykyinen sijainti: {pelaaja.sijainti.nimi}')
    print('Repun sisältö:')
    if len(pelaaja.esineet) == 0:
        print('  (Tyhjä)')
    else:
        for esine in pelaaja.esineet:
            print(f'  - {esine.nimi} ({esine.paino} kg)')


def main():
    # Luo intro.txt ja ohjeet.txt tiedostot automaattisesti jos niitä ei vielä ole
    luo_oletustiedostot_tarvittaessa()

    # Esittelyteksti otetaan intro.txt tiedostosta
    print(lue_tekstitiedosto('intro.txt'))

    huoneet = luo_pelimaailma()
    aloitushuone = huoneet['Kierrätyskeskus']
    pelaaja = None

    # Tarkistaa löytyykö tallennettua peliä
    if os.path.exists('pelin_tallennus.json'):
        valinta = input('\nLöytyi tallennettu peli. Haluatko jatkaa siitä? (k/e): ')
        if valinta == 'k':
            ladattu = lataa_peli(huoneet)
            if ladattu:
                nimi, sijainti, keratyt_nimet = ladattu
                pelaaja = Pelaaja(nimi, sijainti if sijainti else aloitushuone)

                # Palauttaa kerätyt esineet pelaajalle
                kaikki_esineet = {
                    'Muovipullo': Roska('Muovipullo', 0.1),
                    'Paristo': Roska('Paristo', 0.2),
                    'Säilyketölkki': Roska('Säilyketölkki', 0.15),
                    'Piirilevy': Roska('Piirilevy', 0,1)
                }
                for e_nimi in keratyt_nimet:
                    if e_nimi in kaikki_esineet:
                        pelaaja.esineet.append(kaikki_esineet[e_nimi])

                # Poistaa kerätyt roskat maasta
                for h in huoneet.values():
                    if h.esine and h.esine.nimi in keratyt_nimet:
                        h.esine = None

                print(f'\nTervetuloa takaisin {pelaaja.nimi}! Sijaintisi: {pelaaja.sijainti.nimi}')

    # Jos peli ei ladannut, luodaan uusi pelaaja ja kysytään nimi ja ikä
    if not pelaaja:
        nimi = input('\nMikä on nimesi: ')

        # Iän tarkistus
        while True:
            try:
                ika = int(input('Mikä on ikäsi: '))
                break
            except ValueError:
                print('Virhe: syötetty arvo ei ole kokonaisluku. Yritä uudestaan.')

        if ika < 12:
            print('Olet liian nuori. Ohjelma sammuu.')
            return
        else:
            print('Tervetuloa!')
            pelaaja = Pelaaja(nimi, aloitushuone)

    # Tulostaa pelin ohjeet ohjeet.txt tiedostosta
    print('\n' + lue_tekstitiedosto('ohjeet.txt'))

    # Päävalikko
    while True:
        print('\n--- Päävalikko ---')
        print('status    - Näytä pelaajan tiedot')
        print('katso     - Katso alueen tiedot')
        print('liiku     - Liiku toiselle alueelle')
        print('kerää     - Kerää roska')
        print('kierrätä  - Kierrätä roskat kierrätyskeskuksessa')
        print('noppa     - Heitä noppaa')
        print('uusi nimi - Vaihda pelinimesi')
        print('tallenna  - Tallenna peli')
        print('ohjeet    - Näytä ohjeet')
        print('lopeta    - Sulje peli')

        komento = input('\nAnna komento: ')

        # Kaikki komennot
        if komento == 'lopeta':
            print(f'Kiitos pelaamisesta {pelaaja.nimi}!')
            break

        elif komento == 'status':
            nayta_status(pelaaja)

        elif komento == 'noppa':
            nopan_heitto()

        elif komento == 'uusi nimi':
            nimen_vaihto(pelaaja)

        elif komento == 'ohjeet':
            print('\n' + lue_tekstitiedosto('ohjeet.txt'))

        elif komento == 'tallenna':
            tallenna_peli(pelaaja)

        elif komento == 'katso':
            print(f'\nOlet paikassa: {pelaaja.sijainti.nimi}')
            print(f'Kuvaus: {pelaaja.sijainti.kuvaus}')
            if pelaaja.sijainti.esine:
                print(f'Huomaat maassa esineen: {pelaaja.sijainti.esine.nimi}!')
            else:
                print('Täällä ei ole roskia.')

        elif komento == 'liiku':
            print(f'Mahdolliset suunnat: {", ".join(pelaaja.sijainti.naapurit.keys())}')
            suunta = input('Valitse suunta: ')
            pelaaja.liiku(suunta)

        elif komento == 'kerää':
            pelaaja.keraa_esine()

        elif komento == 'kierrätä':
            if pelaaja.sijainti.nimi != 'Kierrätyskeskus':
                print('\nVoit kierrättää roskat vain kierrätyskeskuksessa!')
            else:
                if len(pelaaja.esineet) >= 4:
                    print('\n--------------------------------------------------')
                    print(f'Onnea {pelaaja.nimi}! Läpäisit pelin!')          
                    print('--------------------------------------------------')
                    poista_tallennus()
                    break
                else:
                    print(f'\nSinulta puuttuu vielä {4 - len(pelaaja.esineet)} roskaa!')

        else:
            print('Tuntematon komento. Yritä uudelleen.')


if __name__ == '__main__':
    main()
