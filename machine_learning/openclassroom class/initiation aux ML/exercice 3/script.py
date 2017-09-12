# On importe les librairies dont on aura besoin pour ce tp
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

#cleaning line with NaN (not required in that exqmple for 'arrondissement')
house_data = house_data[np.isfinite(house_data['surface'])]
house_data = house_data[np.isfinite(house_data['arrondissement'])]

data_size = len(house_data)

# Display price per m^2 depending on boroughs
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(xtrain, ztrain, ytrain)
# plt.show()
# we can see than the price is still linear with surface for every borough but the slope and interp should change for all of them

# Split sample for training (80%) and test (80%)
train, test = train_test_split(house_data, test_size = 0.8)
#print(train)

ytrain, Xtrain =  train['price'], train.loc[:,'surface':'arrondissement']
regr = linear_model.LinearRegression()
a = regr.fit(Xtrain, ytrain)
score = regr.score(Xtrain, ytrain)
#print(a.coef_[0], a.coef_[1], a.intercept_, score)
print("Eq : loyer = {:.2f} * Surface + {:.2f} * Arrondissement + {:.2f}".format(a.coef_[0], a.coef_[1], a.intercept_))

# only for manual test
# t = np.array([[70, 4], [70, 5]]) 
# print(regr.predict(t))

ytest, Xtest =  test['price'], test.loc[:,'surface':'arrondissement']
#print(X)

prediction = regr.predict(Xtest)
score = regr.score(prediction, ytest)
print(score)

# print("Eq : loyer = {} * Surface + {}".format(a.coef_[0][0], a.intercept_[0]))
# print("r^2 = {}".format(score))

# plt.xlabel('Surface')
# plt.ylabel('Loyer')

# plt.plot(surface, loyer, 'ro', markersize=2)
# plt.plot([0,250], [a.intercept_, a.intercept_ + 250 * a.coef_], linestyle='--', c='#000000')

# plt.show()
# """