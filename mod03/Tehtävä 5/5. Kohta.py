yritykset = 0

while yritykset < 5:
    tunnus = input('Käyttäjätunnus: ')
    sala = input('Salasana: ')

    if tunnus == 'python':
        if sala == 'rules':
            print('Tervetuloa')
            break

    yritykset += 1
    print('Väärä käyttäjätunnus tai salasana')

if yritykset == 5:
    print('Pääsy evätty')