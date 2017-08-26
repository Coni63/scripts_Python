import datetime
import statistics
import tensorflow as tf
import random

min_ = tf.placeholder(tf.float32, [])
max_ = tf.placeholder(tf.float32, [])
avg_ = tf.placeholder(tf.float32, [])
stdev_ = tf.placeholder(tf.float32, [])
score_per_step = tf.placeholder(tf.float32, [])
summary_min = tf.summary.scalar("min", min_)
summary_max = tf.summary.scalar("max", max_)
summary_avg = tf.summary.scalar("avg", avg_)
summary_stdev = tf.summary.scalar("stdev", stdev_)
summary_score_per_step = tf.summary.scalar("score_per_step", score_per_step)

summary_min = tf.Summary()
summary_max = tf.Summary()
summary_avg = tf.Summary()
summary_dev = tf.Summary()
summary_sps = tf.Summary()

# min = tf.Variable(0.0)
# s1 = tf.summary.scalar("min", min)
# max = tf.Variable(0.0)
# s2 = tf.summary.scalar("max", max)
# avg = tf.Variable(0.0)
# tf.summary.scalar("avg", avg)
# dev = tf.Variable(0.0)
# tf.summary.scalar("dev", dev)
# sps = tf.Variable(0.0)
# tf.summary.scalar("sps", sps)

#write_op = tf.summary.merge_all()
#
# now = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
# writer1 = tf.summary.FileWriter("./summary2/min-{}".format(now), tf.get_default_graph())
# writer2 = tf.summary.FileWriter("./summary2/max-{}".format(now), tf.get_default_graph())
# writer3 = tf.summary.FileWriter("./summary2/avg-{}".format(now), tf.get_default_graph())
# writer4 = tf.summary.FileWriter("./summary2/dev-{}".format(now), tf.get_default_graph())
# writer5 = tf.summary.FileWriter("./summary2/sps-{}".format(now), tf.get_default_graph())
#
# with tf.Session() as sess:
#     for iteration in range(100):
#         summary_score = [random.random() for _ in range(10)]
#         summary_step = [random.random() for _ in range(10)]
#         # sess.run(summary_min, feed_dict={min_: min(summary_score)})
#         # sess.run(summary_max, feed_dict={max_: max(summary_score)})
#         # sess.run(summary_avg, feed_dict={avg_: sum(summary_score) / 10})
#         # sess.run(summary_stdev, feed_dict={stdev_: statistics.stdev(summary_score)})
#         # sess.run(summary_score_per_step, feed_dict={score_per_step: sum(summary_score) / sum(summary_step)})
#
#         summary_min.value.add(tag="score", simple_value=min(summary_score))
#         summary_max.value.add(tag="score", simple_value=max(summary_score))
#         summary_avg.value.add(tag="score", simple_value=sum(summary_score) / 10)
#         summary_dev.value.add(tag="dev", simple_value=statistics.stdev(summary_score))
#         summary_sps.value.add(tag="autre", simple_value=sum(summary_score) / sum(summary_step))
#         writer1.add_summary(summary_min, global_step=iteration)
#         writer2.add_summary(summary_max, global_step=iteration)
#         writer3.add_summary(summary_avg, global_step=iteration)
#         writer4.add_summary(summary_dev, global_step=iteration)
#         writer5.add_summary(summary_sps, global_step=iteration)

        # writer1.add_summary(summary_min, iteration)
        # writer2.add_summary(summary_max, iteration)
        # writer3.add_summary(summary_avg, iteration)
        # writer4.add_summary(summary_stdev, iteration)
        # writer5.add_summary(summary_score_per_step, iteration)

        # summary = min.assign(random.random())   #sess.run(write_op, {min: random.random()})
        # writer1.add_summary(s1, iteration)
        # writer1.flush()
        #
        # summary = max.assign(random.random())# sess.run(write_op, {max: random.random()})
        # writer2.add_summary(s2, iteration)
        # writer2.flush()

        # summary = sess.run(write_op, {avg: random.random()})
        # writer3.add_summary(summary, iteration)
        # writer3.flush()
        #
        # summary = sess.run(write_op, {dev: random.random()})
        # writer4.add_summary(summary, iteration)
        # writer4.flush()
        #
        # summary = sess.run(write_op, {sps: random.random()})
        # writer5.add_summary(summary, iteration)
        # writer5.flush()