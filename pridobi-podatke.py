
import requests
import time


leto=2025
headers={"User-Agent":"Mozilla/5.0"}
teme_nagrada=[
    "physics",
    "chemistry",
    "medicine",
    "literature",
    "peace",
    "economic-sciences"
    ]


def koda_za_htmlje(leto):    
    for stevilo in range(1901, leto + 1):
        for tema in teme_nagrada:
            url='https://www.nobelprize.org/prizes/'+ tema +'/'+ str(stevilo) +'/summary/' #koda za pobiranje
                
    
            try:
                ime_dat=f'{tema},{stevilo}.html'
                odgovor = requests.get(url, headers=headers, timeout=10)
                odgovor.raise_for_status()

                vsebina = odgovor.text

                with open(ime_dat, 'w', encoding='utf-8') as f:
                     f.write(vsebina)        
                print(f'Datoteka nobelova nagrada {ime_dat} ustvarjena')

           
            except requests.exceptions.RequestException:
                    pass
            time.sleep(2)

    
koda_za_htmlje(leto)





#def dobi_v_datoteko_html(leto):
#    for tem in teme_nagrada:
#        for i in range(1901,leto):
#            shrani_kot_html(f'{tem},{i}.html',koda_za_htmlje(leto))
        
#dobi_v_datoteko_html(leto)




