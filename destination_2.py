MESTA = ('Praha', 'Viden','Olomouc','Svitavy','Zlin','Ostrava')
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = '================================================================'
SLEVY = ('Olomouc','Ostrava')
AKTUALNI_ROK = 2020
sleva_v_desetinych_cislech = 0.75


print(ODDELOVAC)
print('Vytejte v nasi aplikaci.')
print(ODDELOVAC) #pouzijeme viceradkovy string
print('''
1 - Praha   | 150 
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
''')
print(ODDELOVAC)


index_destinace = int(input("Zadej cislo destinace: "))
if (index_destinace - 1) in range(len(MESTA)):

    destinace = MESTA[index_destinace-1]
    cena = CENY[index_destinace-1]

    #Kontroluji jestli je destinace ve SLEVACH
    if destinace in SLEVY:
      cena_po_sleve = cena * sleva_v_desetinych_cislech
    else:
      cena_po_sleve = cena

    #kontrola jmena a prijmeni:
    prijmeni = input("Zadej prijmeni: ")
    jmeno = input("Zadej jmeno: ")

    if (jmeno + prijmeni).isalpha():
        print(f'Jmeno: {jmeno}, prijmeni: {prijmeni}')
    else:
        print('Jmeno a prijmeni musi obsahovat pouze pismena.')
        exit()

    # Vek narozeni
    rok_narozeni = int(input("Zadej rok narozeni: "))
    kontrola = AKTUALNI_ROK - rok_narozeni

    if kontrola >= 18:
        print("Pokračuj...")
    else:
        print('Nase sluzby jsou az od 18 let.')
        exit()

    # mail
    email = input('Email: ')

    if ("@" in email) and ("." in email):
        print("Email v poradku")
    else:
        print("Zadal jsi Email ve spatnem formatu. Musi tam byt @!")
        exit()

    #overeni hesla
    heslo = input("Heslo: ")
    if len(heslo)  >= 8 and not heslo.isalpha() and not heslo.isdecimal():
        print('Heslo je v poradku.')
        print(ODDELOVAC)
        print('Uzivatel: ' + jmeno)
        print('Destinace: ' + destinace)
        print(f'Cena(cil: {destinace})' + str(cena_po_sleve))
        print('jizdenku posleme na Vasi adresu: ', email)

    else:
        print('''Vami zadane heslo je spatn! 
          1. Musi obsahovat Jak pismena, tak cislice
          2. Musi byt alespon 8 znaku dlouhe''')
        exit()




else:
    print(f"Vyber destinace cisla od 1 do {len(MESTA)}")
    exit()





