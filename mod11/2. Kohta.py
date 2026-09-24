class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


sahko = Sahkoauto('ABC-15', 180, 52.5)
polttomoottori = Polttomoottoriauto('ACD-123', 165, 32.3)

sahko.nopeus = 120
polttomoottori.nopeus = 100

sahko.kulje(3)
polttomoottori.kulje(3)

print(f'Sähköauton ({sahko.rekisteritunnus}) matkamittari: {sahko.kuljettu_matka} km')
print(f'Polttomoottoriauton ({polttomoottori.rekisteritunnus}) matkamittari: {polttomoottori.kuljettu_matka} km')