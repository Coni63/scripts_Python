import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
from sklearn.decomposition import PCA

def next_batch(X, y, size=50, nb = 50):
    nb_instance, nb_features = X.shape
    p = np.random.permutation(nb_instance)
    X = X[p]
    y = y[p]
    for i in range(nb):
        a = np.random.choice(nb_instance, size)
        yield X[a], y[a]

input_features = 28*28
size_hidden_layer_1 = 2*28*28
size_hidden_layer_2 = 500
size_output_layer = 10

# Creation Graph
X = tf.placeholder(tf.float32, shape=(None, input_features), name='X')
y = tf.placeholder(tf.int32, shape=(None), name='y')

# Creation layers
hidden_layer_1 = tf.layers.dense(X, size_hidden_layer_1, name="hidden1", activation=tf.nn.relu)
hidden_layer_2 = tf.layers.dense(hidden_layer_1, size_hidden_layer_2, name="hidden2", activation=tf.nn.relu)
output_layer = tf.layers.dense(hidden_layer_2, size_output_layer, name="output") # pas d'activation

# Cost function
cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=output_layer)
loss= tf.reduce_mean(cross_entropy)

# Backpropagation
LR = 0.01
optimizer = tf.train.GradientDescentOptimizer(LR).minimize(loss)

# evaluation
correct = tf.nn.in_top_k(output_layer, y, 1)
accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

# Initialization
init = tf.global_variables_initializer()
saver = tf.train.Saver()

# Tensorborad info
acc_summary = tf.summary.scalar("Accuracy", accuracy)
file_writter = tf.summary.FileWriter("/saves/summary/Original-{}-{}/".format(size_hidden_layer_1, size_hidden_layer_2), tf.get_default_graph())

training_step = True
mnist = input_data.read_data_sets("/data/")
n_epoch = 60
batch_size = 70
training_instances = mnist.train.num_examples
nb_batch = training_instances // batch_size

if input_features < 28*28:
    pca = PCA(n_components=input_features)
    X_train = pca.fit_transform(mnist.train.images)
    X_test = pca.transform(mnist.test.images)
else:
    X_train = mnist.train.images
    X_test = mnist.test.images

with tf.Session() as sess:
    if not training_step:
        #saver = tf.train.import_meta_graph("/saves/my_model_chapter10.ckpt.meta")
        saver.restore(sess, "/saves/my_model_chapter10_2.ckpt")
        print("Model Loaded")
        print(accuracy.eval(feed_dict={X: X_test, y: mnist.test.labels}))
    else:
        init.run()
        for epoch in range(n_epoch):
            for X_batch, y_batch in next_batch(X_train, mnist.train.labels, batch_size, nb_batch):
                sess.run(optimizer, feed_dict={X: X_batch, y: y_batch})
            accuracy_str = acc_summary.eval(feed_dict={X: X_test, y: mnist.test.labels})
            file_writter.add_summary(accuracy_str, epoch)
            print(epoch, accuracy.eval(feed_dict={X: X_test, y: mnist.test.labels}))
        save_path = saver.save(sess, "/saves/my_model_chapter10_2.ckpt")
    file_writter.close()