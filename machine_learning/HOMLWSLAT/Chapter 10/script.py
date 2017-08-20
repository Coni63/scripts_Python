import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/data/")

input_features = 28*28
size_hidden_layer_1 = 300
size_hidden_layer_2 = 100
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

n_epoch = 40
batch_size = 50
training_instances = mnist.train.num_examples
prec = []
nb_batch = training_instances // batch_size

with tf.Session() as sess:
    init.run()
    for epoch in range(n_epoch):
        for i in range(nb_batch):
            X_batch, y_batch = mnist.train.next_batch(batch_size)
            sess.run(optimizer, feed_dict={X: X_batch, y: y_batch})
        prec.append(accuracy.eval(feed_dict={X: mnist.test.images, y: mnist.test.labels}))

    save_path = saver.save(sess, "/saves/my_model_chapter10.ckpt")

    print(prec)