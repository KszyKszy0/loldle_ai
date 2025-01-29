import tensorflow as tf
import pandas as pd
import random
import time
import numpy as np

dict_regions = {
    'Bandle City': 0,
    'Bilgewater': 1,
    'Demacia': 2,
    'Ionia': 3,
    'Ixtal': 4,
    'Noxus': 5,
    'Piltover': 6,
    'Shadow Isles': 7,
    'Shurima': 8,
    'Targon': 9,
    'Freljord': 10,
    'The Void': 11,
    'Zaun': 12,
    'Runeterra': 13
}

dict_gender = {
    'male': 14,
    'female': 15
}

dict_resource = {
    'Mana': 16,
    'Manaless': 17,
    'Energy': 18,
    'Fury': 19,
    'Grit': 20,
    'Ferocity': 21,
    'Courage': 22,
    'Shield': 23,
    'Health': 24,
    'Heat': 25,
    'Flow': 26
}

dict_ranged = {
    'melee': 27,
    'ranged': 28,
    'mixed': 29
}

dict_year = {
    '2009': 30,
    '2010': 31,
    '2011': 32,
    '2012': 33,
    '2013': 34,
    '2014': 35,
    '2015': 36,
    '2016': 37,
    '2017': 38,
    '2018': 39,
    '2019': 40,
    '2020': 41,
    '2021': 42,
    '2022': 43,
    '2023': 44,
    '2024': 45,
}

dict_adaptive = {
    'physical': 46,
    'magic': 47
}

dict_class = {
    'Enchanter': 48,
    'Catcher': 49,
    'Juggernaut': 50,
    'Diver': 51,
    'Burst': 52,
    'Battlemage': 53,
    'Artillery': 54,
    'Marksman': 55,
    'Assassin': 56,
    'Skirmisher': 57,
    'Vanguard': 58,
    'Warden': 59,
    'Specialist': 60
}

dict_regions_no = {
    'Bandle City': 61,
    'Bilgewater': 62,
    'Demacia': 63,
    'Ionia': 64,
    'Ixtal': 65,
    'Noxus': 66,
    'Piltover': 67,
    'Shadow Isles': 68,
    'Shurima': 69,
    'Targon': 70,
    'Freljord': 71,
    'The Void': 72,
    'Zaun': 73,
    'Runeterra': 74
}

dict_gender_no = {
    'male': 75,
    'female': 76
}

dict_resource_no = {
    'Mana': 77,
    'Manaless': 78,
    'Energy': 79,
    'Fury': 80,
    'Grit': 81,
    'Ferocity': 82,
    'Courage': 83,
    'Shield': 84,
    'Health': 85,
    'Heat': 86,
    'Flow': 87
}

dict_ranged_no = {
    'melee': 88,
    'ranged': 89,
    'mixed': 90
}

dict_year_no = {
    '2009': 91,
    '2010': 92,
    '2011': 93,
    '2012': 94,
    '2013': 95,
    '2014': 96,
    '2015': 97,
    '2016': 98,
    '2017': 99,
    '2018': 100,
    '2019': 101,
    '2020': 102,
    '2021': 103,
    '2022': 104,
    '2023': 105,
    '2024': 106,
}

dict_adaptive_no = {
    'physical': 107,
    'magic': 108
}

dict_class_no = {
    'Enchanter': 109,
    'Catcher': 110,
    'Juggernaut': 111,
    'Diver': 112,
    'Burst': 113,
    'Battlemage': 114,
    'Artillery': 115,
    'Marksman': 116,
    'Assassin': 117,
    'Skirmisher': 118,
    'Vanguard': 119,
    'Warden': 120,
    'Specialist': 121
}




df = pd.read_csv('main_6.csv')


state_list = []
results = []
real_results = []
false_results = []

state = [0]*122

def porownaj_rekordy(rekord1, rekord2):
    global state
    wspolne_pola = ''
    for kolumna in rekord1.index:
        if rekord1[kolumna] == rekord2[kolumna]:
            wspolne_pola += str(rekord1[kolumna])
            wspolne_pola += " "
            if kolumna == 'region':
                state[dict_regions[rekord1['region']]] = 1
            if kolumna == 'gender':
                state[dict_gender[rekord1['gender']]] = 1
            if kolumna == 'resource':
                state[dict_resource[rekord1['resource']]] = 1
            if kolumna == 'ranged':
                state[dict_ranged[rekord1['ranged']]] = 1
            if kolumna == 'year':
                state[dict_year[str(rekord1['year'])]] = 1
            if kolumna == 'adaptive':
                state[dict_adaptive[rekord1['adaptive']]] = 1
            if kolumna == 'class':
                state[dict_class[rekord1['class']]] = 1
        else:
            if kolumna == 'region':
                state[dict_regions_no[rekord1['region']]] = 1
            if kolumna == 'gender':
                state[dict_gender_no[rekord1['gender']]] = 1
            if kolumna == 'resource':
                state[dict_resource_no[rekord1['resource']]] = 1
            if kolumna == 'ranged':
                state[dict_ranged_no[rekord1['ranged']]] = 1
            if kolumna == 'year':
                state[dict_year_no[str(rekord1['year'])]] = 1
            if kolumna == 'adaptive':
                state[dict_adaptive_no[rekord1['adaptive']]] = 1
            if kolumna == 'class':
                state[dict_class_no[rekord1['class']]] = 1
    return wspolne_pola

def guess_name(name,sleeptime,view_mode,model):
    global state
    licznik = 0
    losowy = df[df['name'] == name].iloc[0]
    state = [0]*122
    temp_result = [0]*167
    temp_result[losowy.name]=1
    checked_indices = []
    # print(temp_result)
    if view_mode:
        print("Losowy rekord został wygenerowany. Spróbuj odgadnąć 'name'.")
        print(losowy)
    cancel = False
    while True:
        # odgadniete_imie = input("Podaj imię: ")
        # if odgadniete_imie == 'z':
        #     break
        # odgadniete_imie = input("Podaj imię: ")
        odgadniete_imie = df.sample().iloc[0]['name']
        model_values = model.predict(np.array(state).reshape(1, -1),verbose=0)
        while True:
            if np.argmax(model_values) in checked_indices:
                model_values[0][np.argmax(model_values)]=0
            else:
                checked_indices.append(np.argmax(model_values))
                break
        odgadniete_imie = df.iloc[np.argmax(model_values)]['name']
        false_predict = np.argmax(model_values)

        # Pobranie indeksów 10 największych prawdopodobieństw dla każdego przykładu
        top_k_indices = tf.math.top_k(model_values, k=10).indices.numpy()

        # Pobranie wartości 10 największych prawdopodobieństw dla każdego przykładu
        top_k_values = tf.math.top_k(model_values, k=10).values.numpy()

        # Wypisanie wyników
        if view_mode:
            for i in range(len(model_values)):
                print("Największe prawdopodobieństwa dla przykładu", ":")
                for j in range(len(top_k_indices[i])):
                    print("Klasa:", df.iloc[top_k_indices[i][j]]['name'], "Prawdopodobieństwo:", top_k_values[i][j])


            time.sleep(sleeptime)
            print(odgadniete_imie)
        licznik += 1
        if odgadniete_imie == losowy['name']:
            if view_mode:
                print("Gratulacje! Udało Ci się odgadnąć imię.")
                print("Ilość prób:",licznik)
            state_list.append(state)
            results.append(temp_result)
            false_results.append(false_predict)
            real_results.append(losowy.name)
            return licznik
        else:
            ilosc_wspolnych_pol = porownaj_rekordy(df[df['name'] == odgadniete_imie].iloc[0], losowy)
            if view_mode:
                print(state)
                print("Nie udało się odgadnąć imienia.")
                print("Index: "+str(df[df['name'] == odgadniete_imie].index[0]))
                print("Wspolne pola:", ilosc_wspolnych_pol)
            #print(state)
            state_list.append(state)
            results.append(temp_result)
            false_results.append(false_predict)
            real_results.append(losowy.name)

def stress_test(model_path,full_list):
    model = tf.keras.models.load_model(model_path)
    counter = 0
    temp = 0
    max_res = 0
    avg = 0
    max_arr = []
    min_arr = []
    min_res = 100
    pary = []
    model = tf.keras.models.load_model(model_path)
    for index, champ in df.iterrows():
        temp = guess_name(champ['name'],0,False,model)
        avg += temp
        counter += 1
        if temp != 1:
            if temp >= max_res:
                if temp > max_res:
                    max_arr = []
                max_res = temp
                max_arr.append(champ['name'])
            if temp <= min_res:
                if temp < min_res:
                    min_arr = []
                min_res = temp
                min_arr.append(champ['name'])
        pary.append((champ['name'],temp))
        print(counter)
    if full_list:
        pary_posortowane = sorted(pary, key=lambda x: x[1], reverse=True)
        for para in pary_posortowane:
            print(para[0], para[1])
    print("AVG",avg/counter)
    print("Worst",max_res,max_arr)
    print("Best",min_res,min_arr)
    print("Model_name",model_path)

model_path = "mixed_model_0_1.h5"

model = tf.keras.models.load_model(model_path)
model.summary()
stress_test(model_path,True)
# model.save("best_model.keras")
# model.save("best_model.h5")
#guess_name("Jhin",1,True,model)