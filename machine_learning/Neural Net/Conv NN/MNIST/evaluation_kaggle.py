import tensorflow as tf
import numpy as np
import pandas as pd

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

with tf.name_scope("eval"):
    prediction = tf.argmax(logits, 1)

with tf.name_scope("init_and_save"):
    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

test_set = pd.read_csv("test.csv").as_matrix()
n = test_set.shape[0]
batch_size = 50

result = np.zeros(shape = (n, 2), dtype="int16")
result[:, 0] = np.arange(1,n+1)

i=0
with tf.Session() as sess:
    saver.restore(sess, "./model/my_mnist_model")
    gen_x = batch(test_set, batch_size)
    for iteration in range(n // batch_size):
        X_batch = next(gen_x)
        guess = prediction.eval(feed_dict={X: X_batch})
        result[i:i+batch_size, 1] = guess
        i += batch_size

df = pd.DataFrame(data=result, columns =["ImageId", "Label"])
df.to_csv("result.csv", sep=',', index=False)
#np.savetxt("result.csv", result, delimiter=",")