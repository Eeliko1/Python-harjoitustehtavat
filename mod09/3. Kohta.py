class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tamanhetkinen + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen = 0
        else:
            self.tamanhetkinen = uusi_nopeus

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.tamanhetkinen * tuntimaara

if __name__ == '__main__':
    uusi_auto = Auto('ABC-123', 142)

    uusi_auto.kuljettu_matka = 2000
    uusi_auto.kiihdyta(60)
    uusi_auto.kulje(1.5)

    print(f'Kuljettu matka: {uusi_auto.kuljettu_matka} km')