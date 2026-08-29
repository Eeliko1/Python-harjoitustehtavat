sukupuoli = input('Mikä on biologinen sukupuolesi (mies/nainen): ')
hemoglobiini = float(input('Mikä on hemoglobiiniarvosi (g/l): '))

if sukupuoli == 'mies':
    if hemoglobiini < 134:
        print(f'Hemoglobiini arvosi{hemoglobiini: .2f} on alhainen.')
    elif hemoglobiini <= 195:
        print(f'Hemoglobiini arvosi{hemoglobiini: .2f} on normaali.')
    else:
        print(f'Hemoglobiini arvosi{hemoglobiini: .2f} on korkea.')

elif sukupuoli == 'nainen':
    if hemoglobiini < 117:
        print(f'Hemoglobiini arvosi{hemoglobiini: .2f} on alhainen.')
    elif hemoglobiini <= 175:
        print(f'Hemoglobiini arvosi{hemoglobiini: .2f} on normaali.')
    else:
        print(f'Hemoglobiini arvosi{hemoglobiini: .2f} on korkea.')

else:
    print('Virheellinen sukupuoli.')