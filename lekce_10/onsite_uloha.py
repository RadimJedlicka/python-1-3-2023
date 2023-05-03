import os


txt_soubor = 'countries_and_cities.txt'


def nacti_txt_soubor(jmeno: str, encoding: str = 'UTF-8') -> list:
    try:
        with open(jmeno, mode='r', encoding=encoding) as txt:
            obsah = txt.readlines()
    
    except FileNotFoundError:
        print(
            f'SOUBOR: {jmeno} NEBYL NALEZEN!',
            f'AKTUALNI ADRESAR: {os.getcwd()}',
            f'OBSAH ADRESARE: {os.listdir()}', sep='\n'
        )
    else:
        print(f'SOUBOR: {jmeno} NACTEN')
        return obsah
    finally:
        print(f'UKONCUJI FUNKCI: nacti_txt_soubor\n')

        
def zformatuj_nazvy():
    for udaj in nacti_txt_soubor(txt_soubor):
        if 'quit' in udaj.lower():
            break
        else:
            zeme, mesto = udaj.split(', ')
            
            print(f'{zeme=:<15} {mesto=}')


zformatuj_nazvy()