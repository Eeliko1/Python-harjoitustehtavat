import random

luku = random.randint(1, 10)

while True:
    arvaa = int(input('Arvaa luku 1-10 väliltä: '))
    if arvaa < luku:
        print('Liian pieni arvaus')
    elif arvaa > luku:
        print('Liian suuri arvaus')
    else:
        print('Oikein!')
        break
