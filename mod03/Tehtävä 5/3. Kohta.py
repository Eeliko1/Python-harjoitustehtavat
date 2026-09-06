luvut = input('Anna luku: ')

if luvut != '':
    luku = float(luvut)
    pienin = luku
    isoin = luku

    while True:
        luvut = input('Anna luku: ')
        if luvut == '':
            break
            
        luku = float(luvut)
        if luku < pienin:
            pienin = luku
        if luku > isoin:
            isoin = luku

    print(f'Pienin luku: {pienin}')
    print(f'Suurin luku: {isoin}')