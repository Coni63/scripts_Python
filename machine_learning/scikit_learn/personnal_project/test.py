import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_sample_images

sample = load_sample_images()
dataset = sample.images
nb_images = len(dataset)
print(nb_images) # => 2

for image in dataset:
    print(image.shape) # retourne 2x (427, 640, 3)

img_1 = dataset[0].astype(np.float32)
print(img_1[:, :, 1])

img_1[:, :, 0:2] = img_1[:, :, 0:2]/255.
print(img_1[:, :, 0])

plt.imshow(img_1[:, :, 1])
plt.show()