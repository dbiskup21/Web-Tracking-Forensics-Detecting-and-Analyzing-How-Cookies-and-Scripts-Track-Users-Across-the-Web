# Reference i izvori

Ovaj dokument navodi ključne izvore, alate i dokumentaciju korištene pri izradi projekta **Web Tracking Forensics: Detecting and Analyzing How Cookies and Scripts Track Users Across the Web**.

---

## 1. Akademska i stručna literatura

1. Englehardt, S., & Narayanan, A. (2016).  
   **Online Tracking: A 1-million-site Measurement and Analysis**.  
   Proceedings of the ACM Conference on Computer and Communications Security (CCS).  
   https://webtransparency.cs.princeton.edu/webcensus/ 

   *Rad pruža temeljno razumijevanje third-party trackinga, kolačića i mrežnih zahtjeva.*

2. Mayer, J. R., & Mitchell, J. C. (2012).  
   **Third-Party Web Tracking: Policy and Technology**.  
   IEEE Symposium on Security and Privacy.  

   *Teorijska podloga za razlikovanje first-party i third-party trackera.*

---

## 2. Softverski alati i tehnologije

### 2.1 Glavni alati

- **mitmproxy** – interaktivni HTTPS proxy za snimanje i analizu mrežnog prometa  
  https://mitmproxy.org/

- **Python 3** – obrada logova, klasifikacija trackera i analiza podataka  
  https://www.python.org/

- **SQLite** – lagana relacijska baza podataka za pohranu mrežnih zahtjeva  
  https://www.sqlite.org/

- **Gephi** – alat za vizualizaciju i analizu grafova  
  https://gephi.org/

---

## 3. Online resursi i dokumentacija

### 3.1 Službena dokumentacija

- mitmproxy dokumentacija  
  https://docs.mitmproxy.org/

- Python službena dokumentacija  
  https://docs.python.org/3/

- SQLite SQL dokumentacija  
  https://www.sqlite.org/docs.html

- Gephi dokumentacija  
  https://gephi.org/users/

---

## 4. Liste i baze poznatih trackera

- **EasyList / EasyPrivacy** – popisi poznatih advertising i tracking domena  
  https://easylist.to/

- **Disconnect Tracking Protection List**  
  https://disconnect.me/trackerprotection

*Liste korištene kao referenca za klasifikaciju tracking domena.*

---

