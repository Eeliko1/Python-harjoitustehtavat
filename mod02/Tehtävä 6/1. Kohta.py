import random

maara = int(input('Arpakuutioiden määrä: '))

summa = 0

for x in range(maara):
    heitto = random.randint(1, 6)
    summa += heitto

print(f'Lukujen summa on {summa}')