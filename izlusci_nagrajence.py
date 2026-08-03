
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
    slov={}
    ime1 = 'ime'
    nagrada1 = 'nagrada'
    rojstvo1 = 'rojstvo'
    smrt1 = 'smrt'
            
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
    popravljeno = ime_apostrof(popravi_ime(ime_dobitnika.group(1)))
    rojstvo = re.search(r'<p class="born-date">Born:(.*?)\s*</p>',
                        preberi_html,
                        re.DOTALL)
    smrt = re.search(r'<p class="dead-date">Died:(.*?)</p>',
                     preberi_html,
                     re.DOTALL)
    nagrada2=odstrani_nobel_prize(popravi_ime(nagrada_je))

    if smrt:
        slov[ime1]=popravljeno
        slov[nagrada1]=nagrada2
        slov[rojstvo1]=popravi_ime(rojstvo.group(1))
        slov[smrt1]=popravi_ime(smrt.group(1))
        return slov
    elif rojstvo:
        slov[ime1]=popravljeno
        slov[nagrada1]=nagrada2
        slov[rojstvo1]=popravi_ime(rojstvo.group(1))
        return slov
    elif not smrt and not rojstvo:
        slov[ime1]=popravljeno
        slov[nagrada1]=nagrada2
        return slov
    #else:
    #    return('neki')
def ime_apostrof(ime):
    a=' &#039;'
    if a in ime:
        ime1=ime.replace(a, "'")
        return ime1
    else:
        return ime

def odstrani_nobel_prize(nagrada):
    odstranit = 'Nobel Prize in '
    ekonomska_nagrada = 'Sveriges Riksbank Prize in '
    mir = 'Nobel Peace Prize'
    if odstranit in nagrada:
        nova_nagrada = nagrada.replace(odstranit, '')
        return nova_nagrada
    elif ekonomska_nagrada in nagrada:
        nova_nagrada = nagrada.replace(ekonomska_nagrada, '')
        return nova_nagrada
    elif mir in nagrada:
        nova_nagrada = nagrada.replace(mir,'')
        nagrada1 = 'Peace' + nova_nagrada
        return nagrada1


po_datot_z_nagrjajenci(mapa_z_nagrajenci)