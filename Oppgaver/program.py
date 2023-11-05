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

def getThemes(dataframe):
    themes = []
    for theme in dataframe["Theme"]:
        if theme not in themes:
            themes.append(theme)
    return themes

def getFromSelector(selector):
    path = "./Oppgaver/data/lego.population.csv"
    df = getDataFrame(path)
    
    work_df = getSelectionDataFrame(df, selector)
    
    
    correlation_pieces = computations.getCorrelationRelatedToElement(work_df, "Pieces")
    correlation_pages = computations.getCorrelationRelatedToElement(work_df, "Pages")
    correlation_minifigures = computations.getCorrelationRelatedToElement(work_df, "Minifigures")
    #correlation_unique_pieces = computations.getCorrelationRelatedToElement(work_df, "Unique_Pieces")
    
    pieces = correlations.Correlations(selector, "Pieces", "Price", correlation_pieces)
    pages = correlations.Correlations(selector, "Pages", "Price", correlation_pages)
    minifigures = correlations.Correlations(selector, "Minifigures", "Price", correlation_minifigures)
    #unique_pieces = correlations.Correlations(selector, "Unique_Pieces", "Price", correlation_unique_pieces)
    
    
    correlations_array = []
    correlations.appendToArray(correlations_array, pieces)
    correlations.appendToArray(correlations_array, pages)
    correlations.appendToArray(correlations_array, minifigures)
    #correlations.appendToArray(correlations_array, unique_pieces)
    
    return correlations_array

def main():
    
    path = "./Oppgaver/data/lego.population.csv"
    df = getDataFrame(path)
    themes = getThemes(df)
    
    correlations_array = []
    for theme in themes:
        correlations_array.append(getFromSelector(theme))
    
    for i in range(len(correlations_array)):
        for item in correlations_array[i]:
            item.printContent()
        print()
    


main()