import os
from random import choice, seed

from slova import hadana_slova
from grafika import obesenec


zivoty = 7
hra_bezi = True
seed(2) # slovo je 'vojna'
slovo = choice(hadana_slova)
tajenka = ['_'] * len(slovo)

while hra_bezi and zivoty > 0:
    os.system("cls") #pro Linux a Mac -> clear
    print(f"Tajenka: {''.join(tajenka)}")
    print(obesenec[7 - zivoty])
    print(f"Zbyvajici pocet zivotu: {zivoty}")
    hadani = input('Hadej pismeno/cele slovo: ')
    
    if hadani == slovo:
        hra_bezi = False
    elif hadani in slovo and len(hadani) == 1:
        for index, symbol in enumerate(slovo):
            if symbol == hadani:
                tajenka[index] = hadani
        print('Uhodl jsi spravne pismeno!')
        if '_' not in tajenka:
            hra_bezi = False
    else:
        print('Pismeno neni v tajence, hadej znova!')
        zivoty -= 1
else:
    if hra_bezi == False:
        print('Vyhral jsi!')
    else:
        print(f'Prohral jsi, tajenka byla "{slovo}"')
