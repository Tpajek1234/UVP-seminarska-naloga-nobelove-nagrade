import requests
import time
import re
import os




headers={"User-Agent":"Mozilla/5.0"}


def izlusci_vse_povezave_nagrajencev():
    slovar_prii = {}
    for html in os.listdir('htmlji'):
        if html.endswith(".html"):
            pot = os.path.join('htmlji', html) 

            with open(pot, encoding='utf-8') as d:
                preberi_html = d.read()
               
                povezave = re.findall(
                            r'<h3 itemprop="name">\s*<a\s*href="(.*?)" title="Title text" itemprop="url" >',
                            preberi_html,
                            re.DOTALL
                            )
                priimki_dobitnikov = re.findall(
                                    r'<h3 itemprop="name">\s*<a\s*href="https://www.nobelprize.org/prizes/(.*?)/facts/".*?>\s*.*?</a>',
                                    preberi_html,
                                    re.DOTALL
                                    )            
                for povezava in povezave: #shrani v slovar povezave in priimke
                    for priimek in priimki_dobitnikov:
                        if priimek in povezava:
                            slovar_prii[priimki_brez_posevnice(priimek)] = povezava
    print(slovar_prii)  
                  
    return slovar_prii

def priimki_brez_posevnice(niz):
    novo=''

    popravljen_priimek=niz.split("/")
        
    for popravljen in range(0,len(popravljen_priimek)):
        novo += popravljen_priimek[popravljen]
        novo+= '-' 
    novo+=popravljen_priimek[-1]

    return novo



def pobere_o_nagrajencih(slovar_prii):  #podatki pobrani 2.8.2026

    os.makedirs("nobelovi_nagrajenci", exist_ok=True)

    for priimek, povezava in slovar_prii.items():
        

        try:
            ime_dat = f'{priimek}.html'
            odgovor = requests.get(povezava, headers=headers, timeout=10)
            odgovor.raise_for_status()
            vsebina = odgovor.text
            with open(os.path.join("nobelovi_nagrajenci", ime_dat),"w",encoding="utf-8") as f:
                 f.write(vsebina)        
            print(f'Datoteka nobelova nagrada {ime_dat} ustvarjena')
    
               
        except requests.exceptions.RequestException as e:
            print(f"Napaka pri {povezava}: {e}")
        
        time.sleep(2)
                    




    




    






