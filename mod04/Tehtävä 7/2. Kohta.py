import random

def noppa(tahkot):
    return random.randint(1, tahkot)

max = int(input('Montako tahkoa nopassa: '))

luku = 0

while luku != max:
    luku = noppa(max)
    print(f'Heitit: {luku}')