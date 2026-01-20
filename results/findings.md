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


