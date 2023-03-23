###### VSTUPNI DATA ###############################################

mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
slevy = ("Olomouc", "Svitavy", "Ostrava")
domeny = ("gmail.com", "seznam.cz", "email.cz")
dvojita_cara = "=" * 35
cara = "-" * 35
AKT_ROK = 2021

nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

###### POZDRAV A NABIDKA ############################################

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(dvojita_cara, end='')
print(nabidka, end='')
print(dvojita_cara)

###### VYBER DESTINACE ##############################################

destinace_cislo = int(input("Vyber cislo destinace: "))

if destinace_cislo >= 1 and destinace_cislo <= 6:
    destinace_nazev = mesta[destinace_cislo - 1]
    print(f"Destinace: {destinace_nazev.upper()}")
else:
    print(f"Destinace cislo {destinace_cislo} NEEXISTUJE!")
    quit()
print(cara)

###### PREPOCET PO SLEVE #############################################

if destinace_nazev in slevy:
    nova_cena = 0.75 * ceny[destinace_cislo -1]
    print(f"Ziskavate 25% slevu! Nova cena: {nova_cena},-")
else:
    nova_cena = ceny[destinace_cislo - 1]
    print(f"Jizdenka bez slevy. Cena: {nova_cena},-")
print(cara)

###### JMENO UZIVATELE ################################################

cele_jmeno = input("Vase cele jmeno: ")

krestni_jmeno = cele_jmeno.split()[0]
if krestni_jmeno.isalpha():
    print(f"Krestni jmeno: {krestni_jmeno}")
else:
    print("Neplatne jmeno!")
print(cara)

###### KONTROLA VEKU ###################################################

rok_narozeni = int(input("Vas rok narozeni: "))

if (AKT_ROK - rok_narozeni) >= 18:
    print(f"Pristup povolen...")
else:
    print("Jste prilis mlady na nakup jizdenek!")
    print("Ukoncuji program")
    quit()
print(cara)

###### VALIDACE E-MAILU #################################################

email = input("Zapis vasi e-mailovou adresu:")

if "@" in email and email.split("@")[1] in domeny:
    print("Overeni e-mailu probehlo v poradku.")
else:
    print("Tento e-mail je neplatny!")
    print("Ukoncuji program")
    quit()
print(dvojita_cara)

###### ZAVERECNA ZPRAVA ##################################################

print(f"""Dekuji, {krestni_jmeno} za objednavku jizdenky.
Cilova destinace: {destinace_nazev}, cena jizdneho: {nova_cena},-
Na Vas e-mail: {email} jsme odeslali e-jizdenku."""
)
print(dvojita_cara * 2)
