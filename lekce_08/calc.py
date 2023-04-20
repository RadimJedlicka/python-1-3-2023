# importy


def show_selection(*args) -> None:
    """
    Popis:
    Funkce spoji poskytnute argumenty pomoci metody .join.
    Argumenty se oddeli pomoci separatoru.

    Priklad:
    args = ("a", "b", "c")

    Vysledek:
    ---------
    a | b | c 
    ---------
    """
    arguments = ' | '.join(*args)
    separator = '-' * len(arguments)
    print(separator, arguments, separator, sep='\n')


def pow() -> None:
    """
    Popis:
    Funkce se zepta uzivatele na mocnence a mocnitele,
    Vysledkem bude umocneni techto cisel.

    Priklad:
    base: 5
    exponent : 2

    Vysledek:
    5 ** 2 = 25
    """
    base = int(input('Base:' ))
    exponent = int(input('Exponent: '))
    result = base ** exponent
    print(result)


def count_average() -> None:
    cisla = []

    while (hodnota := input('Cislo: ')) != '=':
        cisla.append(int(hodnota))

    vysledek = sum(cisla) / len(cisla)
    print(f'Aritmeticky prumer je {vysledek}')



def calculator():
    """
    Hlavni funkce
    """
    selection = ('+', '-', '*', '/', 'pow', 'avg', 'quit')

    while True:
        show_selection(selection)
        
        vstup = input('Select math. operation: ')
        
        if vstup == 'quit':
            break
        elif vstup == 'pow':
            pow()
        elif vstup in 'avg':
            count_average()
        
        # elif:
        


        # break


if __name__ == '__main__':
    calculator()