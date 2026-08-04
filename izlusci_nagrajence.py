
import os
import re


mapa_z_nagrajenci = 'nobelovi_nagrajenci'

def po_datot_z_nagrjajenci(mapa_z_nagrajenci):
    sez=[]

    for html in os.listdir(mapa_z_nagrajenci):
        if html.endswith(".html"):
            pot = os.path.join(mapa_z_nagrajenci, html) 

            with open(pot, encoding='utf-8') as d:
                preberi_html = d.read()
                
                k=izlusci_o_nagrajencih(preberi_html)
                if k is not None:
                    sez.append(k)
        print(sez)


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
    popravljeno = ime_apostrof(popravi_ime(ime_dobitnika.group(1)))
    print(popravljeno)
    nagrada2 = odstrani_nobel_prize(popravi_ime(nagrada.group(1)))
    print(nagrada2)
    leto = loci_leto(nagrada2)
    samo_nagrada = loci(nagrada2)    
    if smrt:
        razdeliti_rojstvo = loci_rojstva_smrt(popravi_ime(rojstvo.group(1)))
        rojstvo_dan_leto = razdeliti_rojstvo[0]
        rojstvo_dan = loci(rojstvo_dan_leto)
        rojstvo_leto = loci_leto(rojstvo_dan_leto)
        rojstvo_drzava = razdeliti_rojstvo[-1]
                
        razdeliti_smrt = loci_rojstva_smrt(popravi_ime(smrt.group(1)))
        smrt_dan_leto = razdeliti_smrt[0]
        smrt_dan = loci(smrt_dan_leto)
        smrt_leto = loci_leto(smrt_dan_leto)
        smrt_drzava = razdeliti_smrt[-1]

        ime1 = popravljeno
        datum1 = datum_rojstva_popravi(rojstvo_dan)
        leto_rojstva = rojstvo_leto
        drzava_rojstva = drzava_rojstva_popravi(popravi_drzava(rojstvo_drzava))
        dan_smrti = smrt_dan
        leto_smrti = smrt_leto
        kraj_smrti = drzava_rojstva_popravi(popravi_drzava(smrt_drzava))
        podrocje = samo_nagrada
        leto_nagrade1 = leto
        return v_slovar(ime1, datum1, leto_rojstva, drzava_rojstva, dan_smrti, leto_smrti, kraj_smrti, podrocje, leto_nagrade1)
        
    elif rojstvo:
        razdeliti_rojstvo = loci_rojstva_smrt(popravi_ime(rojstvo.group(1)))
        rojstvo_dan_leto = razdeliti_rojstvo[0]
        rojstvo_dan = loci(rojstvo_dan_leto)
        rojstvo_leto = loci_leto(rojstvo_dan_leto)
        rojstvo_drzava = razdeliti_rojstvo[-1]

        ime1 = popravljeno
        datum1 = datum_rojstva_popravi(rojstvo_dan)
        leto_rojstva = rojstvo_leto
        drzava_rojstva = drzava_rojstva_popravi(popravi_drzava(rojstvo_drzava))
        dan_smrti = '/'
        leto_smrti = '/'
        kraj_smrti = '/'
        podrocje = samo_nagrada
        leto_nagrade1 = leto
        return v_slovar(ime1, datum1, leto_rojstva, drzava_rojstva, dan_smrti, leto_smrti, kraj_smrti, podrocje, leto_nagrade1)
    
    elif not smrt and not rojstvo:
        ime1 = popravljeno
        datum1 = '/'
        leto_rojstva = '/'
        drzava_rojstva = '/'
        dan_smrti = '/'
        leto_smrti = '/'
        kraj_smrti = '/'
        podrocje = samo_nagrada
        leto_nagrade1=leto
        return v_slovar(ime1, datum1, leto_rojstva, drzava_rojstva, dan_smrti,leto_smrti, kraj_smrti, podrocje, leto_nagrade1)
    
def v_slovar(ime1, datum1, leto_rojstva, drzava_rojstva, dan_smrti, leto_smrti, drzava_smrti, podrocje, leto_nagrade1):
   slovar={
        'ime':ime1,
        'datum rojstva':datum1,
        'leto rojstva': leto_rojstva,
        'drzava rojstva': drzava_rojstva,
        'dan smrti': dan_smrti,
        'leto smrti': leto_smrti,
        'drzava smrti': drzava_smrti,
        'področje nagrade':podrocje,
        'leto nagrade': leto_nagrade1
        
    }
   return slovar

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

def loci_rojstva_smrt(niz):
    if '(' not in niz:
        if niz!='/':
            niz1 = niz.split(',')
            if len(niz1)==3:
                datum, kraj, drzava = niz1
                print(datum, kraj, drzava)
                return datum, kraj, drzava
            elif len(niz1)==2:
                datum, drzava = niz1
                print(datum, drzava)
                return datum, drzava
            elif len(niz1)==4:
                datum, kraj, zvezna_drzava, drzava = niz1
                print(datum, kraj, zvezna_drzava, drzava)
                return datum, kraj, zvezna_drzava, drzava
            elif len(niz1)==5:
                datum, kraj, zvezna_drzava, kraj2, drzava = niz1
                print(datum, kraj, zvezna_drzava, kraj2, drzava)
                return datum, kraj, zvezna_drzava, kraj2, drzava
            elif len(niz1)==1:
                datum=niz1
                print(datum)
                return datum
    else:
        if niz!='/':
            niz1=niz.split('(')
            print(niz1)
            rojst_smrt = niz1[0]
            tisti_cas = rojst_smrt.split(',')

            if len(tisti_cas)==3:
                datum, kraj, drzava = tisti_cas
                print(datum, kraj, drzava)
                return datum, kraj, drzava
            elif len(tisti_cas)==2:
                datum, drzava = tisti_cas
                print(datum, drzava)
                return datum, drzava
            elif len(tisti_cas)==4:
                datum, kraj, zvezna_drzava, drzava = tisti_cas
                print(datum, kraj, zvezna_drzava, drzava)
                return datum, kraj, zvezna_drzava, drzava
            elif len(tisti_cas)==1:
                datum=tisti_cas
                print(datum)
                return datum
            
def popravi_drzava(niz):
    nov=niz.split()
    print(nov)
    sestavi = ''
    for beseda in range(0,len(nov)-1):
        sestavi+=nov[beseda]
        sestavi+=' '
    sestavi+=nov[len(nov)-1]
    print(sestavi)
    return sestavi

def datum_rojstva_popravi(niz):
    if len(niz)==4:
        return '/'
    else:
        return niz
    
def drzava_rojstva_popravi(niz):
    if len(niz)==4:
        a='17' or '18' or '19' or '20'
        if a in niz:
            return '/'
        elif a not in niz:
            return niz
    elif len(niz)!=4:
        return niz


po_datot_z_nagrjajenci(mapa_z_nagrajenci)
