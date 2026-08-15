# Seminarska naloga na temo Nobelove nagrade

Za **pridobitev podatkov** je potrebno 
zagnati le datoteko 
```main.py``` in imeti naložene knjižnice ```requests``` , ```os``` , ```time``` , ```re``` in ```csv```. 

Ko poženete datoteko ```main.py```, se bo najprej pognala datoteka ```pridobi_podatke.py```, iz katere se bo posamezen html povezav shranil v mapo ```htmlji```. Nato se bo pognala datoteka ```izlusci.py```, ki bo iz mape ```htmlji``` izluščila povezave do posameznih nagrajencev in njihove htmlje shranila v mapo ```nobelovi_nagrajenci```. Potem se bo še pognala datoteka ```izlusci_nagrajence.py```, v kateri se bodo iz pridobljenih htmljev posameznih nagrajencev izluščili podatki o njih in ti se bodo shranili v datoteko ```nobelovi_nagrajenci.csv```.

**Predstavitev podatkov** in **analiza** je narejena v datoteki ```nagrajenci_analiza.ipynb```. V njej sem analizirala področja in leta nagrade, starost nagrajencev ob prejemu nagrade, po mesecih, državah in letih rojstva nagrajencev. 

Podatki so pobrani so od prve podelitve nagrad, ki je bila leta 1901 in do vključno leta 2025. Pri izluščitvi podatkov o državah rojstva in smrti sem upoštevala ime države, ki je tam danes.
