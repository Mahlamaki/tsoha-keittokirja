# Web keittokirja

Tämä sovellus on virtuaalinen keittokirja, jossa kirjautunut käyttäjä pystyy selailemaan omia ja muiden tallentamia reseptejä. Reseptejä pystyy selailemaan ruokalajin mukaan ja käyttäjä pystyy tallentamaan reseptejä suosikkeihinsa sekä antamaan niille tykkäyksiä. 

Sovelluksen päätarkoituksena on siis pystyä pitämään kirjaa omista rakkaista resepteistä, ja jakamaan niitä myös toisten nähtäväksi. Suosikit- sivulle voi keräillä omista, ja muiden resepteistä talteen itselle mieluisimpia reseptejä, josta ne on sitten helppo löytää. Tykkäyksistä voi katsoa hieman osviittaa, mitä muut ovat tykänneet jostakin reseptistä, ja antaa itse tykkäämällä reseptin luoneelle hyvän mielen.

### Sovelluksen keskeisimpiä toimintoja


- käyttäjä voi luoda käyttäjätunnuksen ja salasanan
- kirjautunut voi luoda reseptejä
- kirjautunut voi poistaa itse luomansa reseptin
- kirjautunut voi tallentaa reseptin omiin "suosikkeihin" ja poistaa sen suosikeista
- kirjautunut voi selata muiden tekemiä reseptejä
- nähdä lajiteltuja reseptejä (lajiteltu esim. pääruokiin, alkupaloihin ja jälkiruokiin)
- reseptille voi antaa tykkäyksen ja perua tykkäyksen

## Sovelluksen jatkokehitysideoita


- käyttäjä voi poistaa oman tunnuksensa
- käyttäjä voi muuttaa salasanaansa
- sovellus kirjaisi käyttäjän ulos itsestään tietyn ajan kuluessa
- lajittelua voisi laajentaa muihinkin kategorioihin (välipalat, kasvisruoat..)
- reseptejä voisi filtteröidä esim tykkäyksien mukaan (suosituimmat ensin)
- itse luotua reseptiä voisi pystyä muokkaamaan
- sovelluksen ulkoasua voisi kehitellä käyttömukavemmaksi ja mielyttävämmän näköiseksi
- reseptien haku reseptin nimellä


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
pip install -r ./requirements.txt
```

Määritä skeema tietokannalle:
HUOM! Jos sinulla on tietokannassasi saman nimisiä tauluja (recipe, category, favourites, users, likes), sinun kannattaa luoda tätä varten toinen tietokanta. Tähän ohjeet löytyy kurssimateriaalista.

```
psql < schema.sql
```

Käynnistä sovellus:

```
flask run
```
