import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# from sklearn import linear_model
# from sklearn.cross_validation import train_test_split
from sklearn.svm import SVR

# with open("data.csv") as f:
#     f.readline()  # skip the header
#     data = np.loadtxt(fname = f, delimiter = ',')


data = pd.read_csv("data.csv")
#print(data)

data = data.sort_values(by=["X"], ascending=[True])

X = data["X"].values.reshape(-1, 1)
y = data["Ynoised"]
# print(X)
# print(y)

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=3)

y_rbf_raw = svr_rbf.fit(X, y)
y_lin_raw = svr_lin.fit(X, y)
y_poly_raw = svr_poly.fit(X, y)

print(y_rbf_raw)

y_rbf = y_rbf_raw.predict(X)
y_lin = y_lin_raw.predict(X)
y_poly = y_poly_raw.predict(X)

# lw = 2
# plt.scatter(X, y, color='darkorange', label='data')
# plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
# plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
# plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
# plt.xlabel('data')
# plt.ylabel('target')
# plt.title('Support Vector Regression')
# plt.legend()
# plt.show()

t = np.linspace(0, 2*math.pi, 100).reshape(-1,1)
estimation = y_rbf_raw.predict(t)
delta = 5*np.sin(t+(math.pi/4)) - estimation
print(delta)
