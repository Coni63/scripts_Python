import tensorflow as tf
import numpy as np

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

reconstruction_loss = tf.reduce_mean(tf.square(output-X))

reg_loss = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
loss = tf.add_n([reconstruction_loss]+reg_loss)

optimiser = tf.train.AdamOptimizer(learning_rate=0.01)
training = optimiser.minimize(loss)

rec_loss_summary = tf.summary.scalar("Reconstruction", reconstruction_loss)
loss_summary = tf.summary.scalar("Loss", loss)
file_writter = tf.summary.FileWriter("./saves/summary/modele1/", tf.get_default_graph())

saver = tf.train.Saver()

init = tf.global_variables_initializer()

nb_epoch = 15
batch_size = 150

mnist = input_data.read_data_sets("/data/")

with tf.Session() as sess:
    init.run()
    for epoch in range(nb_epoch):
        nb_batch = mnist.train.num_examples // batch_size
        for iteration in range(nb_batch):
            X_batch, y_batch = mnist.train.next_batch(batch_size)
            sess.run(training, feed_dict={X:X_batch})
            if iteration%10 == 0:
                loss_str = loss_summary.eval(feed_dict={X: mnist.test.images})
                rec_loss_str = rec_loss_summary.eval(feed_dict={X: mnist.test.images})
                file_writter.add_summary(loss_str, epoch)
                file_writter.add_summary(rec_loss_str, epoch)
                saver.save(sess, "./saves/modele1_{}_{}.ckpt".format(epoch, iteration))
