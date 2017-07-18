import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

img = scipy.misc.ascent()#[:10, :10]

# plt.gray()
# plt.imshow(img)
# plt.show()
# img.tofile("lena.txt", sep=" ", format = "%i") # liste les couleurs
# print(img.tolist()) #matrice array
# print(img.tostring()) #string repr

#np.clip(img, 30, 120, out=img) #change les seuils

stdev = np.std(img, axis=0)
mean = np.mean(img, axis=0)
data = np.concatenate((mean, stdev)).reshape(2, img.shape[0])
print(data)