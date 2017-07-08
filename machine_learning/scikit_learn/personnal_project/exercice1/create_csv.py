import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

sample_size = 50
K_p = 5
K_n = 0.5
phi = math.radians(45)

X_list = np.random.rand(sample_size, 1)*2*math.pi - math.pi

Y_clean = K_p*np.sin(X_list + phi)
noise =  K_n * (np.random.rand(sample_size, 1)-0.5)
Y_noised = Y_clean + noise

###### Showing data ######
# plt.scatter(X_list, Y_clean, c='b', marker="s", label='clean')
# plt.scatter(X_list, Y_noised, c='r', marker="o", label='noised')
# plt.show()

###### 1st methode to create csv ######
dataframe = pd.DataFrame({'X':X_list.T.tolist()[0], 'Yclean':Y_clean.T.tolist()[0], 'noise':noise.T.tolist()[0], 'Ynoised':Y_noised.T.tolist()[0]})
print(dataframe)
dataframe.to_csv("data.csv")

###### 2nd methode to create csv ######
# a = np.concatenate((X_list.T, Y_clean.T, noise.T, Y_noised.T), axis=0)
# np.savetxt("data.csv", a.T, delimiter=",")