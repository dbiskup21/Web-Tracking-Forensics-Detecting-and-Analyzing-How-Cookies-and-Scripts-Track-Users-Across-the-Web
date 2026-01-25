# Sažetak sigurnosne analize – Web Tracking Forensics

## Opseg analize

Sigurnosna analiza provedena je nad mrežnim prometom generiranim tijekom uobičajenog korištenja web stranica, s ciljem otkrivanja i analize mehanizama web praćenja korisnika.

Analiza je obuhvatila sljedeće aspekte sustava:

- HTTP i HTTPS mrežne zahtjeve
- First-party i third-party komunikaciju
- Korištenje kolačića u mrežnim zahtjevima
- Vanjske domene koje sudjeluju u praćenju korisnika
- Obrasce ponašanja karakteristične za web trackere

Ukupno je analiziran promet prilikom posjeta **20 različitih web stranica** iz različitih kategorija (informativne, tražilice, e-commerce, edukacijske stranice).

### Posjećene web stranice

Analiza je provedena na prometu generiranom prilikom posjeta web stranicama iz
različitih kategorija, uključujući:

- https://www.google.com  
- https://www.bing.com  
- https://www.wikipedia.org  
- https://www.chatgpt.com  
- https://docs.google.com  
- https://www.youtube.com  
- https://www.reddit.com  
- https://www.facebook.com  
- https://www.instagram.com  
- https://www.linkedin.com  
- https://www.twitter.com (X)  
- https://www.amazon.com  
- https://www.ebay.com  
- https://www.aliexpress.com  
- https://www.nytimes.com  
- https://www.bbc.com  
- https://www.stackoverflow.com  
- https://www.github.com  
- https://www.medium.com  
- https://www.coursera.org  

Navedene stranice obuhvaćaju informativne portale, tražilice, društvene mreže,
e-commerce platforme i edukacijske servise, čime je osigurana raznolikost
analiziranog mrežnog prometa.

---

## Metodologija analize

Analiza je provedena korištenjem **intercepting proxy** alata i vlastitih Python skripti za obradu podataka.

### Korišteni alati
- mitmproxy – snimanje HTTP/HTTPS prometa
- Python skripte – obrada, klasifikacija i analiza podataka
- SQLite – pohrana strukturiranih podataka
- Gephi – vizualizacija odnosa web stranica i trackera

### Analizirani podaci
- URL i odredišna domena svakog zahtjeva
- HTTP metoda
- Kolačići prisutni u zahtjevima
- User-Agent zaglavlja
- Oznaka first-party / third-party zahtjeva
- Kategorija trackera

---

## Rezultati analize

### Ukupni statistički pregled

| Kategorija | Vrijednost |
|----------|-----------|
| Ukupan broj analiziranih zahtjeva | 7,556 |
| Third-party zahtjevi | značajan udio |
| Jedinstvene tracking domene | više desetaka |
| Korištene kategorije trackera | analytics, advertising, social, telemetry, other |

---

### Distribucija trackera po kategorijama

Analiza je pokazala da su najzastupljeniji:

- **Analytics trackeri** – korišteni za mjerenje ponašanja korisnika
- **Advertising trackeri** – povezani s oglašivačkim mrežama
- **Social trackeri** – integracije društvenih mreža
- **Telemetry** – tehničko praćenje i dijagnostika
- **Other** – servisi koji ne spadaju u jasno definirane kategorije

Najveći broj zahtjeva dolazi iz kategorije *other*, što ukazuje na složenost i raznolikost web ekosustava.

---

## Očekivano vs. uočeno ponašanje

### Očekivano ponašanje
- Web stranice komuniciraju s ograničenim brojem vanjskih servisa
- First-party zahtjevi dominiraju mrežnim prometom
- Third-party komunikacija je transparentna i predvidiva

### Uočeno ponašanje
- Većina analiziranih web stranica ostvaruje komunikaciju s više third-party domena
- Pojedini trackeri pojavljuju se na velikom broju nepovezanih web stranica
- Tracking komunikacija često se odvija bez izravne interakcije korisnika

---

## Stabilnost i sigurnosni aspekti

Tijekom analize:

- nije došlo do prekida mrežnog prometa
- nije zabilježeno nepredvidivo ponašanje sustava
- nije došlo do rušenja alata za analizu
- prikupljeni podaci bili su konzistentni i ponovljivi

Sustav za analizu pokazao se stabilnim i prikladnim za forenzičku obradu mrežnog prometa.

---

## Vizualna analiza i interpretacija

Grafovska vizualizacija jasno je pokazala:

- postojanje **centraliziranih tracking domena**
- velik broj veza između različitih web stranica i istih trackera
- web stranice s izrazito visokim intenzitetom praćenja

Primjenom ForceAtlas algoritma uočen je gusti centralni klaster koji predstavlja dominantne tracking servise.

---

## Sigurnosna procjena

Na temelju provedene analize može se zaključiti da:

- web praćenje je široko rasprostranjeno
- velik dio praćenja odvija se putem third-party servisa
- korisnici često nisu svjesni opsega mrežne komunikacije koja se odvija u pozadini

### Procjena razine praćenja
**Razina praćenja:** Visoka  
**Transparentnost prema korisniku:** Niska do umjerena

---
## Fingerprinting – analiza i implikacije

### Pojam fingerprintinga

Fingerprinting predstavlja skup tehnika kojima web stranice i treće strane mogu
prepoznati i pratiti korisnika bez oslanjanja na kolačiće, kombiniranjem tehničkih
karakteristika preglednika i uređaja.

Za razliku od klasičnih kolačića, fingerprinting je:
- teže detektirati
- teže blokirati
- manje transparentan korisniku

---

### Fingerprinting indikatori u ovom projektu

U okviru ovog projekta nije provedeno aktivno prikupljanje fingerprinting podataka
na razini JavaScript koda, ali analiza mrežnog prometa omogućila je uočavanje
ključnih indikatora koji se koriste kao temelj fingerprintinga.

Uočeni su sljedeći elementi:

- **User-Agent zaglavlje**
  - tip i verzija preglednika
  - operativni sustav i platforma
  - arhitektura uređaja
- **Telemetry i analytics endpointi**
  - redovito slanje tehničkih podataka
  - ponavljanje istih obrazaca na više web stranica
- **Dosljedna prisutnost istih third-party domena**
  - iste tracking domene pojavljuju se na velikom broju nepovezanih stranica
- **Parametrizirani HTTP zahtjevi**
  - tipični za beacon i collect mehanizme

Kombinacijom navedenih podataka moguće je ostvariti stabilno prepoznavanje korisnika
bez korištenja kolačića.

---

### Povezanost fingerprintinga i third-party trackera

Analiza je pokazala da se velik broj tracking-capable servisa pojavljuje
istovremeno na više različitih web stranica.

Takva infrastruktura omogućuje:
- povezivanje korisničke aktivnosti kroz različite domene
- dugoročno praćenje korisnika
- izgradnju ponašajnih profila

Iako projekt ne rekonstruira identitet korisnika, jasno je vidljivo da mrežna
infrastruktura podržava fingerprinting mehanizme.

---

### Što projekt nije izravno mjerio

U ovom projektu nisu izravno analizirani sljedeći fingerprinting elementi:

- rezolucija ekrana i DPI
- instalirani fontovi
- Canvas i WebGL fingerprinting
- AudioContext fingerprinting
- precizna geolokacija korisnika

Navedeni podaci uobičajeno se prikupljaju putem JavaScript API-ja na strani klijenta
te nisu vidljivi isključivo analizom HTTP/HTTPS prometa.

---

### Sigurnosne i privatnosne implikacije

Rezultati analize ukazuju na to da fingerprinting:

- ne zahtijeva izričit pristanak korisnika
- može funkcionirati bez kolačića
- koristi široko rasprostranjenu third-party infrastrukturu

Zbog navedenog, fingerprinting predstavlja značajan izazov za zaštitu privatnosti
korisnika i transparentnost obrade podataka.

---

### Zaključak o fingerprintingu

Na temelju provedene analize može se zaključiti da:

- fingerprinting je tehnički izvediv već na razini mrežnog prometa
- third-party servisi omogućuju korelaciju aktivnosti korisnika
- korisnici nemaju jasan uvid u opseg prikupljenih podataka

Projekt *Web Tracking Forensics* uspješno pokazuje kako analiza mrežnog prometa
otkriva temeljne mehanizme fingerprintinga i predstavlja dobru osnovu za daljnja
istraživanja u području privatnosti i sigurnosti.



## Ograničenja analize

- Analiza nije obuhvatila lifetime kolačića
- Praćenje je provedeno u ograničenom vremenskom periodu
- Nisu analizirani JavaScript payloadi na razini izvornog koda

---

## Preporuke za poboljšanje

Na temelju dobivenih rezultata preporučuje se:

- detaljnija analiza trajanja i namjene kolačića
- dugoročno praćenje istih web stranica
- analiza fingerprinting tehnika (Canvas, WebGL, AudioContext)
- razvoj automatiziranog alata za kontinučnu analizu web praćenja

---

## Zaključak

Provedena sigurnosna analiza pokazala je da:

- web stranice koriste velik broj third-party servisa
- mrežni promet predstavlja vrijedan izvor podataka za forenzičku analizu privatnosti
- korištena metodologija uspješno otkriva obrasce web praćenja

Sustav razvijen u ovom projektu može se smatrati **učinkovitim alatom za analizu web trackinga** i dobrom osnovom za daljnja istraživanja u području sigurnosti informacijskih sustava.


