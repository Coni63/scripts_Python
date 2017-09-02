import gym

env = gym.make('Acrobot-v1')

def simple_solver(obs):
    return True

score = 0
observation = env.reset()

while True:
    env.render()
    action = 2 #env.action_space.sample()#simple_solver(observation)
    observation, reward, done, info = env.step(action) # observation = [cart_position, cart speed, pole angle, pole speed]
    print(observation, "\n", reward)
    score += reward
    if done:
        break

print("Final Score : ", score)