import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

height = 28
width = 28
channels = 1

n_inputs = height * width
n_hidden1 = 300
n_hidden2 = 100
n_hidden3 = n_hidden1
n_outputs = n_inputs

X = tf.placeholder(tf.float32, shape = [None, n_inputs], name = "X")

he_init = tf.contrib.layers.variance_scaling_initializer()
l2_regularizer = tf.contrib.layers.l2_regularizer(0.001)

hidden1 = tf.layers.dense(X, n_hidden1, activation=tf.nn.elu, kernel_initializer=he_init, kernel_regularizer=l2_regularizer)
hidden2 = tf.layers.dense(hidden1, n_hidden2, activation=tf.nn.elu, kernel_initializer=he_init, kernel_regularizer=l2_regularizer)
hidden3 = tf.layers.dense(hidden2, n_hidden3, activation=tf.nn.elu, kernel_initializer=he_init, kernel_regularizer=l2_regularizer)
output = tf.layers.dense(hidden3, n_outputs, activation=tf.nn.elu, kernel_initializer=he_init, kernel_regularizer=l2_regularizer)

reconstruction_loss = tf.reduce_mean(output-X)

reg_loss = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
loss = tf.add_n([reconstruction_loss]+reg_loss)

optimiser = tf.train.AdamOptimizer(learning_rate=0.01)
training = optimiser.minimize(loss)

rec_loss_summary = tf.summary.scalar("Reconstruction", reconstruction_loss)
loss_summary = tf.summary.scalar("Loss", loss)
file_writter = tf.summary.FileWriter("./saves/summary/modele1/", tf.get_default_graph())

saver = tf.train.Saver()

init = tf.global_variables_initializer()

mnist = input_data.read_data_sets("/data/")
samples = mnist.test.images[155:157]
print(samples.shape)
f, axarr = plt.subplots(2, 2)
with tf.Session() as sess:
    saver.restore(sess, "./saves/modele1_14_360.ckpt")
    reconstruction = output.eval(feed_dict={X : samples})
    print(reconstruction.shape)
    for i in range(2):
        axarr[i, 0].imshow(samples[i].reshape(28,28))
        axarr[i, 1].imshow(reconstruction[i].reshape(28, 28))
    plt.savefig('result.png', bbox_inches='tight')
    #plt.show()
