import tensorflow as tf

nb_cities = 50
dimensions = 2

path = tf._placeholder(tf.int32, shape=[None, nb_cities], name="path")
cities = tf._placeholder(tf.int32, shape=[nb_cities, dimensions], name="cities")

distance = tf.multiply(path, cities)
rank = tf.nn.softmax(distance, name="fitness")

selection = tf.multinomial(tf.log(rank), nb_cities//2)

#distance = tf._placeholder(tf.int32, shape=[None], name="path")


