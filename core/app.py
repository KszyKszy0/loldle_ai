import customtkinter
import tensorflow as tf
import pandas as pd
import random
import time
import numpy as np
from difflib import get_close_matches

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class guess(customtkinter.CTkLabel):
    def __init__(self,record,row_val,mast,good,col,newer):
        super().__init__(mast)
        counter = 0
        for val in record:
            self.temp = customtkinter.CTkLabel(master=mast)
            label_txt = str(val)
            if str(val) in good:
                self.temp.configure(text_color="green")
            else:
                self.temp.configure(text_color="red")
                if val == record['year']:
                    if newer:
                        label_txt = "↑"+label_txt+"↑"
                    else:
                        label_txt = "↓"+label_txt+"↓"
            self.temp.configure(text=label_txt)
            self.temp.grid(row=row_val,column=counter+col,padx=20, pady=20)
            counter+=1

class app(customtkinter.CTk):

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

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    df = pd.read_csv('main_6.csv')
    model_path = "mixed_model_0_1.h5"
    model = tf.keras.models.load_model(model_path)
    # model.save("model_v4.keras")

    def __init__(self):
        super().__init__()
        self.geometry("850x500")


        self.name = self.df.sample().iloc[0]['name']
        self.labels_types = []


        #input and button
        self.input = customtkinter.CTkEntry(self, placeholder_text="champ")
        self.input.grid(column=0,row=0,padx=20, pady=20,sticky="w")
        self.current_label_row=3
        self.button = customtkinter.CTkButton(self, text="Guess",command=self.check_champ)
        self.button.grid(row=0,column=1,padx=20, pady=20, sticky="e")
        self.restart_button = customtkinter.CTkButton(self, text="Restart",command=self.restart)
        self.restart_button.grid(row=0,column=2,padx=20, pady=20, sticky="e")

        self.createView()

        print(self.name)
        self.guess_list = []
        self.state_for_ai = [0]*122
        self.checked_indices = []

    def createView(self):
        #frame for answers
        self.main_frame = customtkinter.CTkScrollableFrame(self)
        self.main_frame.grid(row=2,column=0,padx=10,pady=10,columnspan=6,sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.player_frame = customtkinter.CTkFrame(self.main_frame, fg_color="#7CC46A")
        self.player_frame.grid(row=2,column=0,padx=10,pady=10,columnspan=6,sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.ai_frame = customtkinter.CTkFrame(self.main_frame)
        self.ai_frame.grid(row=2,column=10,padx=10,pady=10,columnspan=6,sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.user_label = customtkinter.CTkLabel(self.player_frame, text="Twoje odpowiedzi", font=("Arial", 14, "bold"))
        self.user_label.grid(row=0, column=0, columnspan=len(self.df.columns), pady=(10, 5))

        self.ai_label = customtkinter.CTkLabel(self.ai_frame, text="Odpowiedzi AI", font=("Arial", 14, "bold"))
        self.ai_label.grid(row=0, column=5, columnspan=len(self.df.columns), pady=(10, 5))


        self.bind("<Return>",lambda event: self.check_champ_button(event))
        self.bind("<Tab>",lambda event: self.autoComplete(event))
        counter=0
        for kol in self.df.columns:
            self.temp = customtkinter.CTkLabel(self.player_frame)
            self.temp.configure(text=kol)
            self.temp.grid(row=1,column=counter,padx=(30,20), pady=20)
            counter+=1
            self.labels_types.append(self.temp)

        for kol in self.df.columns:
            self.temp = customtkinter.CTkLabel(self.ai_frame)
            self.temp.configure(text=kol)
            if kol == "name":
                self.temp.grid(row=1,column=counter,padx=(30,20), pady=20)
            else:
                self.temp.grid(row=1,column=counter,padx=20, pady=20)
            counter+=1
            self.labels_types.append(self.temp)

    def autoComplete(self, event):
        user_input = self.input.get()

        if user_input:
            matches = get_close_matches(user_input, self.df["name"].tolist(), n=1, cutoff=0.6)
            if matches:
                self.input.delete(0, "end")
                self.input.insert(0, matches[0])


    def restart(self):
        self.current_label_row=3
        self.state_for_ai = [0]*122
        self.checked_indices = []

        self.main_frame.destroy()

        self.createView()

        self.name = self.df.sample().iloc[0]['name']
        print(self.name)

    def check_champ_button(self,event):
        self.current_label_row+=1
        print("a")
        if not self.input.get() in self.df['name'].values:
            print("brak w bazie")
            return
        if self.name == self.input.get():
            print("Gratulacje! Udało Ci się odgadnąć imię.")
            rec=self.df[self.df['name'] == self.input.get()].iloc[0]
            com = self.porownaj_rekordy(self.df[self.df['name'] == self.name].iloc[0],self.df[self.df['name'] == self.input.get()].iloc[0],False)
            if self.df[self.df['name'] == self.name].iloc[0]['year'] > self.df[self.df['name'] == self.input.get()].iloc[0]['year']:
                is_new = True
            else:
                is_new = False
            new_guess = guess(rec,self.current_label_row,self.player_frame,com,0,is_new)
            self.guess_list.append(new_guess)
        else:
            print("Nie udało się odgadnąć")
            com = self.porownaj_rekordy(self.df[self.df['name'] == self.name].iloc[0],self.df[self.df['name'] == self.input.get()].iloc[0],False)
            print(com)
            if self.df[self.df['name'] == self.name].iloc[0]['year'] > self.df[self.df['name'] == self.input.get()].iloc[0]['year']:
                is_new = True
            else:
                is_new = False
            rec=self.df[self.df['name'] == self.input.get()].iloc[0]
            new_guess = guess(rec,self.current_label_row,self.player_frame,com,0,is_new)
            self.guess_list.append(new_guess)
        temp_rec=self.guess_name(self.model,self.df[self.df['name'] == self.name].iloc[0])
        compare = self.porownaj_rekordy(self.df[self.df['name'] == self.name].iloc[0],temp_rec,False)
        if self.df[self.df['name'] == self.name].iloc[0]['year'] > temp_rec['year']:
            is_new = True
        else:
            is_new = False
        new_guess = guess(temp_rec,self.current_label_row,self.ai_frame,compare,8,is_new)
        self.guess_list.append(new_guess)
        self.input.delete(0,customtkinter.END)

    def check_champ(self):
        self.check_champ_button(self)

    def porownaj_rekordy(self,rekord1, rekord2,ai):
        wspolne_pola = []
        for kolumna in rekord1.index:
            if rekord1[kolumna] == rekord2[kolumna]:
                wspolne_pola.append(str(rekord1[kolumna]))
                if ai:
                    if kolumna == 'region':
                        self.state_for_ai[self.dict_regions[rekord1['region']]] = 1
                    if kolumna == 'gender':
                        self.state_for_ai[self.dict_gender[rekord1['gender']]] = 1
                    if kolumna == 'resource':
                        self.state_for_ai[self.dict_resource[rekord1['resource']]] = 1
                    if kolumna == 'ranged':
                        self.state_for_ai[self.dict_ranged[rekord1['ranged']]] = 1
                    if kolumna == 'year':
                        self.state_for_ai[self.dict_year[str(rekord1['year'])]] = 1
                    if kolumna == 'adaptive':
                        self.state_for_ai[self.dict_adaptive[rekord1['adaptive']]] = 1
                    if kolumna == 'class':
                        self.state_for_ai[self.dict_class[rekord1['class']]] = 1
            else:
                if ai:
                    if kolumna == 'region':
                        self.state_for_ai[self.dict_regions_no[rekord1['region']]] = 1
                    if kolumna == 'gender':
                        self.state_for_ai[self.dict_gender_no[rekord1['gender']]] = 1
                    if kolumna == 'resource':
                        self.state_for_ai[self.dict_resource_no[rekord1['resource']]] = 1
                    if kolumna == 'ranged':
                        self.state_for_ai[self.dict_ranged_no[rekord1['ranged']]] = 1
                    if kolumna == 'year':
                        self.state_for_ai[self.dict_year_no[str(rekord1['year'])]] = 1
                    if kolumna == 'adaptive':
                        self.state_for_ai[self.dict_adaptive_no[rekord1['adaptive']]] = 1
                    if kolumna == 'class':
                        self.state_for_ai[self.dict_class_no[rekord1['class']]] = 1
        return wspolne_pola

    def guess_name(self,model,target):
        model_values = model.predict(np.array(self.state_for_ai).reshape(1, -1),verbose=0)
        while True:
            if np.argmax(model_values) in self.checked_indices:
                model_values[0][np.argmax(model_values)]=0
            else:
                self.checked_indices.append(np.argmax(model_values))
                break
        odgadniete_imie = self.df.iloc[np.argmax(model_values)]['name']
        if odgadniete_imie == target['name']:
            print("Gratulacje! Udało Ci się odgadnąć imię.")
        else:
            ilosc_wspolnych_pol = self.porownaj_rekordy(self.df[self.df['name'] == odgadniete_imie].iloc[0], target,True)
        print(self.state_for_ai)
        return self.df.iloc[np.argmax(model_values)]


main = app()
main.mainloop()


