# Web keittokirja

## Kolmas välipalautus

Sovelluksesta tulee virtuaalinen keittokirja, jossa käyttäjä pystyy selailemaan omia ja muiden tallentamia reseptejä. Reseptin pystyy luomaan ja (oman reseptin) poistamaan vain sisään kirjautunut käyttäjä, mutta reseptejä voi selailla, vaikka ei olisikaan kirjautuneena. Reseptejä pystyy järjestämään ruokalajin mukaan ja käyttäjä pystyy tallentamaan reseptejä suosikkeihinsa. Kirjautunut pystyy myös tarkastelemaan omilla sivuillaan omia reseptejään.

Kaikkia toimintoja en ole ehtinyt vielä toteuttamaan, lisäksi sovelluksen ulkoasu ja tietoturva vaativat vielä työtä.

Keittokirjaprojekti on vielä  keskeneräinen. Alla listausta toiminnoista, jotka on jo toteutettu (yliviivatut) ja joitka odottavat vielä toteutusta:

### Keskeisimpiä toimintoja

Käyttäjät pystyvät muunmuassa:

- ~~luomaan käyttäjätunnuksen ja salasanan~~
- ~~luoda reseptejä~~
- ~~poistaa itse tehdyn reseptin~~
- ~~tallentaa resepti omiin "suosikkeihin" ja poistaa sen suosikeista~~
- ~~voi selata muiden tekemiä reseptejä~~
- ~~nähdä lajiteltuja reseptejä (lajiteltu esim. pääruokiin, alkupaloihin ja jälkiruokiin)~~
- reseptille voi antaa tykkäyksen
- reseptejä selaillessa näkee sen tykkäyksien määrän
- pitää vielä laittaa rajoitukset inputteihin
- varmistaa, että kaikista tulee tarvittavat errorviestit
- käyttäjä voi poistaa oman tunnuksensa
- käyttäjä voi muuttaa salasanaansa




## Käynnistysohjeet

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon:
```
git clone git@github.com:Mahlamaki/tsoha-keittokirja.git

cd keittokirja
```

Luo kansioon .env-tiedosto ja tallenna sen sisällöksi tietokannan paikallinen osoite ja salainen avain:

```
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```

Aktivoi virtuaaliympäristö ja asenna tarvittavat riippuvuudet seuraavien ohjeiden mukaisesti:

```
python3 -m venv venv
source venv/bin/activate
pip install flask-sqlalchemy
pip install psycopg2
pip install python-dotenv
```

Määritä skeema tietokannalle:
HUOM! Jos sinulla on tietokannassasi saman nimisiä tauluja (recipe, category, favourites, users), sinun kannattaa luoda tätä varten toinen tietokanta. Tähän ohjeet löytyy kurssimateriaalista.

```
psql < schema.sql
```

Käynnistä sovellus:

```
flask run
```
