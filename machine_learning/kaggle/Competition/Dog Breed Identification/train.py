import os
import numpy as np
import pandas as pd
import tensorflow as tf
import scipy

from sklearn.preprocessing import OneHotEncoder, LabelEncoder


def debug_batch():
    a = np.random.random(size=(10,2))
    b = np.random.random(size=(10,1))
    gen = batch_generator(a,b,3,2)
    for x, y in gen:
        print(x, "\n", y)


def batch_generator(X, y, batch_size=50, step=None):
    l = X.shape[0]
    i, loop = 0, 0
    if step is None:
        step = l//batch_size
        if l%batch_size > 0:
            step += 1
        print(step)

    while i < l and loop < step:
        yield X[i:min(i + batch_size, l)], y[i:min(i + batch_size, l)]
        i += batch_size
        loop += 1


def main():
    classes = pd.read_csv("labels.csv")

    img_id = classes["id"].as_matrix().reshape(-1,1)
    breed = classes["breed"]

    LE = LabelEncoder()
    breed = LE.fit_transform(breed).reshape(-1,1)
    # https://stackoverflow.com/questions/42196589/any-way-to-get-mappings-of-a-label-encoder-in-python-pandas

    OHE = OneHotEncoder()
    OHE_breed = OHE.fit_transform(breed)

    batches = batch_generator(img_id, OHE_breed, 10, 5)

    for x, y in batches:
        print(x, "\n", y)




if __name__ == "__main__":
    #main()
    #debug_batch()

