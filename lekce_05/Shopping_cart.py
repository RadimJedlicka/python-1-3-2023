# TODO promenne
sklad = {
    'mleko':    [30,  5],    # index 0 -> cena; index 1 -> mnozstvi
    'maso':     [100, 1],
    'banan':    [30, 10],
    'jogurt':   [10,  5],
    'chleb':    [20,  5],
    'jablko':   [10, 10],
    'pomeranc': [15, 10], 
}

nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomeranc  |    15,-  |
+-----------+----------+
"""

oddelovac = '=' * 40

#--------------------------------------------

# TODO kosik = dict()
kosik = {}

# TODO Pozdrav a vypsani nabidky
print(
    'Vitejte v nasem online nakupnim kosiku', 
    oddelovac, 
    nabidka, 
    oddelovac,
    'Pro ukonceni nakupu zadej "KONEC"', 
    sep='\n'
    )

# TODO cely cyklus
while (zbozi := input("Zadej nazev zbozi: ")) != 'konec':

    # TODO pokud zbozi nebude v nabidce
    if zbozi not in sklad:
        print('Toto zbozi neni na sklade')

    # TODO Pokud vybrane zbozi neni v nakupnim kosiku
    elif zbozi not in kosik and sklad[zbozi][1] > 0:
        kosik[zbozi] = [sklad[zbozi], 1]
        sklad[zbozi][1] = sklad[zbozi][1] - 1
        print(kosik)

    # TODO pokud zbozi je v kosiku
    elif zbozi in kosik and sklad[zbozi][1] > 0:
        kosik[zbozi][1] += 1
        sklad[zbozi][1] -= 1
        print(kosik)

    # TODO pokud zbozi jiz neni skladem
    elif sklad[zbozi][1] == 0:
        print(f'{zbozi} jiz neni na sklade')

# TODO vypis kosiku
else:
    print(oddelovac, kosik, sep='\n')