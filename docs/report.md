# Izvještaj o sigurnosnoj analizi – Web Tracking Forensics

## 1. Uvod i ciljevi

Razvojem modernih web tehnologija web stranice sve češće koriste vanjske servise za
analizu korištenja, oglašavanje, personalizaciju sadržaja i tehničku telemetriju.
Takvi servisi često sudjeluju u prikupljanju podataka o korisnicima bez njihove
izravne svijesti, kroz mrežni promet koji se odvija u pozadini pregledavanja weba.

Cilj ovog projekta je provesti **forenzičku analizu web praćenja korisnika**
kroz detaljnu analizu HTTP i HTTPS mrežnog prometa generiranog tijekom uobičajenog
korištenja web stranica. Analiza se temelji na presretanju i obradi mrežnih zahtjeva,
identifikaciji uključenih domena te klasifikaciji mehanizama web trackinga.

Projekt je usmjeren na razumijevanje **kako, u kojoj mjeri i putem kojih servisa**
se provodi praćenje korisnika na internetu, s posebnim naglaskom na third-party
komunikaciju i njezine implikacije na privatnost.

### Ciljevi projekta

Ciljevi projekta obuhvaćaju:

- detekciju **third-party trackera** prisutnih tijekom posjeta web stranicama
- identifikaciju vanjskih domena koje sudjeluju u prikupljanju korisničkih podataka
- analizu mrežnih zahtjeva koji se odvijaju bez izravne interakcije korisnika
- klasifikaciju trackera prema njihovoj namjeni (analytics, advertising, social, telemetry)
- procjenu intenziteta praćenja za svaku analiziranu web stranicu
- vizualizaciju odnosa između web stranica i tracking domena

Navedeni ciljevi omogućuju usporedbu web stranica prema razini praćenja korisnika
te pružaju uvid u infrastrukturu web trackinga i njezin utjecaj na privatnost.


## 2. Metodologija rada

Metodologija rada temelji se na forenzičkoj analizi mrežnog prometa s ciljem
identifikacije i razumijevanja mehanizama web praćenja korisnika. Proces analize
podijeljen je u više faza koje obuhvaćaju snimanje prometa, obradu i sanitizaciju
podataka te njihovu pripremu za daljnju analizu.

---

### 2.1 Snimanje mrežnog prometa

Za snimanje mrežnog prometa korišten je intercepting proxy alat **mitmproxy**, koji
omogućuje presretanje HTTP i HTTPS zahtjeva u stvarnom vremenu. Sav mrežni promet
web preglednika preusmjeren je kroz lokalni proxy poslužitelj postavljen na adresu
`127.0.0.1` i port `8080`.

Tijekom uobičajenog pregledavanja web stranica presretani su svi mrežni zahtjevi
koji se automatski generiraju prilikom učitavanja sadržaja. Snimanje je obuhvatilo
kako first-party zahtjeve prema posjećenim web stranicama, tako i third-party
zahtjeve prema vanjskim domenama koje sudjeluju u analitici, oglašavanju, društvenim
integracijama i telemetriji.

Za svaki zahtjev bilježeni su ključni elementi relevantni za analizu web trackinga,
uključujući URL zahtjeva, odredišnu domenu, HTTP metodu, prisutne kolačiće te
zaglavlja poput User-Agenta. Snimanje je provedeno bez aktivne interakcije s
aplikacijskim kodom web stranica, čime je osigurano da prikupljeni podaci
predstavljaju realno ponašanje weba iz perspektive krajnjeg korisnika.

**Rezultat:**
- `traffic_log.json` – sirovi zapis mrežnog prometa koji sadrži sve presretnute
  HTTP i HTTPS zahtjeve tijekom analize

---

### 2.2 Obrada i sanitizacija podataka

Sirovi zapisi mrežnog prometa sadržavali su velik broj tehničkih i redundantnih
podataka koji nisu izravno relevantni za analizu web praćenja, kao i potencijalno
osjetljive informacije. Zbog toga je provedena faza obrade i sanitizacije podataka
kako bi se osigurala sigurnost, preglednost i konzistentnost daljnje analize.

U ovoj fazi uklonjena su nepotrebna HTTP zaglavlja i podaci koji ne doprinose
identifikaciji trackera. Zapisi su normalizirani kako bi svi zahtjevi imali
ujednačenu strukturu, čime je omogućena jednostavnija pohrana i obrada podataka.
Poseban naglasak stavljen je na izdvajanje ključnih atributa, kao što su posjećena
web stranica, odredišna domena zahtjeva, URL, HTTP metoda i kolačići.

Sanitizacijom podataka dodatno je smanjen rizik od pohrane osobnih ili osjetljivih
informacija, čime je analiza usklađena s osnovnim načelima zaštite privatnosti.
Dobiveni podaci predstavljaju anonimiziran i strukturiran skup zapisa spreman za
pohranu u bazu podataka i daljnju forenzičku analizu.

**Rezultat:**
- `traffic_log_sanitized.json` – obrađeni i sanitizirani zapis mrežnog prometa,
  pripremljen za pohranu i analizu

---

## 3. Pohrana podataka

Nakon obrade i sanitizacije mrežnog prometa, prikupljeni podaci pohranjeni su u
relacijsku bazu podataka radi lakše analize i organizacije. Za potrebe projekta
korištena je lagana SQLite baza podataka, koja omogućuje jednostavno upravljanje
podacima bez potrebe za dodatnim poslužiteljskim komponentama.

Podaci su pohranjeni u bazu podataka pod nazivom `tracking.db`, u tablicu
`requests`, gdje svaki zapis predstavlja jedan presretnuti mrežni zahtjev.
Struktura tablice osmišljena je tako da obuhvati sve ključne informacije potrebne
za forenzičku analizu web praćenja.

Tablica sadrži sljedeće atribute:

- **visited_site** – domena web stranice koju je korisnik izravno posjetio  
- **request_domain** – odredišna domena mrežnog zahtjeva  
- **url** – puni URL mrežnog zahtjeva  
- **method** – HTTP metoda korištena u zahtjevu  
- **cookies** – kolačići prisutni u zahtjevu  
- **user_agent** – identifikacija preglednika i operativnog sustava  
- **is_third_party** – oznaka koja razlikuje first-party i third-party zahtjeve  

Ovakva struktura baze omogućuje učinkovito filtriranje i analizu podataka, primjerice
razlikovanje first-party i third-party komunikacije, identifikaciju najčešćih
tracking domena te analizu zahtjeva prema kategorijama trackera. Centralizirana
pohrana podataka u bazi olakšava izvođenje statističkih upita, usporedbu web
stranica i pripremu podataka za vizualizaciju.

Pohrana u relacijsku bazu podataka također omogućuje ponovljivost analize i
jednostavno proširenje projekta dodavanjem novih atributa ili dodatnih faza obrade
podataka u budućnosti.

---

## 4. Detekcija i klasifikacija trackera

Jedan od ključnih koraka analize web praćenja jest identifikacija i razumijevanje
mrežnih zahtjeva koji nisu nužni za osnovno funkcioniranje web stranice, već služe
praćenju korisnika. U ovom poglavlju opisani su postupci detekcije third-party
zahtjeva i njihova klasifikacija prema namjeni.

---

### 4.1 Detekcija third-party zahtjeva

Mrežni zahtjev označava se kao **third-party zahtjev** ako se odredišna domena
zahtjeva razlikuje od domene web stranice koju je korisnik izravno posjetio. Ovakav
pristup omogućuje jasno razlikovanje između komunikacije koja je dio same web
aplikacije (first-party) i komunikacije prema vanjskim servisima.

Detekcija third-party zahtjeva provedena je usporedbom atributa `visited_site` i
`request_domain` za svaki zapis u bazi podataka. Ako navedene domene nisu iste,
zahtjev se označava kao third-party. Time je omogućena automatizirana identifikacija
vanjskih servisa koji sudjeluju u mrežnoj komunikaciji bez obzira na sadržaj
posjećene web stranice.

Ovakva metoda detekcije predstavlja temelj za daljnju analizu web trackinga, budući
da se većina mehanizama praćenja korisnika oslanja upravo na third-party infrastrukturu.

---

### 4.2 Klasifikacija trackera

Nakon identifikacije third-party zahtjeva provedena je njihova klasifikacija prema
namjeni i vrsti praćenja. Svaka third-party domena automatski je svrstana u jednu
od sljedećih kategorija:

- **Analytics** – servisi za prikupljanje statističkih podataka o korištenju web stranica  
- **Advertising** – oglašivačke mreže i servisi za ciljanje korisnika  
- **Social** – integracije društvenih mreža i društveni trackeri  
- **Telemetry** – tehničko praćenje rada aplikacija i sustava  
- **Other** – servisi koji ne pripadaju jasno definiranim kategorijama  

Klasifikacija se temelji na kombinaciji više pristupa. Prije svega korištena je baza
poznatih tracking domena, kao i pravila temeljena na nazivima domena i njihovim
poddomenskim strukturama. Dodatno su primijenjene heuristike nad URL-ovima i
obrascima mrežnih zahtjeva kako bi se obuhvatile i manje poznate ili specifične
tracking domene.

Dobivena kategorija svakog zahtjeva pohranjena je u bazu podataka, čime je omogućena
daljnja statistička analiza, usporedba web stranica te vizualizacija odnosa između
različitih vrsta trackera i posjećenih web stranica.

---

## 5. Procjena intenziteta praćenja

Kako bi se omogućila usporedba web stranica prema razini praćenja korisnika,
za svaku analiziranu web stranicu izračunat je jedinstveni **tracking intensity
score**. Ovaj pokazatelj osmišljen je kako bi kvantitativno izrazio opseg i složenost
web trackinga prisutnog tijekom posjeta pojedinoj stranici.

Tracking intensity score temelji se na kombinaciji više faktora, uključujući:

- ukupan broj mrežnih zahtjeva generiranih tijekom posjeta web stranici
- broj zahtjeva prema third-party domenama
- broj jedinstvenih third-party tracking domena
- zastupljenost pojedinih kategorija trackera (analytics, advertising, social, telemetry)
- indikatore ponašanja koji mogu upućivati na fingerprinting mehanizme

Navedeni faktori omogućuju uvažavanje ne samo količine mrežnih zahtjeva, već i njihove
raznolikosti te potencijalnog utjecaja na privatnost korisnika. Na primjer, web
stranica s manjim brojem zahtjeva, ali s velikim brojem različitih tracking domena,
može imati viši intenzitet praćenja od stranice s većim, ali homogenijim prometom.

Na temelju izračunatog tracking intensity scorea web stranice su rangirane prema
razini praćenja korisnika. Takvo rangiranje omogućuje identifikaciju web stranica s
izraženijim tracking ponašanjem te olakšava usporedbu različitih kategorija web
stranica u kontekstu privatnosti i sigurnosti.

Procjena intenziteta praćenja predstavlja važan korak u analizi jer omogućuje
pretvaranje složenih mrežnih podataka u jasan i interpretabilan pokazatelj koji se
može koristiti u daljnjoj analizi i vizualizaciji rezultata.

---

## 6. Vizualizacija podataka

Vizualizacija podataka predstavlja završni korak analize, čiji je cilj grafički
prikazati složene odnose između web stranica i third-party tracking domena.
Budući da mrežni promet uključuje velik broj međusobno povezanih zahtjeva,
grafovski pristup omogućuje intuitivno razumijevanje strukture web praćenja.

---

### 6.1 Graf mrežnog praćenja

Podaci prikupljeni i obrađeni u prethodnim fazama izvezeni su u grafovski format
prikladan za analizu mrežnih odnosa. U grafu su definirane dvije osnovne vrste
čvorova:

- **web stranice** koje korisnik izravno posjećuje  
- **tracking domene** koje sudjeluju u third-party komunikaciji  

Bridovi u grafu predstavljaju mrežne zahtjeve između web stranica i tracking
domena, čime se jasno modelira odnos između izvora zahtjeva i vanjskih servisa.

Vizualizacija je provedena u alatu **Gephi**, koji omogućuje primjenu grafičkih
algoritama za raspored čvorova i analizu njihove povezanosti. Korištenjem
ForceAtlas algoritma čvorovi s većim brojem veza prirodno se grupiraju, što
olakšava prepoznavanje ključnih elemenata mreže.

Grafički prikaz omogućio je uočavanje nekoliko važnih obrazaca, uključujući
postojanje **centraliziranih tracking servisa** koji su povezani s velikim brojem
različitih web stranica. Također su jasno vidljivi **dominantni third-party
provideri** koji imaju značajnu ulogu u web praćenju korisnika. Vizualizacija
je dodatno omogućila identifikaciju web stranica s izrazito visokim brojem
tracking veza, što upućuje na intenzivnije praćenje korisničke aktivnosti.

Na ovaj način grafovska vizualizacija služi kao vrijedan alat za interpretaciju
rezultata analize i pruža jasan, intuitivan prikaz složenih odnosa unutar web
tracking ekosustava.

---

## 7. Zaključak

Provedena sigurnosna i forenzička analiza mrežnog prometa pokazala je da je web
praćenje korisnika široko rasprostranjena praksa na suvremenim web stranicama.
Rezultati analize jasno ukazuju na činjenicu da većina popularnih web stranica
ostvaruje komunikaciju s više vanjskih, third-party servisa već prilikom osnovnog
učitavanja sadržaja.

Analiza je pokazala da relativno mali broj domena djeluje kao **centralni tracking
čvorovi**, prisutni na velikom broju nepovezanih web stranica. Takvi servisi
omogućuju korelaciju korisničke aktivnosti kroz različite domene i predstavljaju
ključnu komponentu web tracking infrastrukture. Vizualizacija mrežnih odnosa dodatno
je potvrdila postojanje centraliziranih tracking servisa s velikim brojem veza,
što upućuje na visok stupanj koncentracije web praćenja.

Korištenjem analize HTTP i HTTPS mrežnog prometa pokazalo se da je ovaj pristup
učinkovit alat za **forenzičku analizu privatnosti**, jer omogućuje uvid u
komunikaciju koja se odvija u pozadini, često bez izravne interakcije ili svijesti
korisnika. Identifikacija third-party zahtjeva, njihova klasifikacija te procjena
intenziteta praćenja pružaju mjerljiv i objektivan uvid u razinu web trackinga.

Zaključno, rezultati projekta potvrđuju da mrežni promet predstavlja vrijedan izvor
informacija za analizu web praćenja korisnika. Razvijeni sustav i primijenjena
metodologija omogućuju strukturiranu i ponovljivu analizu te mogu poslužiti kao
pouzdana osnova za daljnje sigurnosne i privatnosne analize u području web
tehnologija.

---
