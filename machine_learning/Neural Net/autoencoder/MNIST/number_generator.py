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
n_output_training = 10
n_hidden4 = n_hidden2
n_hidden5 = n_hidden1
n_outputs = n_inputs

X = tf.placeholder(tf.float32, shape = [None, n_inputs], name = "X")
y = tf.placeholder(tf.int32, shape=(None), name='y')
X2 = tf.placeholder(tf.float32, shape=[None, n_output_training])

he_init = tf.contrib.layers.variance_scaling_initializer()
l2_regularizer = tf.contrib.layers.l2_regularizer(0.001)

weights1_init = he_init([n_inputs, n_hidden1])
weights2_init = he_init([n_hidden1, n_hidden2])
weights3_init = he_init([n_hidden2, n_output_training])

weights1 = tf.Variable(weights1_init, dtype=tf.float32, name="weights1")
weights2 = tf.Variable(weights2_init, dtype=tf.float32, name="weights2")
weights3 = tf.Variable(weights3_init, dtype=tf.float32, name="weights3")
weights4 = tf.transpose(weights3, name="weights4")  # tied weights
weights5 = tf.transpose(weights2, name="weights5")  # tied weights
weights6 = tf.transpose(weights1, name="weights6")  # tied weights

biases1 = tf.Variable(tf.zeros(n_hidden1), name="biases1")
biases2 = tf.Variable(tf.zeros(n_hidden2), name="biases2")
biases3 = tf.Variable(tf.zeros(n_output_training), name="biases3")
biases4 = tf.Variable(tf.zeros(n_hidden2), name="biases4")
biases5 = tf.Variable(tf.zeros(n_hidden1), name="biases5")
biases6 = tf.Variable(tf.zeros(n_inputs), name="biases6")

hidden1 = tf.nn.elu(tf.matmul(X, weights1) + biases1)
hidden2 = tf.nn.elu(tf.matmul(hidden1, weights2) + biases2)
output_training = tf.matmul(hidden2, weights3) + biases3  # pas d'activation pour les outputs
input = tf.nn.elu(output_training)
hidden4 = tf.nn.elu(tf.matmul(input, weights4) + biases2)  # X2 or input depending on check of generator
hidden5 = tf.nn.elu(tf.matmul(hidden4, weights5) + biases1)
outputs = tf.nn.elu(tf.matmul(hidden5, weights6))


# # Cost function
# cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=output_training)
# loss= tf.reduce_mean(cross_entropy)
reconstruction_loss = tf.reduce_mean(tf.square(outputs-X))
reg_loss = l2_regularizer(weights1) + l2_regularizer(weights2) + l2_regularizer(weights3)
loss = reconstruction_loss + reg_loss

#Optimisation
optimiser = tf.train.AdamOptimizer(learning_rate=0.01)
training = optimiser.minimize(loss)

# evaluation
prediction = tf.argmax(output_training, 1)
correct = tf.nn.in_top_k(output_training, y, 1)
accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

# softmax
result = tf.nn.softmax(output_training)

saver = tf.train.Saver()

init = tf.global_variables_initializer()

nb_epoch = 50
batch_size = 150

mnist = input_data.read_data_sets("/data/")

stage = "check" # ["training", "generator", "eval", "check"]

with tf.Session() as sess:
    if stage == "training":
        init.run()
        nb_batch = mnist.train.num_examples // batch_size
        for epoch in range(nb_epoch):
            print("epoch {}".format(epoch))
            for iteration in range(nb_batch):
                X_batch, y_batch = mnist.train.next_batch(batch_size)
                sess.run(training, feed_dict={X:X_batch})  #, y:y_batch
                if iteration%10 == 0:
                    saver.save(sess, "./saves/modele3_{}_{}.ckpt".format(epoch, iteration))
    elif stage == "generator":
        samples =   [
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
                    ]

        saver.restore(sess, "./saves/modele3_16_20.ckpt")
        reconstruction = outputs.eval(feed_dict={X2: samples})
        for i in range(10):
            plt.imshow(reconstruction[i].reshape(28, 28))
            plt.savefig('result_model3_{}.png'.format(i), bbox_inches='tight')
        # plt.show()
    elif stage == "eval":
        saver.restore(sess, "./saves/modele3_16_20.ckpt")
        ev = sess.run(result, feed_dict={X: mnist.test.images[:10]})
        print(ev)
        print(mnist.test.labels[:10])
        # acc = sess.run(accuracy, feed_dict={X: mnist.test.images[:10], y: mnist.test.labels[:10]})
        # print(acc)
    elif stage == "check":
        saver.restore(sess, "./saves/modele3_16_20.ckpt")
        reconstruction = outputs.eval(feed_dict={X: mnist.test.images[:10]})
        for i in range(10):
            plt.imshow(reconstruction[i].reshape(28, 28))
            plt.savefig('result_model3_{}_2.png'.format(i), bbox_inches='tight')