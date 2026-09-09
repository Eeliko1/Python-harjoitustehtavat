def parittomat(luvut):
    parilliset = []
    for x in luvut:
        if x % 2 == 0:
            parilliset.append(x)
    return parilliset

eka_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

uus_lista = parittomat(eka_lista)

print(f'Vanha lista: {eka_lista}')
print(f'Uusi lista: {uus_lista}')