import pandas as pd

path = "oppgave1/data/lego.population.csv"

def getDataFrame():
    df = pd.read_csv(path, sep=",", encoding="latin1")

    df_actual = df[["Set_Name", "Theme", "Price", "Pieces", "Pages", "Minifigures", "Unique_Pieces"]]
    df_actual = df_actual.dropna()

    df_actual["Theme"] = df_actual["Theme"].astype(str)
    df_actual["Theme"] = df_actual["Theme"].str.replace(r'[^a-zA-Z0-9\s-]', '', regex=True)

    df_actual["Price"] = df_actual["Price"].str.replace('\$', '', regex=True)
    df_actual["Price"] = df_actual["Price"].astype(float)

    return df_actual
