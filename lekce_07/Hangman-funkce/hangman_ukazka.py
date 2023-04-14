import os
from random import choice

# from grafika import obesenec
# from slova import hadana_slova
hadana_slova = ['dva', 'hudba', 'vecernicek']

# Definice funkci ##################################################
def tajne_slovo():
    tajne_slovo = choice(hadana_slova)
    return tajne_slovo

def vytvor_tajenku(slovo):
    tajenka = ['_'] * len(slovo)
    return tajenka

def zobraz_stav_hry(tajenka, zivoty):
    os.system('cls')   # pro Linux a Mac -> 'clear'
    print(f"Tajenka: {''.join(tajenka)}")
    print(f"Zbyvajici pocet zivotu: {zivoty}")

def co_hada_uzivatel():
    hadani = input('Hadej pismeno/slovo: ')
    return hadani

def ziskej_indexy_pismen(slovo, hadani):
    indexy = []
    for index, symbol in enumerate(slovo):
        if symbol in hadani:
            indexy.append(index)
    return indexy

def dopis_pismena_do_tajenky(indexy, tajenka, hadani):
    for index in indexy:
        tajenka[index] = hadani
    return tajenka

def kompletni_tajenka(tajenka):
    if '_' not in tajenka:
        return False
    else:
        return True
    
def konec_hry(hra_bezi):
    if hra_bezi == False:
        print('Vyhral jsi!')
    else:
        print('Prohral jsi!')

###################################################################

def cela_hra():
    zivoty = 7
    hra_bezi = True
    slovo = tajne_slovo()
    tajenka = vytvor_tajenku(slovo)

    while hra_bezi and zivoty > 0:
        # stav hry
        zobraz_stav_hry(tajenka, zivoty)
        # input hadani
        hadani = co_hada_uzivatel()

        # if uhodnuti celeho slova
        if hadani == slovo:
            hra_bezi = False
        # elif hadani po pismenech
        elif hadani in slovo and len(hadani) == 1:
            # ziskat indexy
            indexy = ziskej_indexy_pismen(slovo, hadani)
            # nasazet uhodnuta pismenka do tajenky
            tajenka = dopis_pismena_do_tajenky(indexy, tajenka, hadani)

            hra_bezi = kompletni_tajenka(tajenka)

        # else pismeno neni v tajence
        else:
            zivoty -= 1

    else:
        # konec hry
        konec_hry(hra_bezi)


if __name__ == '__main__':
    cela_hra()
