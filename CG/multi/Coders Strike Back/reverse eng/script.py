import matplotlib.pyplot as plt
import math
import numpy as np
from sklearn import linear_model

""" Determination des Fonction de transfert en fonction de P """

# data_10 = [0, 8, 15, 21, 26, 30, 34, 37, 39, 41, 43, 45, 46, 47, 48, 49, 50, 51]
# data_20 = [0, 17, 31, 43, 53, 62, 69, 75, 80, 85, 89, 92, 95, 97, 99, 101, 102, 103, 104, 105, 106, 107]
# data_30 = [0, 25, 46, 64, 79, 92, 103, 113, 121, 128, 134, 139, 143, 147, 150, 153, 155, 157, 158, 159, 160, 161, 162, 163, 164]
# data_40 = [0, 34, 62, 86, 107, 124, 139, 152, 163, 172, 180, 187, 192, 197, 201, 204, 207, 209, 211, 213, 215, 216, 217, 218, 219, 220, 221]
# data_50 = [277]
# data_60 = [334]
# data_70 = [0, 59, 109, 152, 188, 219, 245, 267, 286, 302, 316, 328, 338, 346, 353, 359, 364, 368, 372, 375, 378, 380, 382, 384, 385, 386, 387, 388, 389, 390, 391]
# data_80 = [447]
# data_90 = [504]
# data_100 = [0, 85, 157, 218, 270, 314, 351, 383, 410, 433, 453, 470, 484, 496, 506, 515, 522, 528, 533, 538, 542, 545, 548, 550, 552, 554, 555, 556, 557, 558, 559, 560, 561]

# data = [data_10, data_20, data_30, data_40, data_50, data_60, data_70, data_80, data_90, data_100]

# K = {}
# Tau = {}

# for i in range(10):
#     K[i] = data[i][-1]
#     if len(data[i]) > 1:
#         plt.plot(data[i])
#         min_delta = 1e6
#         for tau10 in range(50, 70):
#             tau = tau10/10
#             v = []
#             delta = []
#             for j in range(len(data[i])):
#                 vitesse = int(K[i]*(1-math.exp(-j/tau)))
#                 v.append(vitesse)
#                 delta.append( data[i][j]- vitesse )
#             if abs(sum(delta)) < min_delta:
#                 min_delta = abs(sum(delta))
#                 Tau[i] = tau
#         print(min_delta)

# print(Tau)
# print(K)
# plt.show()

""" Estimation de la relation entre T et Power """

# x = [0, 1, 2, 3, 4, 7, 10]
# y = [4.6, 5.1, 5.5, 5.7, 5.8, 6.0, 6.0]
# y_offset = [x-y[0] for x in y]
# print(y_offset)
# y_test = [1.4*(1-math.exp(-t/2)) for t in x]
# print(y_test)
# plt.scatter(x,y)
# plt.show()

#On peut considerer que T = 4.6 + 1.4 * (1-math.exp(t/2))

""" Estimation de K en fonction de Power """

# x = np.array(list(range(1, 11))).reshape(-1, 1)
# y = np.array([51, 107, 164, 221, 277, 334, 391, 447, 504, 561]).reshape(-1, 1)

# regr = linear_model.LinearRegression()

# a = regr.fit(x, y)
# score = regr.score(x, y)
# print(a.coef_, a.intercept_, score)

# plt.scatter(x,y)
# plt.show()

# K = 56.66 * Power - 6