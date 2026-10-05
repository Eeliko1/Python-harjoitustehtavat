# Ympäristön Putsaus
## Eeli Koivisto

### Pelin idea ja tavoite
Pelin ideana on liikkua eri alueilla, kerätä sieltä roskia ja palauttaa ne kierrätyspisteelle. Pelin päätavoitteena on voittaa, kunhan kaikki roskat on kerätty ja palutettu kierrätyspisteelle.

### Toimintaperiaatteet
**Oliorakenne**
- **Pelaaja:** Hallitsee pelaajan nimeä, nykyistä sijaintia sekä inventaariota.
- **Alue:** Edustaa pelimaailman eri sijainteja. Alueilla on nimi, kuvaus, mahdolliset ilmansuunnat ja siellä mahdollisesti sijaitseva roska.
- **Roska:** Kuvaa maasta löytyviä roskia, joilla on nimi ja paino.

**Moduulit**
 - `main.py`: Käyttöliittymä, pääsilmukka ja komentojen käsittely.
 - `peli/luokat.py`: Luokkamäärittelyt.
 - `peli/maailma.py`: Kartan ja alueiden luonti.
 - `peli/tallennus.py`: Tiedostojenkäsittely kuten JSON-tallennus, lataus ja tekstiluonti.

 ### Toiminnallisuudet
 - **Maailmassa liikkuminen:** Pelaaja voi tutkia ympäristöä ja liikkua eri ilmansuuntiin alueiden välillä.
- **Ympäristön tutkiminen (`katso`):** Pelaaja voi tarkistaa nykyisen sijaintinsa kuvauksen ja katsoa, onko alueella roskia.
- **Interaktiivinen inventaario (`kerää`, `status`):** Roskat voi kerätä reppuun ja repun sisältöä voi tarkastella milloin tahansa.
- **Kierrätysmekaniikka (`kierrätä`):** Kerätyt roskat voidaan palauttaa vain kierrätyskeskuksessa, joka tarkistaa voiko peliä voittaa vielä.
- **Pelitilanteen tallennus ja lataus (`tallenna`):** Pelitilanne (pelaajan nimi, sijainti ja repun sisältö) voidaan tallentaa JSON-muotoiseen tiedostoon (`pelin_tallennus.json`) ja jatkaa myöhemmin.
- **Automaattinen nollaus voittaessa:** Kun peli läpäistään, tallennustiedosto poistetaan automaattisesti.

### Kestävän kehityksen näkökulma
- Pelin mekaaninen tavoite osoittaa, että jokaisella pienellä teolla (roskan keräämisellä) on merkitystä kokonaisuuden ja luonnon pelastamisen kannalta.
- Peli osoittaa, että erilaisten jätteiden kerääminen ja niiden vieminen tarkoitettuihin kierrätyspisteisiin edellyttää ympäristön hyvinvointia.