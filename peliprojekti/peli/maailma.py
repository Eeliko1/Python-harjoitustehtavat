from peli.luokat import Alue, Roska

def luo_pelimaailma():
    # Pelialueiden luonti
    kierratyskeskus = Alue('Kierrätyskeskus', 'Pelin aloitus- ja päätepaikka. Tuo roskat tänne!')
    metsapolku = Alue('Metsäpolku', 'Hiljainen metsä, mutta maassa lojuu muovipullo.')
    ranta = Alue('Saastunut Ranta', 'Rannan hiekalla on vanha paristo.')
    puisto = Alue('Puisto', 'Nurmikolla lojuu metallinen säilyketölkki.')
    tehdas = Alue('Hylätty Tehdas', 'Vanha tehdasalue, jossa on elektroniikkaroskaa.')

    # Roskien sijoitus alueille
    metsapolku.esine = Roska('Muovipullo', 0.1)
    ranta.esine = Roska('Paristo', 0.2)
    puisto.esine = Roska('Säilyketölkki', 0.15)
    tehdas.esine = Roska('Piirilevy', 0.1)

    # Kulkuyhteyksien kytkentä
    kierratyskeskus.suunta('itä', metsapolku)
    kierratyskeskus.suunta('pohjoinen', puisto)

    metsapolku.suunta('länsi', kierratyskeskus)
    metsapolku.suunta('pohjoinen', ranta)

    puisto.suunta('etelä', kierratyskeskus)
    puisto.suunta('itä', tehdas)

    ranta.suunta('etelä', metsapolku)
    ranta.suunta('länsi', tehdas)

    tehdas.suunta('itä', ranta)
    tehdas.suunta('länsi', puisto)

    # Kartan palautus sanakirjana
    return {
        'Kierrätyskeskus': kierratyskeskus,
        'Metsäpolku': metsapolku,
        'Saastunut Ranta': ranta,
        'Puisto': puisto,
        'Hylätty Tehdas': tehdas
    }
