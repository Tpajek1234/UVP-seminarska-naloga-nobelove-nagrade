import os
import pridobi_podatke
import izlusci
import izlusci_nagrajence

leto = 2025

if not os.path.exists("htmlji"):  # shrani htmlje spletnih strani v mapo htmlji
    pridobi_podatke.koda_za_htmlje(leto)  # podatki pobrani 31.7.2026

if not os.path.exists("nobelovi_nagrajenci"):  # shrani htmlje strani nagrajencev v mapo
    izlusci.pobere_o_nagrajencih(
        izlusci.izlusci_vse_povezave_nagrajencev()
    )  # pobrano 2.8.2026


izlusci_o_nagraj = izlusci_nagrajence.po_datot_z_nagrjajenci()
izlusci_nagrajence.shrani_v_csv(izlusci_o_nagraj)  # shrani podatke v csv datoteko
