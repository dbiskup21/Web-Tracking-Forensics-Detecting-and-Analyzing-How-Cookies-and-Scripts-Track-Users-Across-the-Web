# Plan rada – Praktični dio projekta

Praktični dio projekta obuhvaća postavljanje radnog okruženja, snimanje mrežnog prometa web stranica, obradu i pohranu podataka, detekciju i klasifikaciju trackera te vizualizaciju i analizu dobivenih rezultata.

---

## FAZA 1 – Postavljanje radnog okruženja

U prvoj fazi postavljeno je razvojno okruženje za snimanje i analizu web prometa.

### Aktivnosti:
- instalacija Python okruženja
- instalacija alata **mitmproxy**
- konfiguracija proxy poslužitelja (127.0.0.1:8080)
- priprema skripti za snimanje mrežnog prometa

### Cilj faze:
- omogućiti presretanje i bilježenje HTTP/HTTPS zahtjeva web stranica

---

## FAZA 2 – Snimanje mrežnog prometa web stranica

U ovoj fazi sniman je mrežni promet prilikom posjeta web stranicama.

### Alati:
- mitmproxy
- custom Python skripta (`tracker_logger.py`)

### Aktivnosti:
- pokretanje mitmproxyja s vlastitom skriptom
- posjet najmanje 20 popularnih web stranica (news, e-commerce, social, educational)
- bilježenje HTTP zahtjeva, domena, URL-ova i kolačića

### Cilj faze:
- prikupiti sirove podatke o mrežnim zahtjevima i potencijalnim trackerima

---

## FAZA 3 – Obrada i sanitizacija podataka

Prikupljeni podaci obrađeni su kako bi se uklonili nepotrebni i osjetljivi elementi.

### Alati:
- Python (`sanitize_log.py`)

### Aktivnosti:
- čišćenje sirovih logova
- izdvajanje relevantnih informacija (visited_site, request_domain, URL, cookies)
- priprema podataka za daljnju pohranu i analizu

### Cilj faze:
- dobiti strukturirane i sigurne podatke za analizu

---

## FAZA 4 – Pohrana podataka u bazu

U ovoj fazi obrađeni podaci pohranjeni su u bazu podataka.

### Alati:
- SQLite
- Python (`log_to_db.py`, `check_db.py`)

### Aktivnosti:
- dizajn SQLite baze podataka
- spremanje mrežnih zahtjeva u tablicu `requests`
- provjera ispravnosti i sadržaja baze podataka

### Cilj faze:
- omogućiti centraliziranu i preglednu pohranu podataka

---

## FAZA 5 – Detekcija i klasifikacija trackera

U ovoj fazi provedena je analiza i klasifikacija mrežnih zahtjeva.

### Alati:
- Python (`fix_third_party.py`, `classify_trackers.py`)

### Aktivnosti:
- razlikovanje first-party i third-party zahtjeva
- klasifikacija trackera prema poznatim domenama
- kategorizacija u skupine: analytics, advertising, social, telemetry

### Cilj faze:
- identificirati i klasificirati trackere prisutne na web stranicama

---

## FAZA 6 – Procjena intenziteta praćenja

Na temelju prikupljenih podataka izračunat je intenzitet praćenja po web stranici.

### Alati:
- Python (`score_sites.py`)

### Aktivnosti:
- izračun broja third-party zahtjeva
- broj jedinstvenih tracker domena
- izrada ukupnog **tracking intensity score** po web stranici

### Cilj faze:
- usporediti web stranice prema razini praćenja korisnika

---

## FAZA 7 – Vizualizacija i analiza rezultata

U završnoj fazi rezultati su vizualizirani i analizirani.

### Alati:
- Gephi
- CSV export (`graph_nodes.csv`, `graph_edges.csv`)

### Aktivnosti:
- izrada grafova odnosa web stranica i trackera
- vizualizacija kategorija trackera bojama
- analiza centralnih i najaktivnijih tracker domena

### Cilj faze:
- jasno prikazati odnose između web stranica i trećih strana
- omogućiti interpretaciju rezultata i izradu završnog izvještaja

---

