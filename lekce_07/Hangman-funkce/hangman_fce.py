import os
from random import choice, seed

from slova import hadana_slova
from grafika import obesenec


def main():
    zivoty = 7
    hra_bezi = True
    hra(hra_bezi, zivoty)
    

def hra(hra_bezi, zivoty):
    slovo = choice(hadana_slova)
    tajenka = vytvor_tajenku(slovo, '_')
    
    while hra_bezi and zivoty > 0:
        zobraz_stav_hry(tajenka, obesenec, zivoty)

        hadani = input('Hadej pismeno/cele slovo: ')
        
        if hadani == slovo:
            hra_bezi = False
        elif hadani in slovo and len(hadani) == 1:
            indexy = je_pismeno_ve_slove(slovo, hadani)
            if indexy:
                tajenka = prepis_pismeno(indexy, tajenka, hadani)
            print('Uhodl jsi spravne pismeno!')
        
            hra_bezi = kompletni_tajenka(tajenka)
        else:
            print('Pismeno neni v tajence, hadej znova!')
            zivoty -= 1
    else:
        konec_hry(hra_bezi, slovo)

    
def vytvor_tajenku(slovo, znak):
    return [znak] * len(slovo)


def zobraz_stav_hry(tajenka, obesenec, zivoty):
    os.system("cls") #pro Linux a Mac -> clear
    print(f"Tajenka: {''.join(tajenka)}")
    print(obesenec[7 - zivoty])
    print(f"Zbyvajici pocet zivotu: {zivoty}")


def je_pismeno_ve_slove(slovo, hadani):  
    # for index, symbol in enumerate(slovo):
    #         if symbol == hadani:
    #             tajenka[index] = hadani
    return [
        index for index, symbol in enumerate(slovo)
        if hadani in symbol
        ]
    

def prepis_pismeno(indexy, tajenka, hadani):
    for index in indexy:
        tajenka[index] = hadani
    
    return tajenka


def kompletni_tajenka(tajenka):
    if '_' not in tajenka:
        return False
    else:
        return True
    # TODO DU: zapsat if else na jeden radek


def konec_hry(hra_bezi, slovo):
    if hra_bezi == False:
        print('Vyhral jsi!')
    else:
        print(f'Prohral jsi, tajenka byla "{slovo}"')


if __name__ == '__main__':
    main()
