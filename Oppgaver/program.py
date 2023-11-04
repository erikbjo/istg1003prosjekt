import computations
import correlations
import pandas as pd

def getDataFrame(path):
    df = pd.read_csv(path, sep = ",", encoding = "latin1")

    df_actual = df[["Theme", "Price", "Pieces", "Pages", "Minifigures"]]
    df_actual = df_actual.dropna()

    df_actual["Theme"] = df_actual["Theme"].astype(str)
    df_actual["Theme"] = df_actual["Theme"].str.replace(r'[^a-zA-Z0-9\s-]', '', regex = True)

    df_actual["Price"] = df_actual["Price"].str.replace('\$', '', regex = True)
    df_actual["Price"] = df_actual["Price"].astype(float)
    
    return df_actual

def getSelectionDataFrame(dataframe, selector):
    return dataframe[dataframe["Theme"] == selector]

def printContentInDataFrame(dataframe):
    print(dataframe)

def main():
    path = "./Oppgaver/data/lego.population.csv"
    df = getDataFrame(path)
    
    selector = "Star Wars"
    work_df = getSelectionDataFrame(df, selector)
    
    printContentInDataFrame(work_df)
    
    correlation_a = computations.getCorrelationRelatedToElement(work_df, "Minifigures")
    print(correlation_a)

main()