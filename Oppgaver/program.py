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
    
    # Bare disse temaene har et antall varer som gir et bilde på korrelasjon.
    # De som ikke har et tilfreds antall varer er derfor fjernet.
    
    lego_array = ["Friends", "City", "Speed Champions", "Hidden Side", "Classic",
                  "Juniors", "Creator 3-in-1", "Ideas", "Creator Expert"]
    
    trademark_array = ["Disney", "Unikitty", "Star Wars", "Minecraft", "Marvel",
                       "Harry Potter", "Trolls World Tour", "DC", "Monkie Kid"]
    
    
    
    lego_correlations = []
    for theme in lego_array:
        lego_correlations.append(getFromSelector(theme))
    
    trademark_correlations = []
    for theme in trademark_array:
        trademark_correlations.append(getFromSelector(theme))
    
    for item in lego_correlations:
        for cor in item:
            cor.printContent()
        print()
    
    print("\n\n\n")
    
    for item in trademark_correlations:
        for cor in item:
            cor.printContent()
        print()
    
    print("Total number of items counted: 522")


main()