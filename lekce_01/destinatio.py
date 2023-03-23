mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150,-Kč
2 - Viden   | 200,-Kč
3 - Olomouc | 120,-Kč
4 - Svitavy | 120,-Kč
5 - Zlin    | 100,-Kč
6 - Ostrava | 180,-Kč
"""

################################################

print('VITEJTE U NASI APLIKACE DESTINATIO!')
print(cara)
print(nabidka)

destinace = input('Cislo destinace: ')
cilova_destinace = mesta[int(destinace) - 1]
finalni_cena = ceny[int(destinace) - 1]

print(cara)
print()

jmeno = input('Jmeno: ')
prijmeni = input('Prijmeni: ')
email = input('Email: ')

# print(cilova_destinace)
# print(str(finalni_cena) + ',-Kc')

print(cara)
print()

print('Cestujici: ' + str(jmeno) + ' ' + str(prijmeni))
print('Cilova destinace: ' + str(cilova_destinace))
print('Cena jizdneho: ' + str(finalni_cena) + ',-Kc')
print('Jizdenku jsme odeslali na: ' + str(email))
