# app/utils.py
import pandas as pd

def load_all_data():
    benin = pd.read_csv('data/benin-malanville_clean.csv')
    benin["Country"] = "Benin"

    sierra = pd.read_csv('data/sierraleone-bumbuna_clean.csv')
    sierra["Country"] = "Sierra Leone"

    togo = pd.read_csv('data/togo-dapaong_qc_clean.csv')
    togo["Country"] = "Togo"

    return pd.concat([benin, sierra, togo], ignore_index=True)
