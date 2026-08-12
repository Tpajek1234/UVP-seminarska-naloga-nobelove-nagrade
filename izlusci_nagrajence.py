import os
import re
import csv


def po_datot_z_nagrjajenci():
    sez = []

    for html in os.listdir("nobelovi_nagrajenci"):
        if html.endswith(".html"):
            pot = os.path.join("nobelovi_nagrajenci", html)

            with open(pot, encoding="utf-8") as d:
                preberi_html = d.read()

                k = izlusci_o_nagrajencih(preberi_html)
                if k is not None:
                    sez.append(k)
    print(sez)
    return sez


def popravi_ime(nagr):  # popravi ime da ni t-jev
    nova_nagr = nagr.strip()
    return nova_nagr


def izlusci_o_nagrajencih(preberi_html):
    ime_dobitnika = re.search(
        r'<div class="content">\s*<p>(.*?)<br>', preberi_html, re.DOTALL
    )

    nagrada = re.search(
        r'<div class="content">\s*<p>.*?<br>\s*(.*?)</p>', preberi_html, re.DOTALL
    )

    rojstvo = re.search(
        r'<p class="born-date">Born:(.*?)\s*</p>', preberi_html, re.DOTALL
    )

    smrt = re.search(r'<p class="dead-date">Died:(.*?)</p>', preberi_html, re.DOTALL)
    return vse_v_slovar(ime_dobitnika, nagrada, rojstvo, smrt)


def vse_v_slovar(ime_dobitnika, nagrada, rojstvo, smrt):
    popravljeno = ime_apostrof(popravi_ime(ime_dobitnika.group(1)))
    nagrada2 = odstrani_nobel_prize(popravi_ime(nagrada.group(1)))
    leto = loci_leto(nagrada2)
    samo_nagrada = loci(nagrada2)

    if smrt:
        razdeliti_rojstvo = popravi_ime(rojstvo.group(1))
        datum_rojstva = samo_datum_rojstva(razdeliti_rojstvo)
        rojstvo_dan = loci(datum_rojstva)
        rojstvo_leto = loci_leto(datum_rojstva)
        rojstvo_drzava = samo_drzava1(razdeliti_rojstvo)

        razdeliti_smrt = popravi_ime(smrt.group(1))
        datum_smrti = samo_datum_rojstva(razdeliti_smrt)
        smrt_dan = loci(datum_smrti)
        smrt_leto = loci_leto(datum_smrti)
        smrt_drzava = samo_drzava1(razdeliti_smrt)

        ime1 = popravljeno
        datum1 = datum_rojstva_popravi(rojstvo_dan)
        leto_rojstva = rojstvo_leto
        drzava_rojstva = drzava_rojstva_popravi(odstrani_oklepaje(rojstvo_drzava))
        dan_smrti = datum_rojstva_popravi(smrt_dan)
        leto_smrti = smrt_leto
        kraj_smrti = drzava_rojstva_popravi(odstrani_oklepaje(smrt_drzava))
        podrocje = samo_nagrada
        leto_nagrade1 = leto
        return v_slovar(
            ime1,
            datum1,
            leto_rojstva,
            drzava_rojstva,
            dan_smrti,
            leto_smrti,
            kraj_smrti,
            podrocje,
            leto_nagrade1,
        )

    elif rojstvo:
        rojstvo_dan_leto = popravi_ime(rojstvo.group(1))
        datum_rojstva = samo_datum_rojstva(rojstvo_dan_leto)
        rojstvo_dan = loci(datum_rojstva)
        rojstvo_leto = loci_leto(datum_rojstva)
        rojstvo_drzava = samo_drzava1(rojstvo_dan_leto)

        ime1 = popravljeno
        datum1 = datum_rojstva_popravi(rojstvo_dan)
        leto_rojstva = rojstvo_leto
        drzava_rojstva = drzava_rojstva_popravi(odstrani_oklepaje(rojstvo_drzava))
        dan_smrti = "/"
        leto_smrti = "/"
        kraj_smrti = "/"
        podrocje = samo_nagrada
        leto_nagrade1 = leto
        return v_slovar(
            ime1,
            datum1,
            leto_rojstva,
            drzava_rojstva,
            dan_smrti,
            leto_smrti,
            kraj_smrti,
            podrocje,
            leto_nagrade1,
        )

    elif not smrt and not rojstvo:
        ime1 = popravljeno
        datum1 = "/"
        leto_rojstva = "/"
        drzava_rojstva = "/"
        dan_smrti = "/"
        leto_smrti = "/"
        kraj_smrti = "/"
        podrocje = samo_nagrada
        leto_nagrade1 = leto
        return v_slovar(
            ime1,
            datum1,
            leto_rojstva,
            drzava_rojstva,
            dan_smrti,
            leto_smrti,
            kraj_smrti,
            podrocje,
            leto_nagrade1,
        )


def v_slovar(
    ime1,
    datum1,
    leto_rojstva,
    drzava_rojstva,
    dan_smrti,
    leto_smrti,
    drzava_smrti,
    podrocje,
    leto_nagrade1,
):
    slovar = {
        "ime": ime1,
        "datum_rojstva": datum1,
        "leto_rojstva": leto_rojstva,
        "država_rojstva": drzava_rojstva,
        "dan_smrti": dan_smrti,
        "leto_smrti": leto_smrti,
        "država_smrti": drzava_smrti,
        "področje_nagrade": podrocje,
        "leto_nagrade": leto_nagrade1,
    }
    return slovar


def ime_apostrof(ime):
    vzorec = " &#039;"
    if vzorec in ime:
        ime1 = ime.replace(vzorec, "'")
        return ime1
    else:
        return ime


def odstrani_nobel_prize(nagrada):
    odstranit = "Nobel Prize in "
    ekonomska_nagrada = "Sveriges Riksbank Prize in "
    mir = "Nobel Peace Prize"

    if odstranit in nagrada:
        nova_nagrada = nagrada.replace(odstranit, "")
        return nova_nagrada

    elif ekonomska_nagrada in nagrada:
        nova_nagrada = nagrada.replace(ekonomska_nagrada, "")
        return nova_nagrada

    elif mir in nagrada:
        nova_nagrada = nagrada.replace(mir, "")
        nagrada1 = "Peace" + nova_nagrada
        return nagrada1


def loci_leto(nagrad):
    loci = nagrad.split()
    return int(loci[-1])


def loci(nagrad):
    loci = nagrad.split()
    nagrada = ""
    for beseda in range(0, len(loci) - 2):
        nagrada += loci[beseda]
        nagrada += " "
    nagrada += loci[len(loci) - 2]
    return nagrada


def samo_drzava1(niz):
    if "," in niz:
        loci_po_vejici = niz.split(",")
        return loci_po_vejici[-1]
    else:
        return "/"


def samo_datum_rojstva(niz):
    if "," in niz:
        loci_po_vejici = niz.split(",")
        return loci_po_vejici[0]
    else:
        return niz


def popravi_drzava(niz):
    nov = niz.split()
    sestavi = ""
    for beseda in range(0, len(nov) - 1):
        sestavi += nov[beseda]
        sestavi += " "
    sestavi += nov[len(nov) - 1]
    return sestavi


def odstrani_oklepaje(niz):
    drzava = popravi_drzava(niz)
    if "(" in drzava and ")" in drzava:
        najdi_okl = drzava.find("(")
        najdi_zakl = drzava.find(")")
        if "now " in drzava:
            return drzava[najdi_okl + 5 : najdi_zakl]
        else:
            return drzava[najdi_okl + 1 : najdi_zakl]

    elif drzava.endswith(")"):
        return drzava[0 : len(drzava) - 1]
    else:
        return drzava


def datum_rojstva_popravi(niz):
    if len(niz) == 4:
        return "/"
    else:
        return niz


def drzava_rojstva_popravi(niz):
    if len(niz) == 4:
        if niz.startswith(("17", "18", "19", "20")):
            return "/"
        else:
            return niz
    elif niz.startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9")):
        return "/"
    elif len(niz) != 4:
        return niz


def shrani_v_csv(podatki):
    with open("nobelovi_nagrajenci.csv", "w", newline="", encoding="utf-8") as dat:
        pisatelj = csv.DictWriter(
            dat,
            fieldnames=[
                "ime",
                "datum_rojstva",
                "leto_rojstva",
                "država_rojstva",
                "dan_smrti",
                "leto_smrti",
                "država_smrti",
                "področje_nagrade",
                "leto_nagrade",
            ],
        )
        pisatelj.writeheader()
        pisatelj.writerows(podatki)
