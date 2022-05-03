
# Ohjelmistotekniikka-projekti
Perustoiminnallinen laskin

## Dokumentaatio


- [Tuntikirjanpito](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/Scarrat/ot_harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)


## Release
- [Viikko5](https://github.com/Scarrat/ot_harjoitustyo/releases/tag/viikko5)

## Käyttöohjeet:
### Asennus
```bash
poetry install
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
