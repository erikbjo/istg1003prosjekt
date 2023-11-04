class Correlations():
    def __init__(self, x, y, correlation):
        self.x = x
        self.y = y
        self.correlation = correlation
        
    def printContent(self):
        print(self.x + "\t" + self.y + "\t" + str(self.correlation))
        
def appendToArray(array, correlation_object):
    array.append(correlation_object)



# Dataene nedenfor gir et bedre syn på korrelasjon, ettersom det er tatt på hensyn av varemerke.
# Det er denne dataen som besvarer problemstillingen på best måte.
# Her er det bare tatt med de tre forklaringsvariablene og pris som respons -> pieces, pages and minifigures.

def getRelatedData():
    first = Correlations("Price", "Pieces", value)













# Dataene nedenfor er tatt på hensyn av pris, UAVHENGIG AV VAREMERKE.
# Dette gir derfor et mindre nøyaktig syn på korrelasjon ift. problemstillingen om varemerke påvirker pris...

def getUnrelatedData():
    first = Correlations("Price", "Pieces", 0.8919257699188028)
    second = Correlations("Price", "Pages", 0.7699355782520129)
    third = Correlations("Price", "Minifigures", 0.5734664309339923)
    fourth = Correlations("Price", "Unique Pieces", 0.7462586579160878)

    price_correlation_array = []
    appendToArray(price_correlation_array, first)
    appendToArray(price_correlation_array, second)
    appendToArray(price_correlation_array, third)
    appendToArray(price_correlation_array, fourth)

    fifth = Correlations("Pieces", "Pages", 0.8149298061475578)
    sixth = Correlations("Pieces", "Minifigures", 0.6093736826249477)
    seventh = Correlations("Pieces", "Unique Pieces", 0.7794059771253119)

    pieces_correlation_array = []
    appendToArray(pieces_correlation_array, fifth)
    appendToArray(pieces_correlation_array, sixth)
    appendToArray(pieces_correlation_array, seventh)

    eight = Correlations("Pages", "Minifigures", 0.6087448542968381)
    ninth = Correlations("Pages", "Unique Pieces", 0.7253293261933386)

    pages_correlation_array = []
    appendToArray(pages_correlation_array, eight)
    appendToArray(pages_correlation_array, ninth)

    tenth = Correlations("Minifigures", "Unique Pieces", 0.6891777749152243)

    minifigures_correlation_array = []
    appendToArray(minifigures_correlation_array, tenth)


    # Array containing the different results from correlation.
    # index 0 == price
    # index 1 = pieces
    # index 2 = pages
    # index 3 = minifigures
    result_list = [price_correlation_array, pieces_correlation_array, pages_correlation_array, minifigures_correlation_array]
    for i in range(len(result_list)):
        for item in result_list[i]:
            item.printContent()
        print()