import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

def get_figure():
  fig = plt.figure(num=0, figsize=(28, 28), dpi=300)
  fig.clf()
  return fig

def batch(elem, batch_size):
    size = elem.shape[0]
    for i in range(size//batch_size):
        yield elem[:batch_size]
        elem = elem[batch_size:]

height = 28
width = 28
channels = 1
n_inputs = height * width
n_outputs = 10

with tf.name_scope("inputs"):
    X = tf.placeholder(tf.float32, shape=[None, n_inputs], name="X")
    X_reshaped = tf.reshape(X, shape=[-1, height, width, channels])
    y = tf.placeholder(tf.int32, shape=[None], name="y")
    training = tf.placeholder_with_default(False, shape=[], name='training')

with tf.name_scope("Conv1"):
    conv1 = tf.layers.conv2d(X_reshaped, filters=32, kernel_size=3, strides=1, padding="SAME", activation=tf.nn.relu)

with tf.name_scope("Conv2"):
    conv2 = tf.layers.conv2d(conv1, filters=64, kernel_size=3, strides=1, padding="SAME", activation=tf.nn.relu)

with tf.name_scope("pool3"):
    pool3 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="VALID")
    pool3_flat = tf.reshape(pool3, shape=[-1, 64 * 14 * 14])
    pool3_flat_drop = tf.layers.dropout(pool3_flat, 0.25, training=training)

with tf.name_scope("fc1"):
    fc1 = tf.layers.dense(pool3_flat_drop, 128, activation=tf.nn.relu)
    fc1_drop = tf.layers.dropout(fc1, 0.5, training=training)

with tf.name_scope("output"):
    logits = tf.layers.dense(fc1, n_outputs)
    Y_proba = tf.nn.softmax(logits)

with tf.name_scope("train"):
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y)
    loss = tf.reduce_mean(cross_entropy)
    optimizer = tf.train.AdamOptimizer()
    training_op = optimizer.minimize(loss)

with tf.name_scope("eval"):
    prediction = tf.argmax(logits, 1)
    correct = tf.nn.in_top_k(logits, y, 1)
    accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

with tf.name_scope("init_and_save"):
    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

with tf.name_scope("images"):
    vis_placeholder = tf.placeholder("uint8", (1, 28, 28, 1))
    img_ph = tf.placeholder(tf.float32, (28*28))
    name_img = tf.placeholder(tf.string)
    image = tf.reshape(img_ph, [-1, 28, 28, 1])
    vis_summary = tf.summary.image("image", image)
    writter = tf.summary.FileWriter("./summary/incorrect", tf.get_default_graph())


mnist = input_data.read_data_sets("/data/")
batch_size = 50

with tf.Session() as sess:
    saver.restore(sess, "./model/my_mnist_model")
    gen_x = batch(mnist.test.images, batch_size)
    gen_y = batch(mnist.test.labels, batch_size)
    for iteration in range(mnist.test.num_examples // batch_size):
        X_batch, y_batch = next(gen_x), next(gen_y)
        guess = correct.eval(feed_dict={ X: X_batch, y: y_batch})
        wrong_index = np.argwhere(guess == False)
        for index in wrong_index:
            image_x = X_batch[index]
            label_y = y_batch[index][0]
            predict = prediction.eval(feed_dict={X: image_x})[0]
            # name = "Predict {} vs Label {}".format(predict, label_y)
            # writter.add_summary(vis_summary.eval(feed_dict={img_ph : image_x}))
            fig = plt.figure()
            plt.imshow(image_x[0].reshape((28,28)))
            fig.savefig(
                "./result/guess_{}_label_{}_instance_{}.png".format(predict, label_y, iteration * batch_size + index))

    acc_test = accuracy.eval(feed_dict={X: mnist.test.images,
                                        y: mnist.test.labels})
    print("Final accuracy on test set:", acc_test)