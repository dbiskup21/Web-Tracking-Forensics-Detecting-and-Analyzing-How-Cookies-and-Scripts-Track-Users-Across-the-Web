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
