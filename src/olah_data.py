import pandas as pd

def load_data_kesehatan():
    # Fungsi ini untuk membaca file csv yang ada di folder data
    return pd.read_csv("../data/heart.csv")