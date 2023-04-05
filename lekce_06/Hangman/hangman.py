# TODO importy zakladnich knihoven (modulu)
import random

# TODO importy vlastnich modulu
import slova
from grafika import obesenec


# TODO promenne
zivoty = 7
hra_bezi = True
slovo = random.choice(slova.hadana_slova)
tajenka = ['_'] * len(slovo)


# TODO hlavni smycka hry
while hra_bezi and zivoty > 0:
    # TODO zobraz tajenku
    print("Tajenka:", ' '.join(tajenka))
    print(slovo)
    print(obesenec[7 - zivoty])
    # TODO input
    hadani = input('Hadej pismeno nebo slovo: ')
    # TODO pokud uzivatel uhadl cele slovo
    if hadani == slovo:
        print('Vyborne, vyhral jsi!')
        hra_bezi = False

    # TODO pokud uzivatel uhadne pismeno
    elif hadani in slovo and len(hadani) == 1:
        print('Uhodl jsi pismeno')

        # TODO pokud uzivatel vsechna pismeno po jednom
   
    # TODO pokud uzivatel uhadl spatne pismeno
    else:
        print('Pismeno neni v tajence.')
        # zivoty = zivoty - 1
        zivoty -= 1
        print(f'Zbyva ti {zivoty} zivotu.')
        # print('Zbyva ti', zivoty,'zivotu.')

# TODO vypis else po tom, co je while cyklus prerusen
else:
    if not hra_bezi:
        print(f'Tajenka: {slovo}, Vyhral jsi')
    else:
        print('Prohral jsi, smula, snad priste')
