class Correlations():
    def __init__(self, theme, x, y, correlation):
        self.theme = theme
        self.x = x
        self.y = y
        self.correlation = correlation
        
    def printContent(self):
        print(self.theme + "\t" + self.x + "\t" + self.y + "\t" + str(self.correlation))
        
def appendToArray(array, correlation_object):
    array.append(correlation_object)