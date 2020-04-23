# Monitorizarea prețurilor unui produs

## Instalarea modulelor necesare rulării corespunzătoare

Utilizăm [pip](https://pip.pypa.io/en/stable/) pentru a instala următoarele module:

```bash
pip install bs4
pip install threaded
pip install matplotlib
pip install times
pip install DateTime
pip install pycopy-urllib.request
pip install re2
```

## Prezentare pe scurt

Gandindu-ne la conceptul de "price monitoring", am realizat acest proiect prin care am dorit să eficientizăm transmiterea către utilizator a unor date esențiale când vine vorba despre un produs de pe un site anume.

## Precizări despre implementare și funcționare


Odată ce am pus bazele unor idei, am importat mai multe librarii care ne-au permis să avansăm în realizarea proiectului și care ne-au oferit un mediu propice. 
Pentru început, librăria "BeautifulSoup" ne-a ajutat să accesăm datele site-urilor și ne-a permis extragerea acestora.

[Vezi aici](https://ibb.co/z4jXHPn)

Pentru a accesa site-urile dorite, ne-am folosit de libraria "urllib.request".
"Datetime" si "time" ne-au permis accesarea datei curente, respectiv folosirea comenzii time.sleep(n), in care se face o pauza de n secunde, pe când libraria "re" a fost necesară pentru formatarea unor șiruri. 
Conceptul de multi-threading l-am putut satisface importând libraria "threading", de aici și folosirea de thread-uri de la sfârșitul programului.
Librăria "matplotlib.pyplot" ne-a ajutat să culminăm programul prin "plotarea" produselor în funcție de prețuri și de data și ora accesării programului.

[Vezi aici](https://ibb.co/c8sjptK)

Am declarat trei string-uri care conțin site-urile ”mamă”, cu ajutorul cărora se va face identificarea site-urilor pe care se răgesc produsele. Am definit o funcție "makeSoup" cu ajutorul căreia accesăm site-ul și căutam datele necesare programului nostru.

**myProgram()**
va deschide fișierul în care se vor da link-urile produselor.

[Vezi aici](https://ibb.co/5FNswdD)

Va identifica pentru fiecare site-ul ”mamă” din care face parte și va aplica metodele pentru fiecare (în funcție de categoria din care face parte) pentru extragerea titlului, a prețului si va inregistra data la care sunt extrase. 

[Vezi aici](https://ibb.co/bb94L0r)

Va crea un fișier cu numele link-ului produsului și va salva acolo datele necesare în următoarea partea a programului.

[Vezi aici](https://ibb.co/5vLQL7D)

[Vezi aici](https://ibb.co/Hgtd5Zb)


**myClient()**
va primi ca parametru unul sau mai multe link-uri de la tastatură.


Va citi datele produsului din fișier și va face grafic cu acestea. 

[Vezi aici](https://ibb.co/1dFQGn3)

Graficul se va salva automat in format ".png"

La sfârșit am definit două variabile numite **firstThread** și **secondThread** în care am apelat funcțiile prestabilite pentru thread.

# Contribuitori:
Dohatcu Andrei-Gabriel

Chivu Denis-Andrei

