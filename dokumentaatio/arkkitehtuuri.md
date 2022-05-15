# Arkkitehtuuri

## Rakenne

UI sisältää käyttöliittymän, services sisältää konnektoriluokan, repositories sisältää tietokantaa hoitavan luokan ja entities sisältää laskin ja historia oliot.


![Pakkauskaavio](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/kuvat/luokkakaavio.png)


## Käyttöliittymä

Käyttöliittymässä on vain yksi näkymä laskimelle, josta vastaa UI luokka.

## Sovelluslogiikka

Sovelluslogiikasta vastaa calculator-luokka joka hoitaa laskutoimitusten laskemisen.

## Tietojen tallennus

Luokka history_repo vastaa laskuhistorian tallentamisesta tietokantaan. Tietokanta tallentaa laskutoimituksen ja sen päivämäärän ja kellonajan.

## Päätoiminnallisuus

Jos sovellukseen näppäillään laskutoimitus, painetaan yhtäkuin näppäintä ja tämän jälkeen tallennusnäppäintä, kontrolli etenee seuraavanlaisesti:
Sekvenssikaavio:

![Sekvenssikaavio](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/kuvat/Selection_168.png)

