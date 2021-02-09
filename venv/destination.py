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

    rok_narozeni = int(input("Zadej rok narozeni: "))
    kontrola = AKTUALNI_ROK - rok_narozeni

    if kontrola >= 18:
        print("Pokračuj...")
    else:
      print('Nase sluzby jsou az od 18 let.')
      exit()

    email = input('Email: ')

    if ("@" in email) and ("." in email):
        print("Email v poradku")
    else:
        print("Zadal jsi Email ve spatnem formatu. Musi tam byt @!")
        exit()
else:
    print(f"Vyber destinace cisla od 1 do {len(MESTA)}")
    exit()





