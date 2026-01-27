# Sažetak sigurnosne analize – Web Tracking Forensics

## Opseg analize

Sigurnosna analiza provedena je nad mrežnim prometom generiranim tijekom uobičajenog
korištenja web stranica, s ciljem otkrivanja i razumijevanja mehanizama web
praćenja korisnika. Analiza je usmjerena na promatranje stvarnog ponašanja web
stranica iz perspektive krajnjeg korisnika, bez izmjena ili manipulacije sadržajem
samih stranica.

Fokus analize bio je na mrežnoj komunikaciji koja se odvija u pozadini pregledavanja
weba, a koja često nije vidljiva korisnicima. Posebna pažnja posvećena je
identifikaciji vanjskih servisa koji sudjeluju u prikupljanju podataka te
razlikovanju nužne funkcionalne komunikacije od komunikacije povezane s praćenjem
korisnika.

Analiza je obuhvatila sljedeće aspekte:

- HTTP i HTTPS mrežne zahtjeve generirane prilikom učitavanja web stranica
- razlikovanje first-party i third-party komunikacije
- korištenje kolačića unutar mrežnih zahtjeva
- vanjske domene koje sudjeluju u analitici, oglašavanju i drugim oblicima praćenja
- obrasce ponašanja karakteristične za web trackere, poput ponavljanja istih domena
  na više nepovezanih web stranica

Ukupno je analiziran mrežni promet prilikom posjeta **20 različitih web stranica**
iz različitih kategorija, čime je osigurana reprezentativnost dobivenih rezultata
i mogućnost usporedbe različitih tipova web servisa.

---

## Posjećene web stranice

Analiza je provedena nad prometom generiranim prilikom posjeta web stranicama iz
različitih područja, uključujući tražilice, informativne portale, društvene mreže,
e-commerce platforme i edukacijske servise. Odabir raznolikih web stranica omogućio
je uočavanje razlika u intenzitetu i vrsti web praćenja među različitim kategorijama
servisa.

Popis analiziranih web stranica uključuje:

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

Navedene web stranice obuhvaćaju širok raspon funkcionalnosti i poslovnih modela,
što je omogućilo uočavanje razlika u korištenju tracking tehnologija. Analiza je
pokazala da su mehanizmi web praćenja prisutni u svim kategorijama stranica, ali se
njihov opseg i složenost razlikuju ovisno o vrsti servisa i njegovoj namjeni.

Dobiveni skup podataka predstavlja čvrstu osnovu za daljnju analizu distribucije
trackera, procjenu intenziteta praćenja te vizualizaciju odnosa između web stranica
i third-party domena.

---

## Metodologija analize

Analiza web praćenja provedena je korištenjem forenzičkog pristupa temeljenog na
presretanju i analizi mrežnog prometa. Metodologija se oslanja na promatranje stvarne
mrežne komunikacije koja se odvija tijekom uobičajenog korištenja web stranica, bez
izmjena aplikacijskog koda ili ponašanja preglednika. Time je osigurano da
prikupljeni podaci vjerno odražavaju stvarne mehanizme web praćenja kojima su
korisnici izloženi.

Središnji element metodologije je **intercepting proxy**, koji omogućuje
presretanje HTTP i HTTPS zahtjeva u stvarnom vremenu. Presretnuti promet obrađivan
je pomoću vlastitih Python skripti koje su razvijene za filtriranje, klasifikaciju
i analizu prikupljenih podataka. Obrada i analiza podataka provedene su postupno,
kroz više faza, kako bi se osigurala konzistentnost i ponovljivost rezultata.

Prikupljeni i obrađeni podaci pohranjeni su u relacijsku bazu podataka, što je
omogućilo jednostavno izvođenje upita, statističku analizu i daljnju obradu
rezultata. Konačno, dobiveni podaci korišteni su za grafičku vizualizaciju odnosa
između web stranica i third-party trackera, čime su složeni odnosi predstavljeni na
intuitivan i pregledan način.

---

### Korišteni alati

Za provedbu analize korištena je kombinacija specijaliziranih alata i vlastitih
skripti, pri čemu svaki alat ima jasno definiranu ulogu u analitičkom procesu.
Intercepting proxy alat korišten je za snimanje HTTP i HTTPS mrežnog prometa,
dok su Python skripte služile za obradu, klasifikaciju i analizu prikupljenih
podataka. Strukturirana pohrana podataka ostvarena je korištenjem SQLite baze
podatataka, a grafička analiza i vizualizacija provedene su pomoću alata Gephi.

Ovakva kombinacija alata omogućila je fleksibilan i modularan pristup analizi, uz
mogućnost jednostavnog proširenja metodologije u budućim istraživanjima.

---

### Analizirani podaci

Analiza se temeljila na detaljnoj obradi ključnih elemenata svakog mrežnog zahtjeva.
Za svaki presretnuti zahtjev analizirani su URL i odredišna domena, korištena HTTP
metoda te prisutni kolačići. Posebna pažnja posvećena je User-Agent zaglavlju, koje
pruža informacije o pregledniku i operativnom sustavu korisnika, kao i oznaci
first-party odnosno third-party zahtjeva.

Dodatno, svaki third-party zahtjev klasificiran je prema kategoriji trackera, što
je omogućilo razlikovanje analitičkih, oglašivačkih, društvenih i telemetrijskih
servisa. Analizom navedenih podataka dobiven je cjelovit uvid u strukturu mrežnog
prometa, učestalost vanjske komunikacije i opseg web praćenja prisutnog na
analiziranim web stranicama.

---

## Rezultati analize

### Ukupni statistički pregled

Tijekom analize mrežnog prometa prikupljenog prilikom posjeta dvadeset različitih
web stranica zabilježen je velik broj HTTP i HTTPS zahtjeva. Ukupan broj
analiziranih zahtjeva iznosio je **7.556**, što jasno pokazuje količinu mrežne
komunikacije koja se odvija u pozadini čak i tijekom kratkotrajnog i uobičajenog
pregledavanja web sadržaja.

Značajan dio ukupnog prometa čine **third-party zahtjevi**, odnosno zahtjevi koji se
ne upućuju prema domeni trenutno posjećene web stranice, već prema vanjskim
servisima. Ovi zahtjevi predstavljaju temeljni mehanizam web praćenja, budući da
omogućuju razmjenu podataka između različitih web stranica i istih vanjskih
domena.

Analiza je identificirala **više desetaka jedinstvenih tracking domena**, od kojih se
mnoge pojavljuju na većem broju nepovezanih web stranica. Takvo ponavljanje istih
domena ukazuje na postojanje centraliziranih tracking servisa koji prate korisnike
kroz različite dijelove weba.

Detektirani trackeri klasificirani su u nekoliko kategorija, uključujući
**analytics**, **advertising**, **social**, **telemetry** i **other**. Ovakva
klasifikacija omogućila je jasniji uvid u svrhu pojedinih zahtjeva te razlikovanje
između funkcionalnih servisa i onih čija je primarna svrha praćenje ponašanja
korisnika.

| Kategorija | Vrijednost |
|----------|-----------|
| Ukupan broj analiziranih zahtjeva | 7.556 |
| Third-party zahtjevi | značajan udio ukupnog prometa |
| Jedinstvene tracking domene | više desetaka |
| Korištene kategorije trackera | analytics, advertising, social, telemetry, other |

---

## Očekivano vs. uočeno ponašanje

### Očekivano ponašanje

Prije provedbe analize pretpostavljalo se da će većina mrežnog prometa biti
vezana uz **first-party komunikaciju**, odnosno komunikaciju između korisnikovog
preglednika i domene web stranice koju korisnik izravno posjećuje. Očekivalo se da
će third-party zahtjevi biti prisutni u manjem opsegu te uglavnom ograničeni na
osnovne servise poput analitike ili učitavanja statičkih resursa.

Također se pretpostavljalo da će komunikacija s vanjskim servisima biti relativno
transparentna i predvidiva, odnosno da će biti jasno poveziva s vidljivim
funkcionalnostima web stranice (npr. video playeri, društvene mreže ili alati za
analitiku). U tom kontekstu očekivalo se da će korisnik imati barem djelomičnu
kontrolu ili svijest o tome kada i zašto dolazi do razmjene podataka s trećim
stranama.

---

### Uočeno ponašanje

Rezultati analize pokazali su znatno drukčiju sliku stvarnog ponašanja web
stranica. Većina analiziranih web stranica uspostavlja **komunikaciju s velikim
brojem third-party domena**, često već pri samom učitavanju početne stranice, bez
ikakve dodatne interakcije korisnika.

Uočeno je da se pojedine tracking domene pojavljuju na velikom broju međusobno
nepovezanih web stranica, što ukazuje na **centralizirane tracking servise** koji
omogućuju praćenje korisnika kroz različite dijelove weba. Takvi servisi često
prikupljaju podatke pasivno, u pozadini, bez jasne ili vidljive naznake korisniku.

Posebno je značajno da se velik dio tracking komunikacije odvija **automatski i
neprimjetno**, neovisno o korisnikovim radnjama poput klikanja ili ispunjavanja
obrazaca. Time se potvrđuje da web praćenje nije vezano isključivo uz aktivno
ponašanje korisnika, već je duboko integrirano u samu infrastrukturu modernih web
stranica.

Ovakvo uočeno ponašanje ukazuje na znatno veći opseg i kompleksnost web praćenja
nego što bi prosječan korisnik mogao očekivati, te dodatno naglašava važnost
forenzičke analize mrežnog prometa u kontekstu privatnosti i sigurnosti korisnika.
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

Grafovska vizualizacija odnosa između web stranica i tracking domena omogućila je
jasan i intuitivan uvid u strukturu web praćenja. Prikaz je pokazao postojanje
**centraliziranih tracking domena** koje ostvaruju velik broj veza s različitim web
stranicama, što ukazuje na njihovu dominantnu ulogu u ekosustavu web praćenja.

Uočeno je da se isti trackeri pojavljuju na velikom broju nepovezanih web stranica,
pri čemu ostvaruju značajan broj veza. Takav obrazac jasno upućuje na mogućnost
praćenja korisnika kroz više različitih domena, bez obzira na vrstu ili namjenu
posjećene web stranice.

Primjenom **ForceAtlas** algoritma formiran je gusti centralni klaster koji
predstavlja dominantne tracking servise, dok su pojedine web stranice raspoređene
prema intenzitetu i učestalosti njihove komunikacije s trećim stranama. Ovakva
vizualizacija omogućila je lakšu identifikaciju najaktivnijih trackera te web
stranica s izrazito visokim intenzitetom praćenja.

---

## Sigurnosna procjena

Na temelju provedene analize mrežnog prometa i detekcije web trackera može se
zaključiti da je **web praćenje izrazito rasprostranjena praksa** na modernim web
stranicama. Gotovo sve analizirane stranice uspostavljaju komunikaciju s jednim ili
više vanjskih servisa koji nisu nužno povezani s osnovnom funkcionalnošću same
web stranice.

Velik dio prikupljenih podataka prenosi se putem **third-party servisa**, koji se
često pojavljuju na velikom broju nepovezanih web stranica. Takvi servisi imaju
potencijal za korelaciju korisničkih aktivnosti kroz različite domene, čime se
omogućuje izgradnja detaljnog profila korisničkog ponašanja bez izravnog znanja ili
svjesne interakcije korisnika.

Analiza je također pokazala da korisnici u većini slučajeva **nisu svjesni opsega
mrežne komunikacije** koja se odvija u pozadini. Značajan broj zahtjeva generira se
automatski prilikom učitavanja stranice, bez ikakvog vidljivog indikatora prema
korisniku. Iako se na mnogim stranicama prikazuju obavijesti o kolačićima, stvarni
opseg praćenja često nadilazi ono što korisnik može lako razumjeti ili kontrolirati.

---

### Procjena razine praćenja

Na temelju količine third-party zahtjeva, broja jedinstvenih tracking domena te
njihove prisutnosti na više različitih web stranica, procijenjena je ukupna razina
praćenja korisnika.

**Razina praćenja:** Visoka  
Analizirani web ekosustav pokazuje intenzivnu upotrebu vanjskih servisa za analitiku,
oglašavanje, društvene integracije i telemetriju, što rezultira velikom količinom
prikupljenih podataka.

**Transparentnost prema korisniku:** Niska do umjerena  
Iako su osnovne informacije o kolačićima često formalno prikazane, stvarni mehanizmi
praćenja odvijaju se u pozadini i teško su uočljivi bez tehničke analize mrežnog
prometa. Time je korisniku otežano donošenje informiranih odluka o vlastitoj
privatnosti.

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

---

## Zaključak

Provedena sigurnosna analiza pokazala je da je **web praćenje široko rasprostranjena
praksa** na modernim web stranicama te da većina analiziranih stranica koristi velik
broj **third-party servisa** već pri samom učitavanju sadržaja. Takva komunikacija
odvija se u pozadini, često bez jasne svijesti korisnika o opsegu razmjene podataka.

Analiza je također otkrila postojanje **centraliziranih tracking domena** koje se
ponavljaju na velikom broju nepovezanih web stranica, što upućuje na mogućnost
praćenja korisnika kroz različite dijelove weba. Vizualna analiza dodatno je
potvrdila ovu pojavu kroz izražene centralne čvorove u grafu mrežnog praćenja.

Korištena metodologija presretanja mrežnog prometa i grafovske analize pokazala se
učinkovitom za forenzičku analizu privatnosti, čineći razvijeni sustav pouzdanom
osnovom za daljnja istraživanja u području sigurnosti informacijskih sustava.


