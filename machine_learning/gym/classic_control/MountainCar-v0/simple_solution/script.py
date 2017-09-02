import gym

env = gym.make("MountainCar-v0")

def evaluate(env):
    x, v = env
    if x > 0:
        if v > 0.001:
            return 2
        else:
            return 0
    if x < 0:
        if v < 0.001:
            return 0
        else:
            return 2

score, step = 0, 0
obs = env.reset()
while True:
    env.render()
    action = evaluate(obs)
    obs, reward, done, info = env.step(action)
    score += reward
    step += 1
    if done:
        break
print("Score : {} in {} steps".format(score, step))