import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

from sklearn import linear_model
from sklearn.model_selection import train_test_split

# getting cvs at the same path as the script
directory = os.path.dirname(__file__)
csv_path = os.path.join(directory, 'house_data.csv')

# Reading info from file
house_data = pd.read_csv(csv_path)

# Filtering NaN datas
house_data = house_data.dropna()

datas = [house_data[house_data['arrondissement'] == i] for i in range(1, 10)]
datas = [x for x in datas if len(x) > 1]
#print(datas)

f, axarr = plt.subplots(4, 3)

i = -1
for subset in datas:
    i += 1
    X, Y = subset['surface'].values.reshape(-1, 1), subset['price'].values.reshape(-1, 1)
    axarr[i, 0].scatter(X, Y)
    axarr[i, 0].set_title('Subset {} - Aucun filtrage'.format(i+1))
    regr = linear_model.LinearRegression()
    a = regr.fit(X, Y)
    score = regr.score(X, Y)
    axarr[i, 0].plot([0,250], [a.intercept_, a.intercept_ + 250 * a.coef_], linestyle='--', c='#000000')
    print(len(subset), a.coef_, a.intercept_, score)

    # Let's remove outliers
    subset = subset.assign(delta = subset['price'] - (a.coef_[0][0] * subset['surface'] + a.intercept_[0]))
    subset = subset[np.abs(subset['delta']-subset['delta'].mean())<=(3*subset['delta'].std())]

    X, Y = subset['surface'].values.reshape(-1, 1), subset['price'].values.reshape(-1, 1)
    axarr[i, 1].scatter(X, Y)
    axarr[i, 1].set_title('Subset {} - 1 seul filtrage'.format(i+1))
    regr = linear_model.LinearRegression()
    a = regr.fit(X, Y)
    score = regr.score(X, Y)
    axarr[i, 1].plot([0,250], [a.intercept_, a.intercept_ + 250 * a.coef_], linestyle='--', c='#000000')
    print(len(subset), a.coef_, a.intercept_, score)

    # Let's remove outliers with the new regression
    subset = subset.assign(delta2 = subset['price'] - (a.coef_[0][0] * subset['surface'] + a.intercept_[0]))
    subset = subset[np.abs(subset['delta2']-subset['delta2'].mean())<=(3*subset['delta2'].std())]

    X, Y = subset['surface'].values.reshape(-1, 1), subset['price'].values.reshape(-1, 1)
    axarr[i, 2].scatter(X, Y)
    axarr[i, 2].set_title('Subset {} - 2 filtrages'.format(i+1))
    regr = linear_model.LinearRegression()
    a = regr.fit(X, Y)
    score = regr.score(X, Y)
    axarr[i, 2].plot([0,250], [a.intercept_, a.intercept_ + 250 * a.coef_], linestyle='--', c='#000000')
    print(len(subset), a.coef_, a.intercept_, score)

#plt.legend(loc="upper left", bbox_to_anchor=(1,1)) # Legend is outside the plot
plt.show()