vuodenajat = ('talvi', 'kevät', 'kesä', 'syksy')

kuukausi = int(input('Anna kuukauden numero (1-12): '))

if kuukausi in (12, 1, 2):
    vuodenaika = vuodenajat[0]
elif kuukausi in (3, 4, 5):
    vuodenaika = vuodenajat[1]
elif kuukausi in (6, 7, 8):
    vuodenaika = vuodenajat[2]
elif kuukausi in (9, 10, 11):
    vuodenaika = vuodenajat[3]
else:
    vuodenaika = None

if vuodenaika:
    print(f'Kuukausi {kuukausi} kuuluu vuodenaikaan: {vuodenaika}')
else:
    print('Väärä kuukauden numero!')