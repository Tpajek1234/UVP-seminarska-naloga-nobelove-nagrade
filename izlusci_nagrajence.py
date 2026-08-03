
import os
import re


mapa_z_nagrajenci = 'nobelovi_nagrajenci'

def po_datot_z_nagrjajenci(mapa_z_nagrajenci):
    
    slovar = {}
    set=[]

    for html in os.listdir(mapa_z_nagrajenci):
        if html.endswith(".html"):
            pot = os.path.join(mapa_z_nagrajenci, html) 

            with open(pot, encoding='utf-8') as d:
                preberi_html = d.read()
                
                k=izlusci_o_nagrajencih(preberi_html)
                if k is not None:
                    set.append(k)
        print(set)


def popravi_ime(nagr): #popravi ime da ni t-jev
    nova_nagr = nagr.strip()
    return nova_nagr

def izlusci_o_nagrajencih(preberi_html):
    ime_dobitnika = re.search(
                        r'<div class="content">\s*<p>(.*?)<br>',
                        preberi_html,
                        re.DOTALL
                        )
    nagrada = re.search(
        r'<div class="content">\s*<p>.*?<br>\s*(.*?)</p>',
        preberi_html,
        re.DOTALL
        )
    nagrada_je = nagrada.group(1)
    popravljeno = popravi_ime(ime_dobitnika.group(1))
    rojstvo = re.search(r'<p class="born-date">Born:(.*?)\s*</p>',
                        preberi_html,
                        re.DOTALL)
    smrt = re.search(r'<p class="dead-date">Died:(.*?)</p>',
                     preberi_html,
                     re.DOTALL)

    if smrt:
        return(popravljeno, popravi_ime(nagrada_je), popravi_ime(rojstvo.group(1)), popravi_ime(smrt.group(1)))
    elif rojstvo:
        return(popravljeno, popravi_ime(nagrada_je), popravi_ime(rojstvo.group(1)))
    elif not smrt and not rojstvo:
        return(popravljeno, popravi_ime(nagrada_je))
    #else:
    #    return('neki')


po_datot_z_nagrjajenci(mapa_z_nagrajenci)