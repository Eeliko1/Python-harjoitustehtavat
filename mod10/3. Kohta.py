class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f'Hissi on kerroksessa {self.nykyinen_kerros}')

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f'Hissi on kerroksessa {self.nykyinen_kerros}')

    def siirry_kerrokseen(self, kohdekerros):
        kohdekerros = max(self.alin_kerros, min(kohdekerros, self.ylin_kerros))

        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()

        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []

        for _ in range(hissien_lukumaara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 1 <= hissin_numero <= len(self.hissit):
            print(f'Ajetaan hissiä {hissin_numero} kerrokseen {kohdekerros}:')
            hissi = self.hissit[hissin_numero - 1]
            hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print('\n--- PALOHÄLYTYS! Kaikki hissit siirtyvät alas ---')
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


talo = Talo(1, 7, 3)

talo.aja_hissia(1, 5)
print()
talo.aja_hissia(2, 7)
print()
talo.aja_hissia(3, 3)

talo.palohalytys()