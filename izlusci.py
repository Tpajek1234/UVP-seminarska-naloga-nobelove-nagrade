

import re
import os




headers={"User-Agent":"Mozilla/5.0"}

mapa_s_htmlji = 'htmlji'

def po_datot(mapa_s_htmlji):
    
    slovar = {}


    for html in os.listdir(mapa_s_htmlji):
        if html.endswith(".html"):
            pot = os.path.join(mapa_s_htmlji, html) 

            with open(pot, encoding='utf-8') as d:
                preberi_html = d.read()
            #print(html)
                vrsta_nagrade = re.findall(
                r'\s*<header class="heading">\s*<h1>\s*(.*?)</h1>\s*</header>',
                preberi_html,
                re.DOTALL
                )
                dobitnik_nagrade = re.findall(
                    r'<h3 itemprop="name">\s*<a\s*href="https://www.nobelprize.org/prizes/.*?/.*?/.*?/facts/".*?>\s*(.*?)</a>',
                    preberi_html,
                    re.DOTALL
                    )
                priimki_dobitnikov = re.findall(
                    r'<h3 itemprop="name">\s*<a\s*href="https://www.nobelprize.org/prizes/.*?/.*?/(.*?)/facts/".*?>\s*.*?</a>',
                    preberi_html,
                    re.DOTALL
                    )

                
                #print(dobitnik_nagrade,vrsta_nagrade)
                for nagra in vrsta_nagrade:
                    #print(nagra)
                    nova=popravi_nagradi(nagra)
                    slovar[nova]=popravi_imena_brez_t(dobitnik_nagrade)
                #print(slovar)
    #print(slovar) #da slovar v katerem je seznam nagrajencev po vrstah nagrad

   

def popravi_imena_brez_t(seznam): #funkcija ki bo popravila da bo brez t ja
    sez=[] #dam v seznam da bo tam brez t jev
    for t in seznam:

        popravljeno_ime = t.strip()
        sez.append(popravljeno_ime)
    return sez

def popravi_nagradi(nagr): #popravi ime da ni t-jev
    nova_nagr = nagr.strip()
    return nova_nagr
    #print(popravljeno_ime)    
    #return popravljeno_ime      

#po_datot(mapa_s_htmlji)


def izlusci_vse_povezave_nagrajencev(mapa_s_htmlji):
    slovar_prii={}
    for html in os.listdir(mapa_s_htmlji):
        if html.endswith(".html"):
            pot = os.path.join(mapa_s_htmlji, html) 

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
                            slovar_prii[priimek] = povezava
    print(slovar_prii)                
    return slovar_prii





    
#izlusci_vse_povezave_nagrajencev(mapa_s_htmlji)



    













