# Reference i izvori

Ovaj dokument navodi ključne akademske izvore, alate i online dokumentaciju korištene pri izradi projekta **Web Tracking Forensics: Detecting and Analyzing How Cookies and Scripts Track Users Across the Web**.

---

## 1. Akademska i stručna literatura

1. Englehardt, S., & Narayanan, A. (2016).  
   **Online Tracking: A 1-million-site Measurement and Analysis**.  
   Proceedings of the ACM Conference on Computer and Communications Security (CCS).  
   https://webtransparency.cs.princeton.edu/webcensus/  

   *Rad pruža empirijsku analizu web trackinga na velikom broju web stranica te predstavlja temelj za razumijevanje third-party trackinga.*

2. Mayer, J. R., & Mitchell, J. C. (2012).  
   **Third-Party Web Tracking: Policy and Technology**.  
   IEEE Symposium on Security and Privacy.  

   *Teorijska podloga za razlikovanje first-party i third-party trackera te raspravu o privatnosnim implikacijama.*

3. IETF. (2011).  
   **RFC 6265: HTTP State Management Mechanism**.  
   https://datatracker.ietf.org/doc/html/rfc6265  

   *Službena specifikacija HTTP kolačića kao osnovnog mehanizma web praćenja.*

---

## 2. Online stručni resursi i privatnost

- Electronic Frontier Foundation. (n.d.).  
  *Online tracking*.  
  https://www.eff.org/issues/online-behavioral-tracking

  *Pregled tehnika web praćenja i njihovog utjecaja na privatnost korisnika.*

- Mozilla Developer Network. (n.d.).  
  *Web privacy and tracking*.  
  https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Firefox_tracking_protection

- Mozilla Developer Network. (n.d.).  
  *Browser fingerprinting*.  
  https://developer.mozilla.org/en-US/docs/Glossary/Fingerprinting

  *Tehnički opisi modernih mehanizama web trackinga i fingerprintinga.*

- European Union Agency for Cybersecurity. (n.d.).  
  *Privacy and data protection*.  
  https://www.enisa.europa.eu/publications/privacy-and-data-protection-by-design

  *Sigurnosni i privatnosni aspekti online praćenja u europskom regulatornom kontekstu.*

---

## 3. Softverski alati i tehnologije

### 3.1 Glavni alati korišteni u projektu

- **mitmproxy** – interaktivni HTTPS proxy za snimanje i analizu mrežnog prometa  
  https://mitmproxy.org/  

- **Python 3** – obrada logova, klasifikacija trackera i analiza podataka  
  https://www.python.org/  

- **SQLite** – lagana relacijska baza podataka za pohranu mrežnih zahtjeva  
  https://www.sqlite.org/  

- **Gephi** – alat za vizualizaciju i analizu grafova  
  https://gephi.org/  

---
