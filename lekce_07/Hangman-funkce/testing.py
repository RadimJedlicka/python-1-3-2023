import os  # from IPython.display import clear_output
import random

from slova import hadana_slova
from grafika import obesenec


def obesenec():
    zivoty = 7
    hra_bezi = True
    hra(zivoty, hra_bezi)


def hra(zivoty, hra_bezi):
    slovo = random.choice(hadana_slova)                                               
    tajenka = vytvor_tajenku(slovo, "_")                                       

    while hra_bezi and zivoty:                                                  
        zobraz_stav_hry(zivoty, tajenka)
        print(slovo)
        hadani = input("Hadej pismeno/slovo:")                                  

        if hadani == slovo:                                                     
            hra_bezi = False                                                    
        elif len(hadani) == 1 and hadani in slovo:
            indexy = je_pismeno_ve_slove(slovo, hadani)
            print(indexy)
            # správné hádání                       
            pass
            # přepisování tajenky
            # konec hádání                            
        else:                                                                   
            zivoty -= 1                                                         

    else:
        print("Konec!")


def vytvor_tajenku(slovo, znak):                                                
    return len(slovo) * [znak]


def zobraz_stav_hry(zivoty, tajenka):                                           
    os.system("clear")                                                          
    print(                                                                      
        f"TAJENKA: {' '.join(tajenka)}; ZIVOTY: {zivoty}",                      
        # obesenec[7 - zivoty],                                                    
        sep="\n"                                                                
    )


def je_pismeno_ve_slove(slovo, hadani):
    return [
        index for index, pismeno in enumerate(slovo)
        if hadani in pismeno
    ]

obesenec()