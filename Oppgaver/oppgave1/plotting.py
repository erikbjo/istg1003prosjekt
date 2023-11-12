import matplotlib.pyplot as plt
import pandas
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D


original_array = ['Friends', 'City', 'Duplo', 'Speed Champions', 'Hidden Side', 'Classic',
                  'Juniors', 'Creator 3-in-1', 'Ideas', 'Creator Expert', 'Powerd up']
brand_array = ['Disney', 'Unikitty', 'Star Wars', 'Minecraft', 'Marvel',
               'Harry Potter', 'Trolls World Tour', 'DC', 'Monkie Kid']

unclear_array = ['Batman', 'Troll World Tour', 'Powerpuff girls', 'Overwatch', 'Spider-man', 'Minifigur']


def multipleCrossPlot(dataset):
    original_conditions = dataset['Theme'].isin(original_array)
    brand_conditions = dataset['Theme'].isin(brand_array)
    unclear_conditions = dataset['Theme'].isin(unclear_array)
    dataset['cat'] = np.select([original_conditions, brand_conditions, unclear_conditions],
                               ['Original', 'Varemerke', 'Uklart'])
    df_original = dataset[dataset['cat'] == 'Original']
    df_brand = dataset[dataset['cat'] == 'Varemerke']
    df_unclear = dataset[dataset['cat'] == 'Uklart']

    # Perform linear regression for the 'Original' category
    regression_original = LinearRegression().fit(df_original[['Pieces']], df_original['Price'])

    # Perform linear regression for the 'Varemerke' category
    regression_brand = LinearRegression().fit(df_brand[['Pieces']], df_brand['Price'])

    # Perform linear regression for the 'unclear' category
    regression_unclear = LinearRegression().fit(df_unclear[['Pieces']], df_unclear['Price'])

    # Create scatter plots for the three categories
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df_original, x='Pieces', y='Price', label='Original', color='blue')
    sns.scatterplot(data=df_brand, x='Pieces', y='Price', label='Varemerke', color='red')
    sns.scatterplot(data=df_unclear, x='Pieces', y='Price', label='Uklart', color='green')

    # Overlay regression lines for the three categories
    x_values_original = np.linspace(min(df_original['Pieces']), max(df_original['Pieces']), 100)
    y_pred_original = regression_original.predict(x_values_original.reshape(-1, 1))
    plt.plot(x_values_original, y_pred_original, color='blue')

    x_values_brand = np.linspace(min(df_brand['Pieces']), max(df_brand['Pieces']), 100)
    y_pred_brand = regression_brand.predict(x_values_brand.reshape(-1, 1))
    plt.plot(x_values_brand, y_pred_brand, color='red')

    x_values_unclear = np.linspace(min(df_unclear['Pieces']), max(df_unclear['Pieces']), 100)
    y_pred_unclear = regression_unclear.predict(x_values_unclear.reshape(-1, 1))
    plt.plot(x_values_unclear, y_pred_unclear, color='green')

    # Customize  plot
    #plt.xlim(0, 200)
    #plt.ylim(0, 25)
    plt.xlabel('Brikker')
    plt.ylabel('Pris $')
    plt.legend()
    plt.title('Varemerke vs Orginal')
    plt.savefig('oppgave1/plots/multiple_regression')
    plt.clf()

def barDiagram(dataset):

    # Counting occurrences using Counter
    price_count = dataset['Price'].value_counts()
    price_count = price_count.sort_index()

    price_count.plot(kind='bar')
    plt.xlabel('Pris($)')
    plt.ylabel('Antall')
    plt.title('Pris på lego sett')
    plt.savefig('oppgave1/plots/bardiagram')
    plt.clf()

def threeDimentntialPlot(dataset):
    # Extracting X, Y, and Z coordinates
    x = dataset['Pieces'].values.reshape(-1, 1)
    y = dataset['Price'].values.reshape(-1, 1)
    z = dataset['Pages'].values

    # Creating a linear regression model
    model = LinearRegression()
    model.fit(np.hstack((x, y)), z)

    # Generating mesh grid for the plane
    x_grid, y_grid = np.meshgrid(np.linspace(min(x), max(x), 10), np.linspace(min(y), max(y), 10))
    z_plane = model.predict(np.hstack((x_grid.reshape(-1, 1), y_grid.reshape(-1, 1)))).reshape(10, 10)

    # Creating the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot of the data points
    ax.scatter(x, y, z)

    # Plotting the regression plane
    ax.plot_surface(x_grid, y_grid, z_plane, alpha=0.5)

    # Setting labels
    ax.set_xlabel('Brikker')
    ax.set_ylabel('Pris($9')
    ax.set_zlabel('Antall sider')

    plt.savefig('oppgave1/plots/3dReg1')
    ax.view_init(elev=10, azim=30)
    plt.savefig('oppgave1/plots/3dReg2')