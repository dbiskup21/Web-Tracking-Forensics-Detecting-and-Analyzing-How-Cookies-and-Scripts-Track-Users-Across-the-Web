# Teorijska pozadina – Web Tracking Forensics

Ovaj dokument opisuje teorijsku osnovu projekta *Web Tracking Forensics* te objašnjava ključne koncepte vezane uz web praćenje korisnika, vrste trackera i metode njihove analize.

---

## 1. Web Tracking – osnovni koncept

Web tracking označava skup tehnika i tehnologija kojima web stranice i povezani vanjski servisi prate ponašanje korisnika tijekom pregledavanja interneta. Praćenje se najčešće odvija automatski i neprimjetno za korisnika, a temelji se na prikupljanju i analizi mrežnih zahtjeva, identifikatora i pohranjenih podataka na korisničkom uređaju.

Primarni ciljevi web trackinga uključuju analizu korištenja web stranica, personalizaciju sadržaja, optimizaciju oglašavanja te prikupljanje telemetrijskih podataka o performansama sustava. Osim toga, napredni oblici praćenja omogućuju praćenje korisnika kroz više različitih web stranica, čime se stvara detaljan profil korisničkog ponašanja.

Praćenje se najčešće provodi putem mrežnih zahtjeva koji se šalju tijekom učitavanja web stranice. Uz zahtjeve prema vlastitoj domeni web stranice (first-party zahtjevi), često se pojavljuju i zahtjevi prema vanjskim domenama (third-party zahtjevi). Te vanjske domene najčešće pripadaju analitičkim platformama, oglašivačkim mrežama ili društvenim servisima.

Tehnologije koje se koriste za web tracking uključuju HTTP kolačiće, lokalnu pohranu preglednika, piksele za praćenje, JavaScript biblioteke te tehnike fingerprintinga. Kombinacijom navedenih metoda moguće je identificirati korisnika ili njegov uređaj čak i bez izravne autentifikacije, što otvara značajna pitanja vezana uz privatnost i zaštitu osobnih podataka.

Razumijevanje osnovnih koncepata web trackinga ključno je za analizu mrežnog prometa, identifikaciju trackera te procjenu razine praćenja kojoj su korisnici izloženi tijekom korištenja modernih web aplikacija.

---
## 2. First-party i Third-party tracking

Web tracking može se podijeliti na first-party i third-party praćenje, ovisno o tome prema kojim domenama se mrežni zahtjevi šalju i tko ima kontrolu nad prikupljenim podacima. Ova podjela ključna je za razumijevanje načina na koji se podaci o korisnicima prikupljaju, obrađuju i dijele između različitih subjekata na webu.

---

### 2.1 First-party zahtjevi

First-party zahtjevi su mrežni zahtjevi koji se šalju prema istoj domeni koju korisnik izravno posjećuje. Takvi zahtjevi generiraju se kao dio osnovne funkcionalnosti web stranice i u pravilu su nužni za njezino ispravno djelovanje.

Primjeri first-party zahtjeva uključuju učitavanje statičkih resursa poput slika, CSS i JavaScript datoteka, kao i API pozive unutar iste web aplikacije koji omogućuju dohvaćanje podataka, autentifikaciju korisnika ili spremanje korisničkih postavki.

First-party tracking često se koristi za osnovnu analitiku, poput praćenja broja posjeta, navigacije unutar web stranice ili poboljšanja korisničkog iskustva. Budući da se podaci prikupljaju i obrađuju unutar iste domene, first-party praćenje se općenito smatra manje invazivnim u odnosu na third-party praćenje, iako i dalje može uključivati obradu osobnih podataka.

Važno je naglasiti da first-party zahtjevi ne znače nužno potpunu zaštitu privatnosti korisnika. Web stranice i dalje mogu koristiti kolačiće, local storage ili druge mehanizme za praćenje ponašanja korisnika unutar vlastitog sustava. Međutim, prikupljeni podaci u tom slučaju ne dijele se izravno s vanjskim servisima.

---

### 2.2 Third-party zahtjevi

Third-party zahtjevi su mrežni zahtjevi koji se šalju prema vanjskim domenama koje nisu domena web stranice koju korisnik trenutačno posjećuje. Ovi zahtjevi najčešće nastaju kao rezultat integracije vanjskih servisa unutar web stranice, poput analitičkih alata, oglasnih mreža ili društvenih mreža.

Uobičajeni primjeri third-party zahtjeva uključuju:
- analitičke servise, poput Google Analyticsa, koji prate ponašanje korisnika na web stranici  
- oglasne mreže, poput DoubleClicka, koje omogućuju prikaz i ciljanje oglasa  
- društvene mreže, poput Facebooka ili TikToka, koje koriste ugrađene widgete i piksele za praćenje  
- telemetrijske servise i mreže za isporuku sadržaja (CDN), koje prikupljaju podatke o performansama i korištenju

Za razliku od first-party praćenja, third-party tracking omogućuje praćenje korisnika preko više različitih web stranica. Budući da isti third-party servis može biti integriran na velikom broju web stranica, on može povezati aktivnosti korisnika u jedinstveni profil, čak i ako korisnik nikada izravno ne posjeti web stranicu tog servisa.

Ovakav oblik praćenja predstavlja značajan izazov za privatnost korisnika. Third-party servisi često prikupljaju velike količine podataka, uključujući informacije o posjećenim stranicama, vremenu zadržavanja, tipu uređaja i lokaciji. Zbog toga je third-party tracking u središtu regulatornih rasprava i zakonskih ograničenja, poput Opće uredbe o zaštiti podataka (GDPR).

U kontekstu ovog projekta, third-party zahtjevi predstavljaju glavni fokus analize. Identifikacijom i klasifikacijom third-party zahtjeva moguće je procijeniti razinu praćenja kojoj su korisnici izloženi te analizirati ulogu pojedinih trackera unutar web ekosustava.

---
## 3. Mehanizmi web praćenja

Web praćenje provodi se korištenjem različitih tehničkih mehanizama koji omogućuju identifikaciju korisnika, praćenje njegovog ponašanja i povezivanje aktivnosti kroz vrijeme i različite web stranice. Najčešći mehanizmi uključuju kolačiće, analizu mrežnih zahtjeva i zaglavlja te napredne tehnike poput fingerprintinga.

---

### 3.1 Kolačići (Cookies)

Kolačići su male tekstualne datoteke koje web stranica pohranjuje u preglednik korisnika. Oni predstavljaju jedan od najraširenijih i najstarijih mehanizama web praćenja te se koriste kako za funkcionalne, tako i za analitičke i marketinške svrhe.

Kolačići se često koriste za:
- identifikaciju korisnika ili korisničke sesije
- održavanje prijavljenog stanja (session management)
- pohranu korisničkih postavki
- praćenje ponašanja korisnika kroz dulje vremensko razdoblje

Tracking kolačići omogućuju prepoznavanje korisnika pri ponovnom posjetu web stranici ili, u slučaju third-party kolačića, na različitim web stranicama koje koriste isti vanjski servis. Takvi kolačići često imaju dulji rok trajanja i služe za izgradnju korisničkih profila.

Poznati primjeri tracking kolačića uključuju:
- `_ga`, koji koristi Google Analytics za razlikovanje korisnika
- `_fbp`, koji koristi Facebook Pixel za praćenje interakcija i oglašavanje

Zbog utjecaja na privatnost, uporaba kolačića regulirana je zakonodavstvom poput GDPR-a i ePrivacy direktive, što zahtijeva informiranje korisnika i pribavljanje privole za njihovo korištenje.

---

### 3.2 URL parametri i request metadata

Osim kolačića, web praćenje se može provoditi i analizom podataka koji se prenose unutar samih mrežnih zahtjeva. Ovi podaci često ne zahtijevaju pohranu informacija na korisničkom uređaju, što ih čini teže uočljivima za krajnjeg korisnika.

Praćenje se može temeljiti na:
- jedinstvenim identifikatorima uključenima u URL parametre
- zaglavlju User-Agent, koje otkriva informacije o pregledniku i operativnom sustavu
- IP adresi korisnika, koja omogućuje približnu geolokaciju i korelaciju sesija
- Referer zaglavlju, koje otkriva s koje je stranice zahtjev poslan

Kombinacijom ovih podataka moguće je pratiti korisničko kretanje između stranica, analizirati obrasce ponašanja i povezati više zahtjeva u jedinstvenu sesiju. Iako se ovi mehanizmi često smatraju manje invazivnima od kolačića, njihova kombinacija može omogućiti relativno precizno profiliranje korisnika.

---

### 3.3 Fingerprinting

Fingerprinting predstavlja napredniji i sofisticiraniji oblik web praćenja koji ne zahtijeva pohranu podataka u preglednik korisnika. Umjesto toga, temelji se na prikupljanju karakteristika uređaja i preglednika koje su dovoljno jedinstvene da omoguće identifikaciju korisnika.

Fingerprinting se najčešće temelji na kombinaciji:
- vrste i verzije preglednika
- operativnog sustava
- rezolucije ekrana i postavki prikaza
- dostupnih fontova i plug-inova
- ponašanja JavaScript API-ja i performansi sustava

Za razliku od kolačića, fingerprinting je znatno teže blokirati i često se provodi bez znanja ili privole korisnika. Zbog toga predstavlja značajan izazov za zaštitu privatnosti te je predmet intenzivnih istraživanja i regulatornih rasprava.

Iako ovaj projekt ne provodi potpunu analizu fingerprintinga, tijekom analize mrežnog prometa uočeni su obrasci koji mogu ukazivati na fingerprinting-like ponašanje, poput učestalih zahtjeva s bogatim skupovima zaglavlja i parametara koji otkrivaju detaljne informacije o korisničkom okruženju.

---


