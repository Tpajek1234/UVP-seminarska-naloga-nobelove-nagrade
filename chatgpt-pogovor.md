ali je ta koda pravilna da dobiš ven htmlje če je vse prav leto=2025 headers={"User-Agent":"Mozilla/5.0"} teme_nagrada=[ "physics", "chemistry", "medicine", "literature", "peace", "economic-sciences" ] def koda_za_htmlje(leto): for stevilo in range(1901, leto + 1): for tema in teme_nagrada: url='https://www.nobelprize.org/prizes/'+ tema +'/'+ str(stevilo) +'/summary/' try: ime_dat=f'{tema},{stevilo}.html' odgovor = requests.get(url, headers=headers, timeout=10) odgovor.raise_for_status() vsebina = odgovor.text with open(ime_dat, 'w', encoding='utf_8') as f: f.write(vsebina) print(f'Datoteka nobelova nagrada {url[32:]} ustvarjena') except requests.exceptions.RequestException: pass time.sleep(2) #koda_za_htmlje(leto)


Logika je pravilna: greš čez vsa leta, čez vsa področja, poskusiš prenesti stran, če ne obstaja, jo preskočiš, nato počakaš 2 sekundi.
Imam pa nekaj manjših pripomb.
________________________________________
✅ 1. Zanke so pravilne
for stevilo in range(1901, leto + 1):
    for tema in teme_nagrada:
To je pravilno.
________________________________________
✅ 2. URL je pravilno sestavljen
url = 'https://www.nobelprize.org/prizes/' + tema + '/' + str(stevilo) + '/summary/'
Lahko pa uporabiš tudi f-string, ki je bolj pregleden:
url = f"https://www.nobelprize.org/prizes/{tema}/{stevilo}/summary/"
________________________________________
✅ 3. try in except
To je v redu:
try:
    ...
except requests.exceptions.RequestException:
    pass
To pomeni: če strani ni ali pride do napake, nadaljuj z naslednjo.
________________________________________
✅ 4. time.sleep(2)
Pravilno si ga dal izven except.
Torej bo program počakal tudi, če stran ne obstaja.
________________________________________
⚠️ 5. encoding
Raje napiši
encoding="utf-8"
namesto
encoding="utf_8"
Oboje običajno deluje, vendar je utf-8 standardni zapis.
________________________________________
⚠️ 6. Izpis
To:
print(f'Datoteka nobelova nagrada {url[32:]} ustvarjena')
deluje, ampak je malo "krhko". Če se URL kdaj spremeni, 32 ne bo več pravi indeks.
Jaz bi raje napisal:
print(f"{ime_dat} ustvarjena")
ali
print(f"Prenesena: {url}")
________________________________________
⚠️ 7. Ena stvar, ki bi jo dodal
Pred zapisom lahko preveriš, ali datoteka že obstaja, da je ne prenašaš znova.
Na primer:
import os

if os.path.exists(ime_dat):
    continue
To ni nujno, je pa uporabno, če program prekineš in ga kasneje ponovno zaženeš.
________________________________________
Moja ocena
✅ Logika: 10/10
✅ Zanke: 10/10
✅ try/except: 10/10
Le nekaj manjših izboljšav (f-string za URL, utf-8, lepši print).
To je že koda, ki bi jo brez težav uporabil kot prvi korak projektne naloge.
Edino še preveri, da so URL-ji res oblike:
https://www.nobelprize.org/prizes/physics/2025/summary/
Če je struktura URL-jev na strani nekoliko drugačna, boš moral prilagoditi le vrstico, kjer sestaviš url; preostala logika je pravilna.


ali je koda ki sem jo spisal pravilna da bo pobrala htmlje iz teh notranjih povezav in bo shranila v mapo nobelovi_nagrajenci (sej pač ustvari samo eno mapo in se bodo shranili notr vsi htmlji da jih ne bo povozilo) in ali je vse pravilno spisano, da se ne bi kaj ko pobiram zalomilo def izlusci_vse_povezave_nagrajencev(mapa_s_htmlji): slovar_prii={} for html in os.listdir(mapa_s_htmlji): if html.endswith(".html"): pot = os.path.join(mapa_s_htmlji, html) with open(pot, encoding='utf-8') as d: preberi_html = d.read() povezave = re.findall( r'<h3 itemprop="name">\s*<a\s*href="(.*?)" title="Title text" itemprop="url" >', preberi_html, re.DOTALL ) priimki_dobitnikov = re.findall( r'<h3 itemprop="name">\s*<a\s*href="https://www.nobelprize.org/prizes/.*?/.*?/(.*?)/facts/".*?>\s*.*?</a>', preberi_html, re.DOTALL ) for povezava in povezave: #shrani v slovar povezave in priimke for priimek in priimki_dobitnikov: if priimek in povezava: slovar_prii[priimek] = povezava return slovar_prii def pobere_o_nagrajencih(slovar_prii): for priimek, povezava in slovar_prii.items(): print(priimek,povezava) try: ime_dat = f'{priimek}.html' odgovor = requests.get(povezava, headers=headers, timeout=10) odgovor.raise_for_status() vsebina = odgovor.text with open(f'/nobelovi_nagrajenci/{ime_dat}', 'w', encoding='utf-8') as f: f.write(vsebina) print(f'Datoteka nobelova nagrada {ime_dat} ustvarjena') except requests.exceptions.RequestException: pass time.sleep(2) #pobere_o_nagrajencih(izlusci_vse_povezave_nagrajencev(mapa_s_htmlji))
Ideja je zelo dobra, ampak v kodi vidim nekaj stvari, ki bi jih popravil, da bo zanesljivo delovala.
1. Največji problem – pot do datoteke
Imaš:
with open(f'/nobelovi_nagrajenci/{ime_dat}', 'w', encoding='utf-8') as f:
To ni pravilno, če želiš mapo nobelovi_nagrajenci znotraj svojega projekta.
Začetni / pomeni absolutno pot (na Linuxu npr. /nobelovi_nagrajenci/...), ne mapo v trenutnem imeniku.
Bolje je:
with open(os.path.join("nobelovi_nagrajenci", ime_dat), "w", encoding="utf-8") as f:
ali vsaj
with open(f"nobelovi_nagrajenci/{ime_dat}", ...)
________________________________________
2. Ali se mapa ustvari?
Ne.
Če mapa nobelovi_nagrajenci še ne obstaja, bo program vrgel napako.
Pred zanko naredi:
os.makedirs("nobelovi_nagrajenci", exist_ok=True)
Če mapa že obstaja, se ne zgodi nič.
________________________________________
3. Iskanje povezav in priimkov
Tole:
for povezava in povezave:
    for priimek in priimki_dobitnikov:
        if priimek in povezava:
            slovar_prii[priimek] = povezava
bo verjetno delovalo, ampak ni najbolj elegantno.
Če sta seznama v istem vrstnem redu (kar pogosto sta), je boljše:
for povezava, priimek in zip(povezave, priimki_dobitnikov):
    slovar_prii[priimek] = povezava
Ni dvojne zanke in je hitrejše.
________________________________________
4. Prepisovanje datotek
Če imata dva nagrajenca isti priimek, npr.
Smith
bo drugi prepisal prvega.
To se lahko zgodi.
Bolj varno je ime sestaviti iz več podatkov, npr.
physics_2025_devoret.html
ali pa dodati ime in priimek.
________________________________________
5. except
To:
except requests.exceptions.RequestException:
    pass
je v redu.
Jaz bi med razvojem raje napisal:
except requests.exceptions.RequestException as e:
    print(e)
Ker boš takoj videl, če imaš napačen URL.
________________________________________
6. time.sleep(2)
Pravilno si ga dal izven except.
👍
________________________________________
7. Regex
To me malo skrbi:
title="Title text"
Ali je v HTML-ju res vedno dobesedno
title="Title text"
?
Če ni, regex ne bo našel ničesar.
Velikokrat je bolje uporabiti
title=".*?"
ali pa sploh ne iskati atributa title, če ga ne potrebuješ.
________________________________________
Moja ocena
•	Organizacija funkcij: 9/10 
•	Logika prenosa: 10/10 
•	Shranjevanje HTML: 8/10 (zaradi poti in možnosti prepisovanja) 
•	Regexov ne morem dokončno oceniti brez dejanskega HTML-ja. 
Preden zaženeš
Jaz bi preveril naslednje:
•	 os.makedirs("nobelovi_nagrajenci", exist_ok=True) je dodan. 
•	 Pot do datoteke ne začne z /. 
•	 Regex res ujame povezave na dejanskem HTML-ju. 
•	 Priimek je res enoličen za ime datoteke ali uporabiš bolj enolično ime. 
Če te štiri stvari uredijo, je zasnova programa dobra in primerna za projekt.

