def lista(luvut):
    summa = 0
    for x in luvut:
        summa += x
    return summa

testi = [2, 3, 6, 8, 65]

tulos = lista(testi)

print(f'Listan lukujen {testi} summa: {tulos}')