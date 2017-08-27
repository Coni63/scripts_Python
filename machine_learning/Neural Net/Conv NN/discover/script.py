import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.datasets import load_sample_image


china = load_sample_image("china.jpg")
flower = load_sample_image("flower.jpg")

# fig = plt.figure()
# a=fig.add_subplot(1,2,1)
# plt.imshow(china)
# a=fig.add_subplot(1,2,2)
# plt.imshow(flower)
# plt.show()

dataset = np.array([china, flower], dtype=np.float32)
batch_size, height, width, channels = dataset.shape  #(2, 427, 640, 3)

filters = np.zeros(shape=(5, 5, channels, 2), dtype=np.float32)
filters[:, 3, : , 0] = 1
filters[3, :, : , 1] = 1

print(filters)

X = tf.placeholder(tf.float32, shape=(None, height, width, channels))

conv_test = tf.nn.conv2d(X, filters, strides=[1,2,2,1], padding="SAME")
pool_test = tf.nn.max_pool(X, ksize=[1,2,2,1], strides=[1,2,2,1], padding="VALID")

# conv = tf.nn.conv2d(X, filter=[5,5,1,1],  strides=[1,2,2,1], padding="SAME")
# pool = tf.nn.max_pool(conv, ksize=[1,2,2,1], strides=[1,2,2,1], padding="VALID")
# conv2 = tf.nn.conv2d(pool, filter=[5,5,1,1], strides=[1,2,2,1], padding="SAME")
# pool2 = tf.nn.max_pool(conv2, ksize=[1,2,2,1], strides=[1,2,2,1], padding="VALID")
# conv3 = tf.nn.conv2d(pool2, filter=[5,5,1,1], strides=[1,2,2,1], padding="SAME")
# pool3 = tf.nn.max_pool(conv3, ksize=[1,2,2,1], strides=[1,2,2,1], padding="VALID")
# conv4 = tf.nn.conv2d(pool3, filter=[5,5,1,1], strides=[1,2,2,1], padding="SAME")
# pool4 = tf.nn.max_pool(conv4, ksize=[1,2,2,1], strides=[1,2,2,1], padding="VALID")

with tf.Session() as sess:
    output = sess.run(pool_test, feed_dict={X : dataset})

print(output.shape)

# fig = plt.figure()
# a=fig.add_subplot(1,2,1)
# plt.imshow(output[0, :, : , 0], cmap="gray")
# a=fig.add_subplot(1,2,2)
# plt.imshow(output[1, :, : , 0], cmap="gray")
# plt.show()

plt.imshow(output[0].astype(np.uint8))  # plot the output for the 1st image
plt.show()