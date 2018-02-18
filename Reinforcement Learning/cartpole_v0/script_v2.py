import datetime
import math
import statistics
import numpy as np
import tensorflow as tf
import gym

from tensorforce.contrib.openai_gym import OpenAIGym
from tensorforce.agents import PPOAgent
from tensorforce.execution import Runner

def episode_finished(r):
    if r.episode % 10 == 0:
        print("Finished episode {ep} after {ts} timesteps".format(ep=r.episode + 1, ts=r.timestep + 1))
        print("Episode reward: {}".format(r.episode_rewards[-1]))
        print("Average of last 10 rewards: {}".format(np.mean(r.episode_rewards[-10:])))
    return True

def reward_calculator(obs):
    max_angle = math.radians(20)
    return (2.4 - abs(obs[0])) + 10*(max_angle - abs(obs[2]))

def is_done(obs):
    max_angle = math.radians(20)
    return abs(obs[0]) > 2 or abs(obs[2]) > max_angle

agent = PPOAgent(
    states_spec=dict(type='float', shape=(4,)),
    actions_spec=dict(type='int', num_actions=2),
    network_spec=[
        dict(type='dense', size=4),
        dict(type='dense', size=4)
    ],
    batch_size=1000,
    step_optimizer=dict(
        type='adam',
        learning_rate=1e-4
    )
)

env = OpenAIGym(
	gym_id="CartPole-v1",
	monitor="/log",
	monitor_video=5,
	visualize=False
)

runner = Runner(
    agent = agent,  # Agent object
    environment = env  # Environment object
)

runner.run(
    episodes = 1000,  # number of episodes to run
	episode_finished = episode_finished
)
runner.close()