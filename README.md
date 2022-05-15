
# Ohjelmistotekniikka-projekti
Perustoiminnallinen laskin

## Dokumentaatio


- [Tuntikirjanpito](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Testaus](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/testaus.md)


## Release
- [Viikko5](https://github.com/Scarrat/ot_harjoitustyo/releases/tag/viikko5)

## Käyttöohjeet:
### Asennus
```bash
poetry install
```

### Alkutoimet
```bash
poetry run invoke build
```
### Käynnistäminen
```bash
poetry run invoke start
```
### Testaus
```bash
poetry run invoke test
```
### Testikattavuusraportti
```bash
poetry run invoke coverage-report
```
### Pylint
```bash
poetry run invoke lint
```
