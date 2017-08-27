import datetime
import math
import statistics
import numpy as np
import tensorflow as tf
import gym

def reward_calculator(obs):
    max_angle = math.radians(20)
    return (2.4 - abs(obs[0])) + 10*(max_angle - abs(obs[2]))

def is_done(obs):
    max_angle = math.radians(20)
    return abs(obs[0]) > 2 or abs(obs[2]) > max_angle

# Compute discounted reward
def discount_rewards(rewards, discount_rate):
    discounted_rewards = np.zeros(len(rewards))
    cumulative_rewards = 0
    for step in reversed(range(len(rewards))):
        cumulative_rewards = rewards[step] + cumulative_rewards * discount_rate
        discounted_rewards[step] = cumulative_rewards
    return discounted_rewards

def discount_and_normalize_rewards(all_rewards, discount_rate):
    all_discounted_rewards = [discount_rewards(rewards, discount_rate) for rewards in all_rewards]
    flat_rewards = np.concatenate(all_discounted_rewards)
    reward_mean = flat_rewards.mean()
    reward_std = flat_rewards.std()
    return [(discounted_rewards - reward_mean)/reward_std for discounted_rewards in all_discounted_rewards]


# Create Model
tf.reset_default_graph()
tf.set_random_seed(42)
np.random.seed(42)

# topology
n_inputs = 4
n_hidden = 4
n_outputs = 1

initializer = tf.contrib.layers.variance_scaling_initializer()

X = tf.placeholder(tf.float32, shape=[None, n_inputs])

hidden = tf.layers.dense(X, n_hidden, activation=tf.nn.elu, kernel_initializer=initializer)
logits = tf.layers.dense(hidden, n_outputs)
outputs = tf.nn.sigmoid(logits)

p_left_and_right = tf.concat(axis=1, values=[outputs, 1 - outputs])
action = tf.multinomial(tf.log(p_left_and_right), num_samples=1)

y = 1. - tf.to_float(action)
cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=logits)
optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
#optimizer = tf.train.MomentumOptimizer(learning_rate=0.01, momentum=0.9, use_nesterov=True)

grads_and_vars = optimizer.compute_gradients(cross_entropy)
gradients = [grad for grad, variable in grads_and_vars]
gradient_placeholders = []
grads_and_vars_feed = []
for grad, variable in grads_and_vars:
    gradient_placeholder = tf.placeholder(tf.float32, shape=grad.get_shape())
    gradient_placeholders.append(gradient_placeholder)
    grads_and_vars_feed.append((gradient_placeholder, variable))
training_op = optimizer.apply_gradients(grads_and_vars_feed)

init = tf.global_variables_initializer()
saver = tf.train.Saver()

# summary_min = tf.Summary()
# summary_max = tf.Summary()
# summary_avg = tf.Summary()
# summary_dev = tf.Summary()
# summary_sps = tf.Summary()

# now = 2 #datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
# writer1 = tf.summary.FileWriter("./summary-{}/min3".format(now), tf.get_default_graph())
# writer2 = tf.summary.FileWriter("./summary-{}/max3".format(now), tf.get_default_graph())
# writer3 = tf.summary.FileWriter("./summary-{}/avg3".format(now), tf.get_default_graph())
# writer4 = tf.summary.FileWriter("./summary-{}/dev3".format(now), tf.get_default_graph())
# writer5 = tf.summary.FileWriter("./summary-{}/sps3".format(now), tf.get_default_graph())

env = gym.make("CartPole-v1")
n_games_per_update = 10
n_max_steps = 1000
n_iterations = 1000
n_test = 10
save_iterations = 10
discount_rate = 0.95
training = False

with tf.Session() as sess:
    if training:
        init.run()
        for iteration in range(n_iterations + 1):
            print("\rIteration: {}".format(iteration), end="")
            all_rewards = []
            all_gradients = []
            for game in range(n_games_per_update):
                current_rewards = []
                current_gradients = []
                obs = env.reset()
                for step in range(n_max_steps):
                    action_val, gradients_val = sess.run([action, gradients], feed_dict={X: obs.reshape(1, n_inputs)})
                    obs, reward, done, info = env.step(action_val[0][0])
                    reward = reward_calculator(obs)
                    current_rewards.append(reward)
                    current_gradients.append(gradients_val)
                    if is_done(obs) or done:
                        break
                all_rewards.append(current_rewards)
                all_gradients.append(current_gradients)

            all_rewards = discount_and_normalize_rewards(all_rewards, discount_rate=discount_rate)
            feed_dict = {}
            for var_index, gradient_placeholder in enumerate(gradient_placeholders):
                mean_gradients = np.mean([reward * all_gradients[game_index][step][var_index]
                                          for game_index, rewards in enumerate(all_rewards)
                                              for step, reward in enumerate(rewards)], axis=0)
                feed_dict[gradient_placeholder] = mean_gradients
            sess.run(training_op, feed_dict=feed_dict)
            if iteration % save_iterations == 0:
                saver.save(sess, "./saves/model_AdamOp_{}.ckpt".format(iteration))
                # summary_score = []
                # summary_step = []
                # for _ in range(n_test):
                #     score = 0
                #     step = 0
                #     obs = env.reset()
                #     while True:
                #         act = action.eval(feed_dict={X: obs.reshape(1, n_inputs)})
                #         obs, reward, done, info = env.step(act[0][0])
                #         score += reward_calculator(obs)
                #         step += 1
                #         if is_done(obs) or done:
                #             break
                #     summary_score.append(score)
                #     summary_step.append(step)
                # summary_min.value.add(tag="score", simple_value=min(summary_score))
                # summary_max.value.add(tag="score", simple_value=max(summary_score))
                # summary_avg.value.add(tag="score", simple_value=sum(summary_score) / n_test)
                # summary_dev.value.add(tag="dev", simple_value=statistics.stdev(summary_score))
                # summary_sps.value.add(tag="autre", simple_value=sum(summary_score) / sum(summary_step))
                # writer1.add_summary(summary_min, global_step=iteration)
                # writer2.add_summary(summary_max, global_step=iteration)
                # writer3.add_summary(summary_avg, global_step=iteration)
                # writer4.add_summary(summary_dev, global_step=iteration)
                # writer5.add_summary(summary_sps, global_step=iteration)
    else:
        saver.restore(sess, "./saves/model_AdamOp_1000.ckpt")
        for i in range(1):
            score = 0
            step = 0
            obs = env.reset()
            while True:
                env.render()
                act = action.eval(feed_dict={X : obs.reshape(1, n_inputs)})
                obs, reward, done, info = env.step(act[0][0])
                score += reward_calculator(obs)
                step += 1
                if is_done(obs) or done:
                    break
            print("Score : {} in {} steps".format(score, step))