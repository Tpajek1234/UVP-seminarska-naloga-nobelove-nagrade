
import os
import re


mapa_z_nagrajenci = 'nobelovi_nagrajenci'

def po_datot_z_nagrjajenci(mapa_z_nagrajenci):
    
    
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
    
    rojstvo = re.search(r'<p class="born-date">Born:(.*?)\s*</p>',
                        preberi_html,
                        re.DOTALL)
    
    smrt = re.search(r'<p class="dead-date">Died:(.*?)</p>',
                     preberi_html,
                     re.DOTALL)
    print(vse_v_slovar(ime_dobitnika, nagrada, rojstvo, smrt))
    return vse_v_slovar(ime_dobitnika, nagrada, rojstvo, smrt)

def vse_v_slovar(ime_dobitnika, nagrada, rojstvo, smrt):
    slov={}
    ime1 = 'ime'
    nagrada1 = 'nagrada'
    leto_nagrade='leto nagrade'
    rojstvo1 = 'rojstvo'
    smrt1 = 'smrt'

    popravljeno = ime_apostrof(popravi_ime(ime_dobitnika.group(1)))
    nagrada2 = odstrani_nobel_prize(popravi_ime(nagrada.group(1)))
    leto = loci_leto(nagrada2)
    samo_nagrada = loci(nagrada2)
    
    if smrt:
        slov[ime1] = popravljeno
        slov[rojstvo1] = popravi_ime(rojstvo.group(1))
        slov[smrt1] = popravi_ime(smrt.group(1))
        slov[nagrada1] = samo_nagrada
        slov[leto_nagrade] = leto
        return slov
    
    elif rojstvo:
        slov[ime1] = popravljeno
        slov[rojstvo1] = popravi_ime(rojstvo.group(1))
        slov[smrt1] = '/'
        slov[nagrada1] = samo_nagrada
        slov[leto_nagrade] = leto
        return slov
    
    elif not smrt and not rojstvo:
        slov[ime1]=popravljeno
        slov[rojstvo1] = '/'
        slov[smrt1] = '/'
        slov[nagrada1]=samo_nagrada
        slov[leto_nagrade]=leto
        return slov


  
def ime_apostrof(ime):
    vzorec = ' &#039;'
    if vzorec in ime:
        ime1=ime.replace(vzorec, '\'')
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

def loci_leto(nagrad):
    loci = nagrad.split()
    
    return int(loci[-1])
       
            
def loci(nagrad):
    loci = nagrad.split()
    
    nagrada=''
    for beseda in range(0,len(loci)-2):
        nagrada+=loci[beseda]
        nagrada+=' '
    nagrada+=loci[len(loci)-2]
    
    return nagrada


po_datot_z_nagrjajenci(mapa_z_nagrajenci)