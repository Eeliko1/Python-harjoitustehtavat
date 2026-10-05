class Pelaaja:
    def __init__(self, nimi, aloitushuone):
        self.nimi = nimi
        self.sijainti = aloitushuone
        self.esineet = []

    def liiku(self, kohde_suunta):
        if kohde_suunta in self.sijainti.naapurit:
            self.sijainti = self.sijainti.naapurit[kohde_suunta]
            print(f'\nLähdit suuntaan: {kohde_suunta}.')
            print(f'Olet nyt paikassa: {self.sijainti.nimi}')
            print(f'Kuvaus: {self.sijainti.kuvaus}')
        else:
            print('\nEt voi kulkea siihen suuntaan!')

    def keraa_esine(self):
        if self.sijainti.esine is not None:
            keratty = self.sijainti.esine
            self.esineet.append(keratty)
            self.sijainti.esine = None
            print(f'\nKeräsit esineen: {keratty.nimi} (paino: {keratty.paino} kg).')
            print('Se on nyt repussasi kierrätystä varten!')
        else:
            print('\nTäällä ei ole kerättäviä roskia.')


class Roska:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


class Alue:
    def __init__(self, nimi, kuvaus):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.esine = None
        self.naapurit = {}

    def suunta(self, suunta, huone):
        self.naapurit[suunta] = huone
