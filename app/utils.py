# app/utils.py
import pandas as pd

def load_all_data():
    benin = pd.read_csv('data/benin_clean.csv')
    benin["Country"] = "Benin"

    sierra = pd.read_csv('data/sierra_leone_clean.csv')
    sierra["Country"] = "Sierra Leone"

    togo = pd.read_csv('data/togo_clean.csv')
    togo["Country"] = "Togo"

    return pd.concat([benin, sierra, togo], ignore_index=True)
