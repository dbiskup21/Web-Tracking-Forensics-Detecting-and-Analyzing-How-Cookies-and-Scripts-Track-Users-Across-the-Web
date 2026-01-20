# Izvještaj o sigurnosnoj analizi – Web Tracking Forensics

## 1.  Uvod i ciljevi

Cilj ovog projekta je **forenzička analiza web praćenja korisnika** kroz analizu HTTP/HTTPS mrežnog prometa nastalog tijekom uobičajenog pregledavanja web stranica.

### Glavni ciljevi
- Detekcija **third-party trackera** na web stranicama
- Identifikacija vanjskih domena koje primaju korisničke podatke

### Dodatni ciljevi
- Klasifikacija trackera prema namjeni (analytics, advertising, social, telemetry)
- Procjena intenziteta praćenja po web stranici
- Vizualizacija odnosa između web stranica i tracking domena

---

## 2.  Metodologija rada

### 2.1 Snimanje mrežnog prometa

**Alat:** mitmproxy  

- Sav mrežni promet preusmjeren je kroz lokalni proxy (`127.0.0.1:8080`)
- Presretani su HTTP i HTTPS zahtjevi u stvarnom vremenu
- Tijekom normalnog pregledavanja bilježeni su zahtjevi, kolačići i zaglavlja

**Rezultat:**
- `traffic_log.json` – sirovi zapis mrežnog prometa

---

### 2.2 Obrada i sanitizacija podataka

Sirovi zapisi sadržavali su redundantne i osjetljive podatke.

Provedeni su sljedeći koraci:
- Uklanjanje nepotrebnih zaglavlja
- Normalizacija zapisa zahtjeva
- Priprema podataka za pohranu i analizu

**Rezultat:**
- `traffic_log_sanitized.json`

---

## 3.  Pohrana podataka

**Baza podataka:** SQLite  

Podaci su pohranjeni u bazu `tracking.db` sa sljedećim atributima:
- visited_site
- request_domain
- url
- method
- cookies
- user_agent
- is_third_party

Ovakva struktura omogućuje učinkovitu analizu i filtriranje podataka.

---

## 4.  Detekcija i klasifikacija trackera

### 4.1 Detekcija third-party zahtjeva

Zahtjev se označava kao **third-party** ako se domena zahtjeva razlikuje od domene posjećene web stranice.

---

### 4.2 Klasifikacija trackera

Third-party domene automatski se klasificiraju u kategorije:
- Analytics
- Advertising
- Social
- Telemetry
- Other

Klasifikacija se temelji na:
- Poznatim tracking domenama
- Pravilima temeljenim na nazivima domena
- Heuristikama nad URL-ovima

Kategorija se sprema u bazu podataka za daljnju analizu.

---

## 5.  Procjena intenziteta praćenja

Za svaku web stranicu izračunat je **tracking intensity score**, koji uzima u obzir:
- Ukupan broj zahtjeva
- Broj third-party zahtjeva
- Broj jedinstvenih third-party domena
- Zastupljenost kategorija trackera
- Indikatore fingerprinting ponašanja

Na temelju toga web stranice se rangiraju prema razini praćenja.

---

## 6.  Vizualizacija podataka

### 6.1 Graf mrežnog praćenja

Podaci su izvezeni u grafovski format:
- **Čvorovi:** web stranice i tracking domene
- **Bridovi:** mrežni zahtjevi između njih

Vizualizacija je provedena u alatu **Gephi**, čime su jasno vidljivi:
- centralizirani tracking servisi
- dominantni third-party provideri
- web stranice s najintenzivnijim praćenjem

---

## 7.  Zaključak

Rezultati analize pokazuju da:
- Većina popularnih web stranica komunicira s više third-party servisa
- Mali broj domena djeluje kao centralni tracking čvorovi
- Analiza mrežnog prometa predstavlja učinkovit pristup forenzičkoj analizi privatnosti

### Ograničenja
- Lifetime kolačića nije eksplicitno analiziran
- Analiza se temelji na ograničenom vremenskom periodu pregledavanja

### Moguća proširenja
- Automatsko dohvaćanje trajanja kolačića
- Dugoročna analiza ponašanja trackera
- Izrada interaktivnog dashboarda
