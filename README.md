 # DEMO Evidencije Sati Volontiranja (Streamlit Aplikacija)

 Ova aplikacija omogućuje jednostavno praćenje i analizu volonterskih sati unutar Socijalne samoposluge "Kruh Sv. Antuna, Varaždin"
      Izrađena je pomoću Streamlit okvira, što je čini interaktivnom i jednostavnom za korištenje, bez potrebe za kompleksnim
      bazama podataka. Podaci se spremaju u CSV formatu, što osigurava lakoću pristupa i dijeljenja.

 ## Ključne Značajke

 *   **Unos Sati Volontiranja:** Brzo i jednostavno bilježenje imena, prezimena, datuma i broja volonterskih sati.
 *   **Pregled Podataka:** Tablični prikaz svih zabilježenih volonterskih sati, sortirano po datumu i imenu.
 *   **Izvoz Podataka:** Mogućnost preuzimanja svih ili filtriranih podataka u Excel formatu (.xlsx) za daljnju obradu.
 *   **Statistički Prikazi:**
     *   Ukupan broj sati volontiranja po volonteru.
     *   Ukupan broj sati volontiranja po volonteru na mjesečnoj razini.
     *   Vizualizacije podataka putem interaktivnih Plotly dijagrama (ukupni sati po osobi, trend sati po mjesecu).

 ## Kako Pokrenuti Aplikaciju

 Slijedite ove korake za postavljanje i pokretanje aplikacije na vašem lokalnom sustavu.

 ### Predduvjeti

 Prije pokretanja, provjerite imate li instaliran Python (verzija 3.8 ili novija).

 ### Instalacija
  **Klonirajte repozitorij:**
      ```
      git clone https://github.com/LKatava/Socka_evidencija.git
      cd Socka_evidencija
      ```
  **Instalirajte potrebne pakete:**
     `pip install -r requirements.txt`
 ### Pokretanje Aplikacije

 Nakon instalacije, aplikaciju možete pokrenuti pomoću Streamlit komande:
`streamlit run streamlit_app.py`
 Aplikacija će se automatski otvoriti u vašem web pregledniku.

Ili pokrenite aplikaciju sa streamlit platforme na link: https://sockasati.streamlit.app/
 

 ## Struktura Projekta

 *   `streamlit_app.py`: Glavna datoteka Streamlit aplikacije koja sadrži svu logiku i UI.
 *   `requirements.txt`: Popis svih Python biblioteka potrebnih za rad aplikacije.
 *   `data/sati_volontiranja.csv`: Datoteka u kojoj se spremaju svi podaci o volonterskim satima. Ako datoteka ne postoji, b
      će automatski kreirana.
 *   `images/logo_png.png`: Logo aplikacije.

 ## Korištene Tehnologije

 *   **Python**
 *   **Streamlit**: Za izgradnju interaktivnog web sučelja.
 *   **Pandas**: Za manipulaciju i analizu podataka.
 *   **XlsxWriter**: Za izvoz podataka u Excel format.
 *   **Plotly Express**: Za generiranje interaktivnih dijagrama.

 ## Licenca

 Ovaj projekt je licenciran pod [GNU GLPv3](LICENSE). Pogledajte datoteku `LICENSE` za više 
