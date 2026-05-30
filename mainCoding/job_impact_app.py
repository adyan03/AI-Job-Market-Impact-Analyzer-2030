from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = Path(__file__).resolve().parent.parent
PATH_CSV = BASE_DIR/"mainFile"/"AI_Impact_on_Jobs_2030.csv"
PATH_IMG = BASE_DIR/"mainImg"/"aiRisk.png"

df = pd.read_csv(PATH_CSV)

def tampilMenu():
    print("AI Job Market Impact Analyzer 2030")
    print("1. 📊 Ringkasan Dataset")
    print("2. 🚨 Analisis Risiko AI per Industri")
    print("3. 🛡️ Pencari Profesi Paling Aman")
    print("4. 📈 Export Dashboard (Visualisasi Gambar)")
    print("0. Keluar : ")

def Ringkas_Dataset():
    print("="*20)
    top5 = df.head(5)
    print(top5)
    input('\nTekan Enter...')

def Analisis_Risiko():
    print("="*20)
    rata_resiko = df.groupby('Industry').agg({'AI_Replacement_Risk':'mean'}).sort_values(by='AI_Replacement_Risk',ascending=False)
    print(rata_resiko)
    input('\nTekan Enter...')
    
def Pencari_Profesi_Aman():
    print("="*20)
    kriteria_Aman = df[(df['AI_Replacement_Risk'] < 0.3) & (df['Hiring_Trend_2026'] == 'Growing')].sort_values(by='AI_Replacement_Risk',ascending=False)
    print(kriteria_Aman)
    input('\nTekan Enter')

def Visualisasi_Gambar():
    rata_resiko = df.groupby('Industry').agg({'AI_Replacement_Risk':'mean'}).sort_values(by='AI_Replacement_Risk',ascending=False)
    plt.figure(figsize=(10,6))
    plt.bar(rata_resiko.index,rata_resiko['AI_Replacement_Risk'],color = 'blue')
    plt.title("Risiko AI per Industri")
    plt.xlabel("Industry")
    plt.ylabel("Risk Level")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(PATH_IMG)
    plt.show()
    
    

    
while True :
    os.system('cls' if os.name == 'nt' else 'clear')
    tampilMenu()
    try:
        pilih = int(input("Pilih Menu Pilihan   : "))
    except ValueError:
        print("Harap Masukkan angka!")
        input()
        continue
    
    if pilih == 1 :
        Ringkas_Dataset()
    elif pilih == 2 :
        Analisis_Risiko()
    elif pilih == 3:
        Pencari_Profesi_Aman()
    elif pilih == 4:
        Visualisasi_Gambar()
    elif pilih == 0:
        break