# Setup projekta – Web Tracking Forensics

Ovaj dokument opisuje kompletan postupak pokretanja projekta *Web Tracking Forensics*:  
od snimanja mrežnog prometa, preko obrade i analize podataka, do vizualizacije web trackera.

---

## Preduvjeti

Za pokretanje projekta potrebno je imati sljedeće alate:

- Python 3.10+
- pip
- mitmproxy
- Gephi
- DB Browser for SQLite (preporučeno)

---

## Struktura projekta

Projekt se sastoji od sljedećih skripti:

- tracker_logger.py – snimanje HTTP/HTTPS prometa pomoću mitmproxyja
- sanitize_log.py – sanitizacija i čišćenje sirovih logova
- log_to_db.py – spremanje podataka u SQLite bazu
- fix_third_party.py – ispravak third-party oznaka
- classify_trackers.py – klasifikacija trackera po kategorijama
- score_sites.py – procjena intenziteta praćenja po web stranicama
- export_graph.py – izvoz edge podataka za graf
- export_nodes.py – izvoz node podataka za graf
- check_db.py – provjera ispravnosti baze podataka

---

## 1. Snimanje mrežnog prometa

Prva faza projekta uključuje prikupljanje mrežnog prometa koji nastaje tijekom pregledavanja web stranica. Cilj ove faze je zabilježiti sve HTTP i HTTPS zahtjeve koje web preglednik generira, uključujući zahtjeve prema third-party domenama koje se koriste za analitiku, oglašavanje i druge oblike praćenja korisnika.

Prije početka snimanja potrebno je konfigurirati proxy postavke u operativnom sustavu kako bi sav mrežni promet bio usmjeren kroz lokalni proxy poslužitelj. Na taj način omogućeno je presretanje i zapisivanje zahtjeva u stvarnom vremenu.

### Postavke proxyja

- IP adresa: 127.0.0.1
- Port: 8080

Tijekom snimanja preporučuje se posjetiti najmanje dvadeset različitih web stranica iz različitih kategorija, poput informativnih portala, web trgovina, društvenih mreža i edukativnih stranica. Time se osigurava raznolik skup podataka za kasniju analizu.

Rezultat ove faze je datoteka traffic_log.json koja sadrži sve zabilježene mrežne zahtjeve.

---

## 2. Sanitizacija podataka

Sirovi mrežni logovi sadrže velik broj zapisa, uključujući podatke koji nisu relevantni za analizu praćenja te potencijalno osjetljive informacije. U ovoj fazi provodi se čišćenje i filtriranje prikupljenih podataka.

Proces sanitizacije uklanja nepotrebne zapise, normalizira formate podataka i reducira količinu informacija na one elemente koji su ključni za analizu web trackera. Time se podaci pripremaju za daljnju obradu i pohranu u bazu podataka.

Rezultat sanitizacije je datoteka traffic_log_sanitized.json.

---

## 3. Spremanje podataka u bazu

Nakon sanitizacije podaci se spremaju u relacijsku SQLite bazu podataka. Ova faza omogućuje strukturirano pohranjivanje mrežnih zahtjeva, jednostavno pretraživanje i izvođenje složenijih analiza.

Svaki mrežni zahtjev sprema se kao zapis u bazi, zajedno s pripadajućim metapodacima poput domene, tipa zahtjeva i oznake radi li se o first-party ili third-party komunikaciji.

Rezultat ove faze je baza podataka tracking.db, čija se ispravnost može dodatno provjeriti pomoću odgovarajućih alata za pregled SQLite baza.

---

## 4. Pregled baze podataka

Za dodatnu analizu i ručni pregled podataka moguće je otvoriti bazu tracking.db u alatu DB Browser for SQLite. Ovaj korak omogućuje pregled tablica, provjeru zapisa i validaciju rezultata dobivenih automatskom obradom.

Posebna pažnja posvećuje se tablicama koje sadrže mrežne zahtjeve i izračunate ocjene intenziteta praćenja.


## 5. Detekcija i klasifikacija trackera

U ovoj fazi provodi se identifikacija third-party zahtjeva te njihova klasifikacija prema vrsti praćenja. Analiziraju se domene koje ne pripadaju izravno posjećenoj web stranici kako bi se utvrdilo koriste li se za praćenje korisnika.

Trackeri se klasificiraju u unaprijed definirane kategorije, poput analytics, advertising, social i telemetry. Ova klasifikacija omogućuje bolji uvid u vrste praćenja prisutne na analiziranim web stranicama.

---

## 6. Procjena intenziteta praćenja

Za svaku analiziranu web stranicu izračunava se tracking intensity score, koji predstavlja kvantitativnu mjeru razine praćenja korisnika.

Ocjena se temelji na nekoliko faktora:
- ukupnom broju third-party zahtjeva
- broju jedinstvenih third-party domena
- vrstama i kategorijama identificiranih trackera

Na temelju izračuna moguće je usporediti web stranice i identificirati one s najintenzivnijim oblicima praćenja.

---

## 7. Izvoz podataka za graf

Kako bi se omogućila vizualna analiza odnosa između web stranica i trackera, podaci se izvoze iz baze u CSV format pogodan za grafičke alate.

Izvoze se dvije datoteke:
- graph_edges.csv, koja opisuje veze između web stranica i tracker domena
- graph_nodes.csv, koja sadrži popis svih čvorova i njihove atribute

Ovi podaci služe kao ulaz za grafičku vizualizaciju.

---

## 8. Vizualizacija u Gephi alatu

U alatu Gephi izrađuje se grafička vizualizacija odnosa između web stranica i trackera. Graf se sastoji od čvorova koji predstavljaju web stranice i tracker domene te bridova koji predstavljaju mrežne zahtjeve.

Za raspored čvorova koristi se ForceAtlas2 algoritam, koji omogućuje jasno grupiranje povezanih elemenata. Boje čvorova definirane su prema kategoriji trackera, dok se veličina čvorova prilagođava njihovoj povezanosti unutar grafa.

Vizualizacija omogućuje intuitivan uvid u strukturu web praćenja.

---
