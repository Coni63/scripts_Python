import gym

env = gym.make('Pendulum-v0')

def simple_solver(obs):
    pendulum_angle, pendulum_speed, pendulum_acc = obs
    print(obs)
    if pendulum_angle > 0:
        return [2]
    else:
        return [-2]


score = 0
observation = env.reset()
while True:
    env.render()
    action = simple_solver(observation)
    observation, reward, done, info = env.step(action) # observation = [cart_position, cart speed, pole angle, pole speed]
    score += reward
    if done:
        break

print("Final Score : ", score)