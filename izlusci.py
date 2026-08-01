import re
import os


mapa_s_htmlji = 'htmlji'

def po_datot(mapa_s_htmlji):
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
            print(vrsta_nagrade,dobitnik_nagrade,priimki_dobitnikov)

                

po_datot(mapa_s_htmlji)





        












