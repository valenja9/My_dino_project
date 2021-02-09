import random
import string
import sys


TABLE = 'abcdefghijklmnopqrstuvwxyz '


def vytvoreni_textu():
    celkovy_text = ""
    for radek in range(900):
        text_pro_radek = ""
        for znak in range(900):
            text_pro_radek += random.choice(string.ascii_lowercase) \
                              + str(random.randint(0, 1000)) \
                              + random.choice(string.ascii_uppercase) \
                              + random.choice(string.punctuation)
        celkovy_text += text_pro_radek + "\n"
    return celkovy_text


def vytvoreni_txt_souboru(celkovy_text, jmeno):
    with open(f"{jmeno}.txt", mode="w") as file:
        writer = file.write(celkovy_text)


def cti_txt_soubor(jmeno_souboru):
    with open(f"{jmeno_souboru}", mode="r") as file:
         celkovy_text = file.read()
    return celkovy_text


def klic_pro_soubor(celkovy_text):
    sectu_cisla = 0  # cislo pro soucet
    for znak in celkovy_text:
        # Pro kazde pismeno v textu
        if znak.isdecimal():  # Kontrola jestli se jedna o cislo
            znak_je_cislo = int(znak)  # Pokud ano, tak znak preved na cislo
            sectu_cisla = sectu_cisla + znak_je_cislo  # cisla secti
    return sectu_cisla


def zasifruj_text_pomoci_CS(klic_pro_sifru, text):
    dict_ = {char: i for char, i in zip(TABLE, range(0, 27))}
    redict = {i: char for char, i in zip(TABLE, range(0, 27))}
    nova_zprava = ""
    for char in text:
        nova_zprava += char.replace(char, redict[((dict_[char] + klic_pro_sifru) % len(TABLE))])
    return nova_zprava


def dekoduj_text_pomoci_CS(klic_pro_sifru, text):
    dict_ = {char: i for char, i in zip(TABLE, range(0, 27))}
    redict = {i: char for char, i in zip(TABLE, range(0, 27))}
    nova_zprava = ""
    for char in text.split(".")[0]:
        nova_zprava += char.replace(char, redict[((dict_[char] - klic_pro_sifru) % len(TABLE))])
    return nova_zprava



def main():
    mode = sys.argv[1]
    text_pro_zasifrovani = " ".join([word.strip(",:;?!").lower() for word in sys.argv[2:]])
    print(text_pro_zasifrovani)

    if mode == "sifruji":
        text = vytvoreni_textu()
        klic_pro_sifru = klic_pro_soubor(text)
        sifra = zasifruj_text_pomoci_CS(klic_pro_sifru, text_pro_zasifrovani)
        print(sifra)
        vytvoreni_txt_souboru(text, sifra)
        print(f"Soubor se ulozil pod jmenem: {sifra}.txt ")

    else:
        jmeno_txt_souboru = sys.argv[2]
        text_ze_souboru = cti_txt_soubor(jmeno_txt_souboru)
        klic = klic_pro_soubor(text_ze_souboru)
        print("Klic, k souboru je: ", dekoduj_text_pomoci_CS(klic, jmeno_txt_souboru))
main()