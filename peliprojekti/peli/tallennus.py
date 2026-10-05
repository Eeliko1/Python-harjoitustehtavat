import json
import os

TALLENNUS_TIEDOSTO = 'pelin_tallennus.json'

# Luo intro.txt ja ohjeet.txt tiedostot jos niitä ei ole vielä olemassa
def luo_oletustiedostot_tarvittaessa():
    if not os.path.exists('intro.txt'):
        with open('intro.txt', 'w', encoding='utf-8') as f:
            f.write(
                '--------------------------------------------------\n'
                '                YMPÄRISTÖN PUTSAUS\n'
                '--------------------------------------------------\n'
                'Tavoite: Liiku eri alueilla, kerää kaikki 4 roskaa\n'
                          'ja vie ne kierrätyskeskukseen!\n'
                '--------------------------------------------------\n'
            )

    if not os.path.exists('ohjeet.txt'):
        with open('ohjeet.txt', 'w', encoding='utf-8') as f:
            f.write(
                '--- PELIN KOMENNOT ---\n'
                'status       - Näytä pelaajan tiedot ja kerätyt roskat\n'
                'katso        - Katso ympärillesi ja tarkista alue\n'
                'liiku        - Liiku toiselle alueelle\n'
                'kerää        - Kerää alueella oleva roska\n'
                'kierrätä     - Vie kerätyt roskat kierrätyskeskukseen\n'
                'noppa        - Heitä noppaa\n'
                'uusi nimi    - Vaihda pelinimesi\n'
                'tallenna     - Tallenna pelitilanne ja jatka myöhemmin\n'
                'ohjeet       - Näytä tämä ohje uudelleen\n'
                'lopeta       - Poistu pelistä\n'
            )

# Lukee ja palauttaa intro.txt ja ohjeet.txt tiedostot virheenkäsittelyllä
def lue_tekstitiedosto(tiedoston_nimi):
    try:
        with open(tiedoston_nimi, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f'Virhe: Tiedostoa "{tiedoston_nimi}" ei löytynyt.'
    except IOError:
        return f'Virhe: Tiedoston "{tiedoston_nimi}" käsittelyssä tapahtui virhe.'

# Tallentaa pelaajan tilanteen JSON tiedostoon
def tallenna_peli(pelaaja):
    tallennus_data = {
        'nimi': pelaaja.nimi,
        'sijainti': pelaaja.sijainti.nimi,
        'esineet': [e.nimi for e in pelaaja.esineet]
    }

    with open(TALLENNUS_TIEDOSTO, 'w') as f:
        json.dump(tallennus_data, f, ensure_ascii=False)
    print(f'\nPeli tallennettu tiedostoon "{TALLENNUS_TIEDOSTO}"!')

# Lataa tallennetun pelin JSON tiedostosta virheenkäsittelyllä
def lataa_peli(huoneet):
    try:
        with open(TALLENNUS_TIEDOSTO, 'r') as f:
            data = json.load(f)

            nimi = data.get('nimi')
            sijainti_nimi = data.get('sijainti')
            keratyt_nimet = data.get('esineet', [])

            sijainti = huoneet.get(sijainti_nimi)
            return nimi, sijainti, keratyt_nimet

    except FileNotFoundError:
        print('Virhe: Tallennustiedostoa ei löytynyt.')
    except (json.JSONDecodeError, IOError):
        print('Virhe: Tallennustiedosto on korruptoitunut tai sitä ei voitu lukea.')

    return None

# Poistaa tallennustiedoston kun peli on läpäisty
def poista_tallennus():
    if os.path.exists(TALLENNUS_TIEDOSTO):
        os.remove(TALLENNUS_TIEDOSTO)
        print('\nTallennettu pelitilanne nollattiin läpipelaamisen takia.')
