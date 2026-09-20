import random

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
    autot = []
    for i in range(1, 11):
        rekisteri = f'ABC-{i}'
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteri, huippunopeus))

    kilpailu_kaynnissa = True

    while kilpailu_kaynnissa:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

            if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False

    print(f'{"Rekisteri":<12} | {"Huippunopeus":<15} | {"Tämänhetkinen nopeus":<22} | {"Kuljettu matka":<15}')
    print('-' * 72)

    for auto in autot:
        print(f'{auto.rekisteritunnus:<12} | {auto.huippunopeus:<15.0f} | {auto.tamanhetkinen:<22.0f} | {auto.kuljettu_matka:<15.0f}')