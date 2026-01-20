# Web Tracking Forensics  
**Detecting and Analyzing How Cookies and Scripts Track Users Across the Web**

Projekt je namijenjen za korištenje na kolegiju **Sigurnost informacijskih sustava** s ciljem analize i demonstracije
načina na koje web stranice koriste **cookies, skripte i mrežne zahtjeve** za praćenje korisnika na internetu.

---

## Cilj projekta

Cilj projekta je dizajnirati i implementirati okvir (framework) koji:

- nadzire korisnički web promet (HTTP/HTTPS),
- detektira cookie-based i cookie-less metode praćenja,
- bilježi i klasificira ponašanje trackera (treće strane),
- pohranjuje prikupljene dokaze za daljnju analizu,
- vizualizira odnose između web stranica i tracking domena
  (tj. koje treće strane “vide” korisnikovo pregledavanje).

---

## Originalni zadatak

Web tracking predstavlja skup tehnika kojima oglašivačke mreže, analitičke platforme i druge treće strane
prate ponašanje korisnika na internetu. To se postiže korištenjem:

- HTTP cookiesa (first-party i third-party),
- skripti za praćenje (analytics, pixels, beacons),
- fingerprinting tehnika (canvas, fonts, JS API-ji),
- mrežnih zahtjeva prema vanjskim domenama.

Zadatak projekta je forenzički analizirati te tehnike, identificirati trackere
i procijeniti razinu privatnosti koju pojedine web stranice nude korisniku.

---

## Praktična komponenta projekta

Projekt je podijeljen u više funkcionalnih cjelina:

### 1. Analiza mrežnog prometa
- Snimanje HTTP(S) prometa pomoću alata kao što su **Wireshark**, **mitmproxy** ili headless browser (npr. Puppeteer).
- Ekstrakcija cookiesa, HTTP headera i sumnjivih zahtjeva (beacons, tracking pixels).
- Identifikacija domena koje primaju podatke o korisniku.

### 2. Baza podataka i backend
- Dizajn baze podataka za pohranu:
  - imena cookiesa, domene, trajanja i postavki,
  - mrežnih zahtjeva (metoda, URL, parametri),
  - mapiranja između posjećenih stranica i tracking domena.
- Implementacija skripti za parsiranje prometa i spremanje podataka u bazu.

### 3. Detekcija i klasifikacija trackera
- Razlikovanje **first-party** i **third-party** cookiesa.
- Prepoznavanje poznatih tracking domena pomoću blocklista (EasyList, Disconnect).
- Detekcija potencijalnog fingerprintinga (JS biblioteke, canvas pozivi, neuobičajeno dugi parametri).
- Izračun “intenziteta praćenja” za pojedine web stranice.

### 4. Vizualizacija i izvještavanje
- Grafički prikaz odnosa *web stranica → tracker* (npr. D3.js, Gephi).
- Izrada nadzorne ploče (dashboard) koja prikazuje:
  - broj trackera po stranici,
  - kategorije trackera (oglašavanje, analitika, društvene mreže),
  - trajanje i količinu postavljenih cookiesa.
- Generiranje PDF/HTML izvještaja za potrebe “privacy audit-a”.

---

## Isporučivi rezultati (Deliverables)

1. Alat / framework za:
   - snimanje mrežnog prometa,
   - pohranu podataka u bazu,
   - vizualizaciju tracking odnosa.
2. Studija slučaja analize najmanje **20 popularnih web stranica**
   (npr. vijesti, e-commerce, društvene mreže, obrazovne stranice).
3. Završni izvještaj s tehničkom analizom i etičko-pravnom raspravom.
4. Prezentacija i demonstracija rada alata na stvarnoj web stranici.

---

