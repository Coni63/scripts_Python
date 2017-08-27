import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def leaky_relu(z, alpha=0.01):
    return tf.maximum(alpha*z, z)

def batch(elem, batch_size):
    size = elem.shape[0]
    for i in range(size//batch_size):
        yield elem[:batch_size]
        elem = elem[batch_size:]

def next_batch(X, y, size=50, nb = 50):
    nb_instance, nb_features = X.shape
    p = np.random.permutation(nb_instance)
    X = X[p]
    y = y[p]
    for i in range(nb):
        a = np.random.choice(nb_instance, size)
        yield X[a], y[a]

input_features = 28*28
size_hidden_layer_1 = 300
size_hidden_layer_2 = 100
size_output_layer = 10

# Creation Graph
X = tf.placeholder(tf.float32, shape=(None, input_features), name='X')
y = tf.placeholder(tf.int32, shape=(None), name='y')

# Creation layers
hidden_layer_1 = tf.layers.dense(X, size_hidden_layer_1, name="hidden1", activation=tf.nn.elu)
bn1 = tf.layers.batch_normalization(hidden_layer_1, training=True, momentum=0.9)
bn1_act = tf.nn.elu(bn1)
hidden_layer_2 = tf.layers.dense(bn1_act, size_hidden_layer_2, name="hidden2", activation=tf.nn.elu)
bn2 = tf.layers.batch_normalization(hidden_layer_2, training=True, momentum=0.9)
bn2_act = tf.nn.elu(bn2)
output_layer = tf.layers.dense(bn2_act, size_output_layer, name="output") # pas d'activation

# Cost function
cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=output_layer)
loss= tf.reduce_mean(cross_entropy)

# Backpropagation
LR = 0.01
optimizer = tf.train.MomentumOptimizer(learning_rate=LR, momentum=0.9).minimize(loss)

# evaluation
prediction = tf.argmax(output_layer, 1)
correct = tf.nn.in_top_k(output_layer, y, 1)
accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

# Initialization
init = tf.global_variables_initializer()
saver = tf.train.Saver()

# Tensorborad info
acc_summary = tf.summary.scalar("Accuracy", accuracy)
file_writter = tf.summary.FileWriter("/saves/summary/BN_MO_elu-{}-{}/".format(size_hidden_layer_1, size_hidden_layer_2), tf.get_default_graph())

training_step = False
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
        fig = plt.figure()
        #saver = tf.train.import_meta_graph("/saves/my_model_chapter10.ckpt.meta")
        saver.restore(sess, "/saves/my_model_chapter10_2.ckpt")
        gen_x = batch(mnist.test.images, batch_size)
        gen_y = batch(mnist.test.labels, batch_size)
        for iteration in range(mnist.test.num_examples // batch_size):
            X_batch, y_batch = next(gen_x), next(gen_y)
            guess = correct.eval(feed_dict={X: X_batch, y: y_batch})
            wrong_index = np.argwhere(guess == False)
            for index in wrong_index:
                image_x = X_batch[index]
                label_y = y_batch[index][0]
                predict = prediction.eval(feed_dict={X: image_x})[0]
                # name = "Predict {} vs Label {}".format(predict, label_y)
                # writter.add_summary(vis_summary.eval(feed_dict={img_ph : image_x}))
                plt.imshow(image_x[0].reshape((28, 28)))
                fig.savefig("./result/guess_{}_label_{}_instance_{}.png".format(predict, label_y, iteration*batch_size + index))
                fig.clf()
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