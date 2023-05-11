import json
import csv
import os
from pprint import pprint


rel_cesta = 'solution/'
zadouci_klice = ('first_name', 'last_name', 'email')

def json_to_csv():
    jsony = najdi_jsony(rel_cesta)

    obsah_jsonu = []

    for soubor in jsony:
        for zaznam in precti_json(soubor):
            obsah_jsonu.append(filtr_klicu(zaznam, zadouci_klice))

    zapis_csv('result.csv', obsah_jsonu)

    
def zapis_csv(cilovy_soubor, zaznamy):
    with open(cilovy_soubor, 'w', encoding='UTF-8', newline='') as csv_vystup:
        zapis = csv.DictWriter(csv_vystup, fieldnames=zaznamy[0].keys())
        zapis.writeheader()
        zapis.writerows(zaznamy)
        print(f'Soubor {cilovy_soubor} byl zapsan na disk')


def filtr_klicu(puvodni_zaznam, zadouci_klice):
    vycisteny_zaznam = {}

    for klic in puvodni_zaznam.keys():
        if klic not in zadouci_klice:
            continue
        vycisteny_zaznam[klic] = puvodni_zaznam[klic]

    return vycisteny_zaznam


def precti_json(jmeno):
    try:
        soub_json = open(os.path.join('solution', jmeno), mode='r', encoding='UTF-8')
    except FileNotFoundError:
        print('File not found')
    else:
        lide_info = json.load(soub_json)
        soub_json.close()
        return lide_info


def najdi_jsony(adresar: str) -> list:
    list_souboru = []

    for jmeno in os.listdir(adresar):
        if os.path.splitext(jmeno)[1] == '.json' and '_' in jmeno:
            list_souboru.append(jmeno)

    return list_souboru



test = json_to_csv()
pprint(test)