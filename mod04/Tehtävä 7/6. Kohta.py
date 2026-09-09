import math

def pizza(halkaisija, hinta):
    sade = (halkaisija / 100) / 2
    pinta_ala = math.pi * (sade ** 2)
    return hinta / pinta_ala

halkaisija1 = float(input('1. pizzan halkasija (cm): '))
hinta1 = float(input('1. pizzan hinta (€): '))

halkaisija2 = float(input('\n2. pizzan halkasija (cm): '))
hinta2 = float(input('2. pizzan hinta (€): '))

pizzan_hinta1 = pizza(halkaisija1, hinta1)
pizzan_hinta2 = pizza(halkaisija2, hinta2)

print(f'\n1. pizzan hinta: {pizzan_hinta1: .2f} €/m^2')
print(f'\n2. pizzan hinta: {pizzan_hinta2: .2f} €/m^2')

if pizzan_hinta1 < pizzan_hinta2:
    print('\nEnsimmäinen pizza on halvempi.')
elif pizzan_hinta2 < pizzan_hinta1:
    print('\nToinen pizza on halvempi.')
else:
    print('\nMolemmat ovat saman hintaisia.')
