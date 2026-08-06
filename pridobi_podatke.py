
import requests
import time
import os

leto=2025
headers={"User-Agent":"Mozilla/5.0"}


def koda_za_htmlje(leto):    #pridobljeni podatki 31.7.2026
    teme_nagrada=[
    "physics",
    "chemistry",
    "medicine",
    "literature",
    "peace",
    "economic-sciences"
    ]

    os.makedirs("htmlji", exist_ok=True)

    for stevilo in range(1901, leto + 1):
        for tema in teme_nagrada:
            url = 'https://www.nobelprize.org/prizes/'+ tema +'/'+ str(stevilo) +'/summary/' #koda za pobiranje
                
    
            try:
                ime_dat = f'{tema},{stevilo}.html'
                odgovor = requests.get(url, headers=headers, timeout=10)
                odgovor.raise_for_status()

                vsebina = odgovor.text

                with open(os.path.join("htmlji", ime_dat), 'w', encoding='utf-8') as f:
                     f.write(vsebina)        
                print(f'Datoteka nobelova nagrada {ime_dat} ustvarjena')

           
            except requests.exceptions.RequestException:
                    pass
            time.sleep(2)

    


