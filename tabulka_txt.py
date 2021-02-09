#Vytror kod, ktery mi do umozni ze zadane tabulky zapsat data do txt souboru. A opacne z txt souboru udela tabulku.
#Pouzij aspon jednu vyjimku.
import time
import logging
import sys
import os



tabulka = [["Jmeno", "Prijmeni", "Vek"],["Petr","Novotny", 45], ["Hanka","Bila", 33], ["Sabima","Suchanova", 11]]



def vytvor_file(data:list, cesta:str) -> None:
    os.chdir(os.getcwd() + "/" + "textove_tabulky")
    with open(cesta, mode="w") as file:
        for row in data:
            jmeno, prijmeni, vek = row
            text = f"{jmeno},{prijmeni},{vek}" + "\n"
            print(text)
            file.writelines(text)

def precti_file_a_vytvor_list(cesta:str) -> list:
    data = []
    try:
        logging.basicConfig(level=logging.DEBUG, filename='myapp.log', format='%(asctime)s %(levelname)s:%(message)s')
        with open(cesta, mode= "r") as file:
            for radek in file.readlines():
                list_hodnot = "".join(radek).replace("\n","").split(",")
                print(list_hodnot[2])
                try:
                    list_hodnot[2] = int(list_hodnot[2])
                    data.append(list_hodnot)
                except ValueError:
                    data.append(list_hodnot)
        return data
    except FileNotFoundError as ve:
        logging.error(f"Tento soubor neexistuje! nastala chyba :{ve.__class__.__name__}")
        print(f"Tento soubor neexistuje! nastala chyba :{ve.__class__.__name__}")
def main():
    mode = sys.argv[1].lower()
    print(mode)
    jmeno_souboru = sys.argv[2]
    print(jmeno_souboru)
    if mode == "r":
        list_listu = precti_file_a_vytvor_list(jmeno_souboru)
        print(type(list_listu), list_listu)
    elif mode == "w":
        tabulka = eval(input("Zadej svuj list listu: "))
        vytvor_file(tabulka, jmeno_souboru)
    else:
        print("Zadal jsi spatny mod!")
        exit()
def overeni_slozky():
    try:
        os.mkdir("textove_tabulkyII")
    except FileExistsError:
        print("Slozka uz existuje")

if __name__ == "__main__":
    overeni_slozky()
    print("Prave jsi spustil tento soubor: ", sys.argv[0])
    zacatek = time.time()
    main()
    konec = time.time()
    print("Jak dlouho trva tva prace? ", konec - zacatek)