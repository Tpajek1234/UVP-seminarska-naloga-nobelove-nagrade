
import os
import pridobi_podatke
import izlusci
import izlusci_nagrajence


leto = 2025

if not os.path.exists('htmlji'):
    pridobi_podatke.koda_za_htmlje(leto)

if not os.path.exists('nobelovi_nagrajenci'):
    izlusci.pobere_o_nagrajencih(izlusci.izlusci_vse_povezave_nagrajencev())



izlusci_o_nagraj = izlusci_nagrajence.po_datot_z_nagrjajenci()
izlusci_nagrajence.shrani_v_csv(izlusci_o_nagraj)