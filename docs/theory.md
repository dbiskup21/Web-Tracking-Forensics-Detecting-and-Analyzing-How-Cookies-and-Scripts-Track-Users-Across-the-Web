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
## 4. Kategorije trackera

Kako bi se omogućila sustavna analiza mrežnog prometa i razumijevanje uloge pojedinih vanjskih servisa, u ovom projektu trackeri se klasificiraju u nekoliko kategorija. Klasifikacija se temelji na primarnoj svrsi trackera, vrsti podataka koje prikuplja te načinu na koji se ti podaci koriste.

Razvrstavanje trackera u kategorije omogućuje jasniji uvid u strukturu web praćenja te olakšava procjenu intenziteta i potencijalnog utjecaja praćenja na privatnost korisnika.

---

### 4.1 Analytics

Analytics trackeri služe za prikupljanje statističkih podataka o korištenju web stranica. Njihova primarna svrha je analiza ponašanja korisnika kako bi vlasnici web stranica mogli poboljšati sadržaj, funkcionalnost i korisničko iskustvo.

Ovi trackeri obično prikupljaju podatke poput broja posjeta, trajanja sesije, pregledanih stranica, izvora prometa i osnovnih informacija o uređaju ili pregledniku. Iako se analytics trackeri često smatraju manje invazivnima u odnosu na oglasne trackere, oni i dalje omogućuju praćenje korisnika kroz vrijeme, osobito ako se koriste persistentni identifikatori.

Primjeri analytics trackera uključuju:
- Google Analytics, koji omogućuje detaljnu analizu korisničkog ponašanja
- Google Tag Manager, koji služi kao posredni sloj za upravljanje različitim analitičkim i tracking skriptama

U kontekstu ovog projekta, analytics trackeri identificiraju se kao third-party zahtjevi čija je primarna svrha statistička analiza, a ne izravno oglašavanje.

---

### 4.2 Advertising

Advertising trackeri povezani su s oglasnim mrežama i sustavima za ciljanje korisnika. Njihova svrha je prikupljanje podataka koji se koriste za prikaz personaliziranih oglasa i mjerenje učinkovitosti oglašivačkih kampanja.

Ovi trackeri često prikupljaju detaljnije podatke o korisničkom ponašanju, uključujući informacije o posjećenim web stranicama, interesima i interakcijama s oglasima. Budući da su iste oglasne mreže prisutne na velikom broju web stranica, advertising trackeri omogućuju cross-site praćenje korisnika.

Primjeri advertising trackera uključuju:
- DoubleClick, koji je dio Googleove oglasne infrastrukture
- Amazon Ads, koji se koristi za ciljanje oglasa unutar i izvan Amazonovog ekosustava
- različite adservice domene koje služe kao posrednici u isporuci oglasa

Zbog svoje uloge u intenzivnom praćenju korisnika, advertising trackeri predstavljaju jedan od najvećih rizika za privatnost i često su u fokusu regulatornih ograničenja.

---

### 4.3 Social

Social trackeri povezani su s društvenim mrežama i njihovim vanjskim integracijama. Oni se najčešće pojavljuju u obliku ugrađenih elemenata, poput gumba za dijeljenje sadržaja, widgeta ili pikselâ za praćenje.

Ovi trackeri omogućuju društvenim mrežama prikupljanje podataka o korisničkoj aktivnosti čak i kada korisnik ne komunicira izravno s ugrađenim elementom. Na taj način moguće je povezati aktivnosti korisnika na različitim web stranicama s njegovim društvenim profilom.

Primjeri social trackera uključuju:
- Facebook tracking servise i piksele
- Twitter tracking skripte
- TikTok tracking endpointе

U kontekstu privatnosti, social trackeri su posebno osjetljivi jer omogućuju povezivanje web aktivnosti s identitetom korisnika na društvenim mrežama.

---

### 4.4 Telemetry

Telemetrijski trackeri prikupljaju tehničke podatke o radu aplikacija, preglednika i operativnih sustava. Njihova primarna svrha nije izravno praćenje korisničkog ponašanja, već praćenje performansi, stabilnosti i pouzdanosti sustava.

Telemetrijski podaci mogu uključivati informacije o greškama, vremenu učitavanja, verzijama softvera i konfiguraciji sustava. Iako se telemetrija često smatra tehnički nužnom, ona također može sadržavati identifikatore koji omogućuju povezivanje podataka s određenim korisnikom ili uređajem.

Primjeri telemetrijskih servisa uključuju:
- Microsoft telemetry servise ugrađene u preglednike i operativne sustave
- različite browser telemetry endpointe koji šalju podatke o performansama i greškama

U ovom projektu telemetrijski trackeri klasificiraju se zasebno kako bi se razlikovali od trackera čija je primarna svrha oglašavanje ili analitika, ali se i dalje uzimaju u obzir prilikom procjene ukupne razine praćenja.

---

Ova klasifikacija trackera omogućuje jasniju interpretaciju rezultata analize te pruža temelj za izračun intenziteta praćenja i vizualizaciju odnosa između web stranica i vanjskih servisa.

---

## 5. Forenzička analiza web prometa

Forenzička analiza web prometa predstavlja sustavan i metodološki pristup proučavanju mrežnih komunikacija koje nastaju tijekom korištenja web stranica. U kontekstu web trackinga, cilj forenzičke analize nije samo promatranje prometa, već razumijevanje skrivenih mehanizama praćenja koji se odvijaju u pozadini korisničkog iskustva.

Web tracking forensics usmjeren je na otkrivanje i analizu načina na koji web stranice i povezani vanjski servisi prikupljaju, razmjenjuju i obrađuju podatke o korisnicima. Ovakav pristup omogućuje dublji uvid u strukturu web ekosustava i odnose između različitih aktera uključenih u proces praćenja.

Glavni ciljevi forenzičke analize web prometa u ovom projektu uključuju:
- identifikaciju third-party servisa koji sudjeluju u učitavanju web stranica  
- razumijevanje odnosa između posjećenih web stranica i vanjskih tracking domena  
- kvantifikaciju razine praćenja kojoj je korisnik izložen tijekom pregledavanja interneta  

Analiza se temelji na presretanju i obradi HTTP i HTTPS zahtjeva koji nastaju prilikom učitavanja web stranica. Svaki zahtjev predstavlja potencijalni izvor informacija o vrsti servisa, svrsi komunikacije i ulozi pojedine domene u procesu praćenja.

U okviru ovog projekta posebna pažnja posvećena je analizi domena odredišta mrežnih zahtjeva. Identifikacijom domena koje ne pripadaju izravno posjećenoj web stranici moguće je razlikovati first-party i third-party komunikaciju. Third-party domene često ukazuju na prisutnost analitičkih alata, oglasnih mreža, društvenih mreža ili telemetrijskih servisa.

Nakon identifikacije, svaki third-party zahtjev povezuje se s pripadajućom kategorijom trackera, poput analytics, advertising, social ili telemetry. Ova klasifikacija omogućuje semantičko razumijevanje prikupljenog prometa te olakšava daljnju analizu i usporedbu web stranica.

Forenzička analiza također uključuje kvantitativni aspekt, pri čemu se mjeri broj third-party zahtjeva, broj jedinstvenih domena i raspodjela kategorija trackera po web stranicama. Na temelju tih podataka moguće je izračunati pokazatelje koji opisuju intenzitet praćenja korisnika.

Rezultati forenzičke analize čine temelj za kasnije faze projekta, uključujući izračun tracking intensity score, izradu grafičkih prikaza odnosa između web stranica i trackera te vizualizaciju strukture web praćenja. Time se omogućuje jasniji i objektivniji uvid u razinu i složenost web trackinga u stvarnom okruženju.

---

## 6. Vizualizacija kao analitički alat

Vizualizacija mrežnih odnosa predstavlja važan analitički alat u forenzičkoj analizi web prometa jer omogućuje intuitivno razumijevanje kompleksnih i višedimenzionalnih podataka. Umjesto promatranja pojedinačnih zapisa u tablicama ili bazama podataka, vizualizacija omogućuje sagledavanje cjelokupne strukture odnosa između web stranica, third-party domena i kategorija trackera.

U kontekstu web trackinga, vizualizacija se temelji na grafovima koji se sastoje od čvorova i bridova. Čvorovi mogu predstavljati web stranice ili tracking domene, dok bridovi predstavljaju mrežne zahtjeve koji povezuju te entitete. Takav grafički prikaz omogućuje jasnu interpretaciju odnosa koji bi inače bili teško uočljivi u sirovim podacima.

Vizualizacija mrežnih odnosa omogućuje lakše razumijevanje veza između:
- web stranica koje korisnik posjećuje  
- third-party domena koje sudjeluju u učitavanju sadržaja  
- različitih kategorija trackera, poput analytics, advertising, social i telemetry  

Grafički prikazi pomažu u identifikaciji dominantnih trackera, odnosno onih third-party domena koje se pojavljuju na velikom broju web stranica ili generiraju velik broj mrežnih zahtjeva. Takvi trackeri često imaju središnju ulogu u web ekosustavu i predstavljaju ključne točke praćenja korisnika.

Jedna od važnih prednosti vizualizacije je mogućnost uočavanja centralnih čvorova unutar mreže. Centralni čvorovi su oni koji imaju velik broj veza prema drugim čvorovima, što može ukazivati na široko rasprostranjene tracking servise ili web stranice s izuzetno intenzivnim praćenjem. Analizom centralnosti čvorova moguće je identificirati najutjecajnije aktere u procesu web trackinga.

Vizualizacija također omogućuje usporedbu intenziteta praćenja među različitim web stranicama. Web stranice koje su povezane s velikim brojem third-party domena ili s trackerima iz više kategorija mogu se lako razlikovati od onih s ograničenim ili minimalnim praćenjem. Time se omogućuje kvalitativna i kvantitativna usporedba razine praćenja.

Osim analitičke vrijednosti, vizualizacija ima i komunikacijsku ulogu. Grafički prikazi omogućuju jasnu prezentaciju rezultata analize čak i osobama bez dubokog tehničkog znanja. Na taj način vizualizacija služi kao most između tehničke forenzičke analize i interpretacije rezultata u širem kontekstu privatnosti i sigurnosti korisnika.

U ovom projektu vizualizacija se koristi kao završni korak analize, nadopunjujući numeričke pokazatelje i tablične podatke. Kombinacijom forenzičke analize i grafičke vizualizacije dobiva se cjelovit uvid u strukturu i intenzitet web trackinga.

## 7. Zaključak teorijskog dijela

Web tracking predstavlja sastavni i neizostavni dio modernog web ekosustava. Kroz različite tehničke mehanizme omogućuje prikupljanje podataka koji se koriste za poboljšanje funkcionalnosti web stranica, analizu korisničkog ponašanja i optimizaciju digitalnih usluga. Međutim, istovremeno predstavlja značajan izazov u kontekstu privatnosti i zaštite osobnih podataka korisnika.

Analiza teorijskih aspekata web trackinga pokazuje da se praćenje provodi na više razina, uključujući first-party i third-party zahtjeve, različite mehanizme praćenja te širok raspon kategorija trackera. Posebno je naglašena uloga third-party trackera koji omogućuju praćenje korisnika kroz više web stranica i stvaranje detaljnih profila ponašanja.

Razumijevanje mehanizama web praćenja i njihova analiza kroz mrežni promet omogućuju:
- veću transparentnost u načinu na koji se korisnički podaci prikupljaju i koriste  
- bolju informiranost korisnika o prisutnosti i ulozi trackera  
- objektivnu evaluaciju privatnosnih rizika povezanih s korištenjem web stranica  

Forenzički pristup analizi web prometa pruža metodološki okvir za identifikaciju i klasifikaciju trackera, kao i za kvantifikaciju razine praćenja kojoj su korisnici izloženi. Takav pristup omogućuje prelazak s apstraktnih rasprava o privatnosti na mjerljive i empirijski utemeljene rezultate.

Teorijski dio ovog rada postavlja temelj za praktični dio projekta u kojem se navedeni koncepti primjenjuju na stvarnim podacima. Kroz prikupljanje mrežnog prometa, obradu podataka i vizualizaciju odnosa između web stranica i trackera, teorijski okvir se nadopunjuje konkretnom analizom web trackinga u realnom okruženju.

Na taj način teorijski i praktični dio projekta čine cjelinu koja omogućuje dublje razumijevanje web trackinga, njegovih tehničkih implikacija i utjecaja na privatnost korisnika.


