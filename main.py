import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox

from sklearn.model_selection import train_test_split

import xgboost as xgb
from xgboost import XGBRegressor

def satıs_goruntuleme_islemleri():
    pencere3=tk.Tk()
    pencere3.geometry("1470x700+25+50")
    pencere3.config(bg="#ffc000")
    pencere3.title("Satıs Yonetimi")
    pencere3.resizable(width="FALSE", height="FALSE")

    data=pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
    data=pd.DataFrame(data)
    data = data.drop('seller_type', axis=1)

    frame=tk.Frame(pencere3)
    frame.pack(expand=1)

    tv=ttk.Treeview(frame,columns=(1,2,3,4,5,6,7),show="headings")
    tv.pack()
    tv.heading(1, text="Model")
    tv.heading(2, text="Year")
    tv.heading(3, text="Price")
    tv.heading(4, text="KM-Driven")
    tv.heading(5, text="Fuel")
    tv.heading(6, text="Transmission")
    tv.heading(7, text="Owner")

    df_rows=data.to_numpy().tolist()
    for i in df_rows:
        tv.insert('','end',values=i)



def fiyat_hesaplama_islemleri():
    pencere4=tk.Tk()
    pencere4.geometry("600x600+350+100")
    pencere4.config(bg="#ffc000")
    pencere4.title("Satıs Yonetimi")
    pencere4.resizable(width="FALSE", height="FALSE")


    def dataset_islemler():
        data=pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
        data=pd.DataFrame(data)
        data=data.drop('seller_type', axis=1)
        #data_last=pd.get_dummies(data,columns=['fuel', 'transmission', 'owner'], drop_first=True)
        data['fuel']=(data['fuel'] == "Diesel").astype(int)
        data['transmission'] = (data['transmission'] == "Manual").astype(int)
        data['owner'] = (data['owner'] == "First Owner").astype(int)
        y = data['selling_price']
        X = data.drop('selling_price', axis=1)
        X= X.drop('name',axis=1)
        print(X.head())
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        xgb1 = XGBRegressor(colsample_bytree=0.5, learning_rate=0.09, max_depth=4, n_estimators=2000)
        model_xgb = xgb1.fit(X_train, y_train)
        return  model_xgb

    def fiyat_tahmin():
        yeni_veri=[[int(year_entry.get())],[int(km_driven_entry.get())],[int(fuel_entry.get())],[int(transmission_entry.get())],[int(owner_entry.get())]]
        yeni_veri=pd.DataFrame(yeni_veri).T
        df_2=yeni_veri.rename(columns={
            0:"year",
            1:"km_driven",
            2:"fuel",
            3:"transmission",
            4:"owner",
        })
        model_xgb=dataset_islemler()
        pred=model_xgb.predict(df_2)

        if(pred<0):
            pred= -1*pred
        pred=float(pred)

        lbl_fiyat_tahmin.config(text=pred)

    model_entry=tk.Entry(pencere4)
    model_entry.place(x=250,y=150)
    model_lbl=tk.Label(pencere4,text="Model")
    model_lbl.place(x=165,y=150)


    year_entry = tk.Entry(pencere4)
    year_entry.place(x=250, y=200)
    year_lbl = tk.Label(pencere4, text="Year")
    year_lbl.place(x=165, y=200)

    km_driven_entry = tk.Entry(pencere4)
    km_driven_entry.place(x=250, y=250)
    km_driven_lbl = tk.Label(pencere4, text="KM-Driven")
    km_driven_lbl.place(x=165, y=250)

    fuel_entry = tk.Entry(pencere4)
    fuel_entry.place(x=250, y=300)
    fuel_lbl = tk.Label(pencere4, text="Fuel")
    fuel_lbl.place(x=165, y=300)

    transmission_entry = tk.Entry(pencere4)
    transmission_entry.place(x=250, y=350)
    transmission_lbl = tk.Label(pencere4, text="Transmission")
    transmission_lbl.place(x=165, y=350)

    owner_entry = tk.Entry(pencere4)
    owner_entry.place(x=250, y=400)
    owner_lbl = tk.Label(pencere4, text="Owner")
    owner_lbl.place(x=165, y=400)

    btn_fiyat_hesapla=tk.Button(pencere4,text="Fiyat Tahmini Yap",command=fiyat_tahmin)
    btn_fiyat_hesapla.place(x=260,y=450)

    lbl_fiyat_tahmin=tk.Label(pencere4,text="Fiyat Tahmini")
    lbl_fiyat_tahmin.place(x=270,y=500)

def pencere_show_islemler():
    pencere2=tk.Tk()
    pencere2.geometry("360x300+350+100")
    pencere2.config(bg="#ffc000")
    pencere2.title("Satıs Yonetimi")
    pencere2.resizable(width="FALSE", height="FALSE")

    label_yazi=tk.Label(pencere2,text="Yapılabilecek Islemler")
    label_yazi.place(x=120,y=60)

    btn_satıs_goruntuleme=tk.Button(pencere2,text="Satısları Goruntuleme",command=satıs_goruntuleme_islemleri)
    btn_satıs_goruntuleme.place(x=120,y=100)

    btn_fiyat_hesaplama=tk.Button(pencere2,text="Fiyat Tahmini",command=fiyat_hesaplama_islemleri)
    btn_fiyat_hesaplama.place(x=130,y=140)

def login_check():
    if entry_username.get() == "admin" and entry_parola.get() == "1903":
        messagebox.showinfo("Login Succesfully")
        pencere_show_islemler()
    else:
        messagebox.showinfo("Login Failed")

pencere=tk.Tk()
pencere.geometry("360x300+350+100")
pencere.config(bg="#ffc000")
pencere.title("Satıs Yonetimi")
pencere.resizable(width="FALSE",height="FALSE")

label_username=tk.Label(text="Username")
label_username.place(x=75,y=80)

entry_username=tk.Entry()
entry_username.place(x=150,y=80)

label_parola=tk.Label(text="Password")
label_parola.place(x=75,y=120)

entry_parola=tk.Entry()
entry_parola.place(x=150,y=120)

btn_giris_Yap=tk.Button(text="Giris Yap",command=login_check)
btn_giris_Yap.place(x=160,y=180)

pencere.mainloop()