# Gaussin eliminaation välivaiheiden tex-generaattori

Ohjelma käyttää yleistä Gaussin eliminaatioalgoritmiä ratkaistakseen annetun matriisin.
Ohjelma tallentaa välivaiheet ja formatoi ne latex muotoiseksi ja latoo sen pdflatexia käyttäen.

## Asentaminen

Lataa projektin tiedostot kovalevylle.
Varmista, että tietokoneellasi on asennettuna [`python>3.9`](https://www.python.org/downloads/) sekä python-paketti Pandas: `pip install pandas`.

## Käyttö

Muokkaa projektikansion `gauss.csv` tiedostoa ratkaistavan matriisin muotoiseksi. Rivit erottuvat rivivaihdolla, alkiot pilkuilla. Käytä vain rationaalilukuja desimaalimuodossa tai murtolukuja /-merkkiä käyttäen.

Tämän jälkeen suorita `gauss.bat` tiedosto, minkä jälkeen kansioon ilmestyy gauss.tex-tiedosto sekä pdf kansio, jonne ladottu pdf-tiedosto ilmestyy, mikäli tietokoneella on asennettua latex-ladontajärjestelmä.
