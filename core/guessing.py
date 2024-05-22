import pandas as pd
import random

df = pd.read_csv('csv\main_6.csv')

def porownaj_rekordy(rekord1, rekord2):
    wspolne_pola = ''
    for kolumna in rekord1.index:
        if rekord1[kolumna] == rekord2[kolumna]:
            wspolne_pola += str(rekord1[kolumna])
            wspolne_pola += " "
    return wspolne_pola

losowy = df.sample().iloc[0]
print("Losowy rekord został wygenerowany. Spróbuj odgadnąć 'name'.")
print(losowy)
while True:
    odgadniete_imie = input("Podaj imię: ")
    if odgadniete_imie == losowy['name']:
        print("Gratulacje! Udało Ci się odgadnąć imię.")
        break
    else:
        ilosc_wspolnych_pol = porownaj_rekordy(df[df['name'] == odgadniete_imie].iloc[0], losowy)
        print("Nie udało się odgadnąć imienia.")
        print("Index: "+str(df[df['name'] == odgadniete_imie].index[0]))
        print("Wspolne pola:", ilosc_wspolnych_pol)
