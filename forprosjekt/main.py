import pandas as pd
import openpyxl  # needed for read_excel
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excel('skostr_hoyde.xlsx')

slope, intercept, r, p, std_err = stats.linregress(df['skostr'], df['hoyde'])


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, df['skostr']))

plt.scatter(df['skostr'], df['hoyde'])
plt.plot(df['skostr'], mymodel, color='red')
plt.xlabel('Sko størrelse')
plt.ylabel('Høyde')
plt.title('Sko størrelse mot høyde')
plt.legend(['y={:.2f}x+{:.2f}'.format(slope, intercept)])
plt.grid()
plt.savefig('skostr_hoyde.pdf')
plt.show()
