class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f'Kirjan nimi: {self.nimi}')
        print(f'Kirjoittaja: {self.kirjoittaja}')
        print(f'Sivumäärä: {self.sivumaara} sivua\n')


hytti = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)

hytti.tulosta_tiedot()