kuhan_mitta = float(input('Kuinka monta senttimetriä pitkä kuha on: '))

puuttuu = 37-kuhan_mitta

if kuhan_mitta < 37:
    print(f'Liian lyhyt, laske se takas järveen. Alimmasta pyyntimitasta puutuu {puuttuu: .2f} cm.')

else:
    print('On tarpeeksi pitkä.')