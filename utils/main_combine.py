import tensorflow as tf
import pandas as pd
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn import metrics

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

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(122, )),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dropout(0.2),  # Dodaj warstwę Dropout z prawdopodobieństwem odrzucenia 0.2
    tf.keras.layers.Dense(167, activation='softmax'),
])
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
#model = tf.keras.models.load_model('model_2.0_loldle')

df = pd.read_csv('main_6.csv')
state_list = []
results = []
real_results = []
false_results = []
state = [0]*122

def porownaj_rekordy(rekord1, rekord2):
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

def guess_name(name,sleeptime):
    losowy = df[df['name'] == name].iloc[0]
    state = [0]*122
    temp_result = [0]*167
    temp_result[losowy.name]=1
    checked_indices = []
    # print(temp_result)
    print("Losowy rekord został wygenerowany. Spróbuj odgadnąć 'name'.")
    print(losowy)
    cancel = False
    while True:
        # odgadniete_imie = input("Podaj imię: ")
        # if odgadniete_imie == 'z':
        #     break
        # odgadniete_imie = input("Podaj imię: ")
        odgadniete_imie = df.sample().iloc[0]['name']
        model_values = model.predict(np.array(state).reshape(1, -1))
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
        for i in range(len(model_values)):
            print("Największe prawdopodobieństwa dla przykładu", ":")
            for j in range(len(top_k_indices[i])):
                print("Klasa:", df.iloc[top_k_indices[i][j]]['name'], "Prawdopodobieństwo:", top_k_values[i][j])

        time.sleep(sleeptime)
        print(odgadniete_imie)
        
        if odgadniete_imie == losowy['name']:
            print("Gratulacje! Udało Ci się odgadnąć imię.")
            state_list.append(state)
            results.append(temp_result)
            false_results.append(false_predict)
            real_results.append(losowy.name)
            break
        else:
            ilosc_wspolnych_pol = porownaj_rekordy(df[df['name'] == odgadniete_imie].iloc[0], losowy)
            print("Nie udało się odgadnąć imienia.")
            print("Index: "+str(df[df['name'] == odgadniete_imie].index[0]))
            print("Wspolne pola:", ilosc_wspolnych_pol)
            #print(state)
            state_list.append(state)
            results.append(temp_result)
            false_results.append(false_predict)
            real_results.append(losowy.name)

def make_data_times(how_many,random):
    for i in range(how_many):
        print(i)
        for indx in df.index:
            checked_indices = []
            print(indx)
            losowy = df.iloc[indx]
            state = [0]*122
            temp_result = [0]*167
            temp_result[losowy.name]=1
            # print(temp_result)
            # print("Losowy rekord został wygenerowany. Spróbuj odgadnąć 'name'.")
            # print(losowy)
            while True:
                if random:
                    odgadniete_imie = df.sample().iloc[0]['name']
                    false_predict=df[df['name'] == odgadniete_imie].index[0]
                    while false_predict in checked_indices:
                        odgadniete_imie = df.sample().iloc[0]['name']
                        false_predict=df[df['name'] == odgadniete_imie].index[0]
                    checked_indices.append(false_predict)
                else:
                    model_values = model.predict(np.array(state).reshape(1, -1),verbose=0)
                    while True:
                        if np.argmax(model_values) in checked_indices:
                            model_values[0][np.argmax(model_values)]=0
                        else:
                            checked_indices.append(np.argmax(model_values))
                            break        
                    odgadniete_imie = df.iloc[np.argmax(model_values)]['name']
                    false_predict = np.argmax(model_values)
                    # print(odgadniete_imie)
                #time.sleep(1)
                #print(odgadniete_imie)

                if odgadniete_imie == losowy['name']:
                    # print("Gratulacje! Udało Ci się odgadnąć imię.")
                    state_list.append(state)
                    results.append(temp_result)
                    false_results.append(false_predict)
                    real_results.append(indx)
                    break
                else:
                    ilosc_wspolnych_pol = porownaj_rekordy(df[df['name'] == odgadniete_imie].iloc[0], losowy)
                    #print("Nie udało się odgadnąć imienia.")
                    #print("Index: "+str(df[df['name'] == odgadniete_imie].index[0]))
                    #print("Wspolne pola:", ilosc_wspolnych_pol)
                    #print(state)
                    state_list.append(state)
                    results.append(temp_result)
                    false_results.append(false_predict)
                    real_results.append(indx)

def make_data_times_restricted(how_many,random,bound):
    for i in range(how_many):
        print(i)
        for indx in df.index:
            checked_indices = []
            print(indx)
            losowy = df.iloc[indx]
            state = [0]*122
            temp_result = [0]*167
            temp_result[losowy.name]=1
            # print(temp_result)
            # print("Losowy rekord został wygenerowany. Spróbuj odgadnąć 'name'.")
            # print(losowy)
            for i in range(bound):
                if random:
                    odgadniete_imie = df.sample().iloc[0]['name']
                    false_predict=df[df['name'] == odgadniete_imie].index[0]
                    while false_predict in checked_indices:
                        odgadniete_imie = df.sample().iloc[0]['name']
                        false_predict=df[df['name'] == odgadniete_imie].index[0]
                    checked_indices.append(false_predict)
                else:
                    model_values = model.predict(np.array(state).reshape(1, -1),verbose=0)
                    while True:
                        if np.argmax(model_values) in checked_indices:
                            model_values[0][np.argmax(model_values)]=0
                        else:
                            checked_indices.append(np.argmax(model_values))
                            break        
                    odgadniete_imie = df.iloc[np.argmax(model_values)]['name']
                    false_predict = np.argmax(model_values)
                    # print(odgadniete_imie)
                #time.sleep(1)
                #print(odgadniete_imie)

                if odgadniete_imie == losowy['name']:
                    # print("Gratulacje! Udało Ci się odgadnąć imię.")
                    state_list.append(state)
                    results.append(temp_result)
                    false_results.append(false_predict)
                    real_results.append(indx)
                    break
                else:
                    ilosc_wspolnych_pol = porownaj_rekordy(df[df['name'] == odgadniete_imie].iloc[0], losowy)
                    #print("Nie udało się odgadnąć imienia.")
                    #print("Index: "+str(df[df['name'] == odgadniete_imie].index[0]))
                    #print("Wspolne pola:", ilosc_wspolnych_pol)
                    #print(state)
                    state_list.append(state)
                    results.append(temp_result)
                    false_results.append(false_predict)
                    real_results.append(indx)

def default_data():
    for index, row in df.iterrows():
        temp_state = 122 * [0]
        result = 167 * [0]
        result[index] = 1
        # print(result)
        temp_state[dict_regions[row['region']]] = 1
        temp_state[dict_gender[row['gender']]] = 1
        temp_state[dict_resource[row['resource']]] = 1
        temp_state[dict_ranged[row['ranged']]] = 1
        temp_state[dict_year[str(row['year'])]] = 1
        temp_state[dict_adaptive[row['adaptive']]] = 1
        temp_state[dict_class[row['class']]] = 1
        state_list.append(temp_state)
        results.append(result)
        false_results.append(index)
        real_results.append(index)
        # print(index, row['name'], temp_state)

def default_data_prob(randomness):
    for index, row in df.iterrows():
        temp_state = 122 * [0]
        result = 167 * [0]
        result[index] = 1
        # print(result)
        if randomness > random.randint(0,10):
            temp_state[dict_regions[row['region']]] = 1
        if randomness > random.randint(0,10):
            temp_state[dict_gender[row['gender']]] = 1
        if randomness > random.randint(0,10):
            temp_state[dict_resource[row['resource']]] = 1
        if randomness > random.randint(0,10):
            temp_state[dict_ranged[row['ranged']]] = 1
        if randomness > random.randint(0,10):
            temp_state[dict_year[str(row['year'])]] = 1
        if randomness > random.randint(0,10):
            temp_state[dict_adaptive[row['adaptive']]] = 1
        if randomness > random.randint(0,10):
            temp_state[dict_class[row['class']]] = 1
        state_list.append(temp_state)
        results.append(result)
        false_results.append(index)
        real_results.append(index)
        # print(index, row['name'], temp_state)

def make_data_times_only_familiar(how_many):
    for i in range(how_many):
        print(i)
        for indx in df.index:
            checked_indices = []
            print(indx)
            losowy = df.iloc[indx]
            state = [0]*122
            temp_result = [0]*167
            temp_result[losowy.name]=1
            # print(temp_result)
            # print("Losowy rekord został wygenerowany. Spróbuj odgadnąć 'name'.")
            # print(losowy)
            imie_info = df.iloc[indx][['region', 'class','year']]
            kraj_imienia = imie_info['region']
            class_df = imie_info['class']
            year_df = imie_info['year']
            result = df[(df['region'] == kraj_imienia) | (df['class'] == class_df) | (df['year'] == year_df)]
            for ind in result.index:
                state = [0]*122
                # if random:
                #     odgadniete_imie = df.sample().iloc[0]['name']
                #     false_predict=df[df['name'] == odgadniete_imie].index[0]
                #     while false_predict in checked_indices:
                #         odgadniete_imie = df.sample().iloc[0]['name']
                #         false_predict=df[df['name'] == odgadniete_imie].index[0]
                #     checked_indices.append(false_predict)
                # else:
                #     model_values = model.predict(np.array(state).reshape(1, -1),verbose=0)
                #     while True:
                #         if np.argmax(model_values) in checked_indices:
                #             model_values[0][np.argmax(model_values)]=0
                #         else:
                #             checked_indices.append(np.argmax(model_values))
                #             break        
                #     odgadniete_imie = df.iloc[np.argmax(model_values)]['name']
                #     false_predict = np.argmax(model_values)
                    # print(odgadniete_imie)
                #time.sleep(1)
                #print(odgadniete_imie)
                odgadniete_imie = df.iloc[ind]['name']

                if odgadniete_imie == losowy['name']:
                    # print("Gratulacje! Udało Ci się odgadnąć imię.")
                    state_list.append(state)
                    results.append(temp_result)
                    false_results.append(indx)
                    real_results.append(indx)
                    break
                else:
                    ilosc_wspolnych_pol = porownaj_rekordy(df[df['name'] == odgadniete_imie].iloc[0], losowy)
                    #print("Nie udało się odgadnąć imienia.")
                    #print("Index: "+str(df[df['name'] == odgadniete_imie].index[0]))
                    #print("Wspolne pola:", ilosc_wspolnych_pol)
                    #print(state)
                    state_list.append(state)
                    results.append(temp_result)
                    false_results.append(indx)
                    real_results.append(indx)

def prepare_conf_matrix():
    y_true = pd.Series(real_results, name="Actual")
    y_pred = pd.Series(false_results, name="Predicted")
    print(y_true)
    print(y_pred)
    df_confusion = pd.crosstab(y_true, y_pred)
    df_confusion.columns = df['name'].tolist()
    df_confusion.index = df['name'].tolist()
    print(df_confusion)
    df_confusion.to_excel("ex.xlsx")

def except_key(słownik, klucz):
    return [wartość for k, wartość in słownik.items() if k != klucz]

def reversed_data_one(index,champ):
        list_inx = except_key(dict_regions_no,champ['region'])
        list_inx.extend(except_key(dict_gender_no,champ['gender']))
        list_inx.extend(except_key(dict_resource_no,champ['resource']))
        list_inx.extend(except_key(dict_ranged_no,champ['ranged']))
        list_inx.extend(except_key(dict_year_no,str(champ['year'])))
        list_inx.extend(except_key(dict_adaptive_no,champ['adaptive']))
        list_inx.extend(except_key(dict_class_no,champ['class']))
        champ_anti_state = [0]*122
        for indx in list_inx:
            champ_anti_state[indx]=1
        return champ_anti_state

def data_one(index,row):
    temp_state = 122 * [0]
    # print(result)
    temp_state[dict_regions[row['region']]] = 1
    temp_state[dict_gender[row['gender']]] = 1
    temp_state[dict_resource[row['resource']]] = 1
    temp_state[dict_ranged[row['ranged']]] = 1
    temp_state[dict_year[str(row['year'])]] = 1
    temp_state[dict_adaptive[row['adaptive']]] = 1
    temp_state[dict_class[row['class']]] = 1
    return temp_state

def mixed_data():
    for index, champ in df.iterrows():
        one_state = data_one(index,champ)
        anti = reversed_data_one(index,champ)
        result = 167 * [0]
        result[index] = 1
        combo_state = 122*[0]
        for i in range(10):
            for i in range(122):
                combo_state[i]=one_state[i]+anti[i]
            ready_state=zero_indexes(combo_state,random.randint(25,35))
            #print(ready_state)    
            state_list.append(ready_state)
            results.append(result)
        

def learn(path_to_save):
    global state_list, results
    print(type(state_list[0]))
    print("Wymiarowość tablicy 1:", len(state_list))
    print("Wymiarowość tablicy 2:", len(results))
    state_list = np.array(state_list)
    results = np.array(results)
    model.fit(state_list,results,epochs=100,batch_size=128)
    model.save('model_v4.keras')


def zero_indexes(lista, ilosc_indeksow):
    niezerowe_indeksy = [i for i, val in enumerate(lista) if val != 0]  # Lista indeksów, które nie są zerami
    indeksy_do_zmiany = random.sample(niezerowe_indeksy, min(ilosc_indeksow, len(niezerowe_indeksy)))
    for indeks in indeksy_do_zmiany:
        lista[indeks] = 0
    return lista
    
def multi_data():
    for key in dict_regions:
        indxs = df.loc[df['region'] == key].index
        temp_result = [0]*167
        for val in indxs:
            temp_result[val]=1
        temp_state = 122*[0]
        temp_state[dict_regions[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)
    for key in dict_gender:
        indxs = df.loc[df['gender'] == key].index
        temp_result = [0]*167
        for val in indxs:
            temp_result[val]=1
        temp_state = 122*[0]
        temp_state[dict_gender[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)
    for key in dict_resource:
        indxs = df.loc[df['resource'] == key].index
        temp_result = [0]*167
        for val in indxs:
            temp_result[val]=1
        temp_state = 122*[0]
        temp_state[dict_resource[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)
    for key in dict_ranged:
        indxs = df.loc[df['ranged'] == key].index
        temp_result = [0]*167
        for val in indxs:
            temp_result[val]=1
        temp_state = 122*[0]
        temp_state[dict_ranged[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)
    for key in dict_year:
        indxs = df.loc[df['year'] == key].index
        temp_result = [0]*167
        for val in indxs:
            temp_result[val]=1
        temp_state = 122*[0]
        temp_state[dict_year[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)
    for key in dict_class:
        indxs = df.loc[df['class'] == key].index
        temp_result = [0]*167
        for val in indxs:
            temp_result[val]=1
        temp_state = 122*[0]
        temp_state[dict_class[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)

def multi_data_false():
    for key in dict_regions:
        indxs = df.loc[df['region'] == key].index
        temp_result = [1]*167
        for val in indxs:
            temp_result[val]=0
        temp_state = 122*[0]
        temp_state[dict_regions_no[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)
    for key in dict_gender:
        indxs = df.loc[df['gender'] == key].index
        temp_result = [1]*167
        for val in indxs:
            temp_result[val]=0
        temp_state = 122*[0]
        temp_state[dict_gender_no[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)
    for key in dict_resource:
        indxs = df.loc[df['resource'] == key].index
        temp_result = [1]*167
        for val in indxs:
            temp_result[val]=0
        temp_state = 122*[0]
        temp_state[dict_resource_no[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)
    for key in dict_ranged:
        indxs = df.loc[df['ranged'] == key].index
        temp_result = [1]*167
        for val in indxs:
            temp_result[val]=0
        temp_state = 122*[0]
        temp_state[dict_ranged_no[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)
    for key in dict_year:
        indxs = df.loc[df['year'] == key].index
        temp_result = [1]*167
        for val in indxs:
            temp_result[val]=0
        temp_state = 122*[0]
        temp_state[dict_year_no[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)
    for key in dict_class:
        indxs = df.loc[df['class'] == key].index
        temp_result = [1]*167
        for val in indxs:
            temp_result[val]=0
        temp_state = 122*[0]
        temp_state[dict_class_no[key]]=1
        state_list.append(temp_state)
        results.append(temp_result)


# multi_data()
# multi_data_false()
#default_data()
# mixed_data()
# for i in range(8,10):
#     default_data_prob(i/10)
# make_data_times(1,False)
# make_data_times(1,True)
# model.summary()
default_data()
learn('model_4_loldle.keras')
# while True:
#     make_data_times(1,False)
#     mixed_data()
#     default_data()
#     default_data_prob(0.5)
#     learn()