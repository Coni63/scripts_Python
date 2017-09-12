# On importe les librairies dont on aura besoin pour ce tp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.cross_validation import train_test_split

url = r'F:\Nicolas\PycharmProjects\machine learning\openclassroom\exercice 1\house.csv'

# On charge le dataset
with open(url) as f:
    f.readline()  # skip the header
    house_data = np.loadtxt(fname = f, delimiter = ',')

data_size = len(house_data)

# Passage sur un sample au lieu du full dataset
sample = np.random.randint(data_size, size=data_size//10)
print(sample)
sampled_data = house_data[sample]
sample_size = len(sampled_data)

surface = sampled_data[:,1].reshape((sample_size, 1))
loyer = sampled_data[:,0].reshape((sample_size, 1))

# split 80% trainsing et 20% validation
# surface = house_data[:,1].reshape((data_size, 1))
# loyer = house_data[:,0].reshape((data_size, 1))
# xtrain, xtest, ytrain, ytest = train_test_split(surface, loyer, train_size=0.8)

# print(surface)
# print(loyer)

"""
house_data = pd.read_csv(url)

# On décompose le dataset et on le transforme en matrices pour pouvoir effectuer notre calcul
X = np.matrix([ np.ones(house_data.shape[0]), house_data["surface"] ]).T
y = np.matrix(house_data["loyer"]).T

#print(X)
#print(y)

# On effectue le calcul exact du paramètre theta
theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

print(theta)
"""

regr = linear_model.LinearRegression()

a = regr.fit(surface, loyer)
score = regr.score(surface, loyer)
#print(a.coef_, a.intercept_, score)
# regr.predict(donnee_test)

print("Eq : loyer = {} * Surface + {}".format(a.coef_[0][0], a.intercept_[0]))
print("r^2 = {}".format(score))

plt.xlabel('Surface')
plt.ylabel('Loyer')

plt.plot(surface, loyer, 'ro', markersize=2)
plt.plot([0,250], [a.intercept_, a.intercept_ + 250 * a.coef_], linestyle='--', c='#000000')

plt.show()
