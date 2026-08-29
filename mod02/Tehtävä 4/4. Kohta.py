vuosi = int(input('Syötä vuosiluku: '))

if vuosi % 400 == 0:
    print(f'Vuosi {vuosi} on karkausvuosi.')
elif vuosi % 100 == 0:
    print(f'Vuosi {vuosi} ei ole karkausvuosi.')
elif vuosi % 4 == 0:
    print(f'Vuosi {vuosi} on karkausvuosi.')
else:
    print(f'Vuosi {vuosi} ei ole karkausvuosi.')