# Testausdokumentti

Ohjelmaa on testattu automaattisilla yksikkötesteillä ja manuaalisella testauksella.

## Yksikkötestaus

### Sovelluslogiikka

Calculator-luokkaa testaa calculator_test luokka. Laskin alustetaan ja laskutoimituksia testataan.

### Repositorio

HistoryRepository-luokkaa testaa history_repo_test-luokka, tietokanta tyhjennetään ja alustetaan, ja testien lopuksi tyhjennetään uudestaan.

### Testauskattavuus

Testauskattavuus 82% ilman käyttöliittymää.

![Testaus](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/kuvat/Selection_173.png)

Testaamattä jäivät history_service, joka on vain yhteyskappale history_repoon, koska jostain syystä en saanut toimimaan ilman, sekä pari riviä calculator-luokasta.

## Järjestelmätestaus

Sovellusta on järjestelmätestattu manuaalisesti linux-ympäristössä. Kaikki toiminnallisuus on testattu, myös virheellisillä arvoilla.

## Sovellukseen jääneet laatuongelmat

Sovellus ei anna aina virheilmoitusta, esimerkiksi tyhjä tallennus ei vain toimi, käyttäjän pitää ymmärtää tajuta miksi se ei toimi.
