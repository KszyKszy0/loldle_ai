import pandas as pd

df = pd.read_csv('csv\main_6.csv')

losowy = df.sample().iloc[0]
print(losowy)

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
    'Enhancer': 48,
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
    'Enhancer': 109,
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
# Inicjalizacja pustej tablicy o długości równej liczbie regionów
tablica = [0] * 61

# Ustawienie 1 na odpowiednim indeksie
tablica[dict_regions[losowy['region']]] = 1
tablica[dict_gender[losowy['gender']]] = 1
tablica[dict_resource[losowy['resource']]] = 1
tablica[dict_ranged[losowy['ranged']]] = 1
tablica[dict_year[str(losowy['year'])]] = 1
tablica[dict_adaptive[losowy['adaptive']]] = 1
tablica[dict_class[losowy['class']]] = 1
print(dict_regions[losowy['region']])
print(tablica)