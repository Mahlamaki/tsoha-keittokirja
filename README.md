# Web keittokirja

## Toinen välipalautus

Sovellus on vielä aivan kesken. Valitettavasti en saanut tähän vielä aikaiseksi mitään toimivuutta. Tietokaintoihin yhdistämiseen opettelussa meni tuhottoman paljon aikaa
joten itse sovelluksen kehitykseen ei minun kohdallani nyt jäänyt juuri ollenkaan aikaa. Tästä keskeneräisestä versiosta löytyy vasta:

-tieto kahdesta ensimmäisestä taulusta
-kaksi html sivua (etusivu ja sivu uuden reseptin luomiseksi), mutta näiden välillä ei pysty vielä liikkumaan. 

Sain nyt tietokannat toimimaan, mutta en valitettavasi niitä tähän palautukseen ole vielä saanut hyödynnettyä. Olen kuitenkin luonut tietokantaan taulut recipe ja category. 

Tähän päättyy välipalautusta varten tehty kommentti. Alla aiemmin kirjattua sovelluksen suunnittelua.


Keittokirjaprojekti on vielä täysin keskeneräinen. Toistaiseksi löydät tästä alta vain tulevan web-keittokirjan mahdollisia tulevia keskeisimpiä toimintoja. Web keittokirjalla ei ole vielä nimeä.

### Keskeisimpiä toimintoja

Käyttäjät pystyvät muunmuassa:

- luomaan käyttäjätunnuksen ja salasanan
- luoda reseptejä
- kommentoida omia ja toisten reseptejä
- poistaa itse tehdyn reseptin tai itse tehdyn kommentin
- tallentaa resepti omiin "suosikkeihin"
- voi nähdä muiden tekemät reseptit
- nähdä lajiteltuja reseptejä (lajiteltu esim. pääruokiin, alkupaloihin ja jälkiruokiin) tästä omat näppäimet sivuston yläreunassa.

Keittokirjaan voi lisätä myös mahdollisia muita toimintoja; harkinnassa muun muassa reseptien arvostelu, reseptien lisäyspäivän ja 
kommenttejen lähetysaikojen päivämäärien ja kellonaikojen näyttäminen jne.


## Käynnistysohjeet

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon:

git clone git@github.com:Mahlamaki/tsoha-keittokirja.git

cd keittokirja


Luo kansioon .env-tiedosto ja tallenna sen sisällöksi tietokannan paikallinen osoite ja salainen avain:

DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>


Aktivoi virtuaaliympäristö ja asenna tarvittavat riippuvuudet seuraavien ohjeiden mukaisesti:

python3 -m venv venv
source venv/bin/activate
pip install flask-sqlalchemy
pip install psycopg2
pip install python-dotenv


Määritä skeema tietokannalle:
HUOM! Jos sinulla on tietokannassasi saman nimisiä tauluja (recipe, category), sinun kannattaa luoda tätä varten toinen tietokanta. Tähän ohjeet löytyy kurssimateriaalista.

psql < schema.sql

Käynnistä sovellus:

flask run
