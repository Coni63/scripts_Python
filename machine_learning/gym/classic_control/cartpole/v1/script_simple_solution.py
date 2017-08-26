import gym

env = gym.make('CartPole-v0')

def simple_solver(obs):
    cart_position, cart_speed, pole_angle, pole_speed = obs
    if pole_angle > 0:
        if pole_speed > 0:
            return 1
        else:
            if pole_angle + pole_speed > 0:
                return 0
            else:
                return 1
    else:
        if pole_speed < 0:
            return 0
        else:
            if pole_angle + pole_speed > 0:
                return 1
            else:
                return 0

score = 0
observation = env.reset()
while True:
    env.render()
    action = simple_solver(observation)
    observation, reward, done, info = env.step(action) # observation = [cart_position, cart speed, pole angle, pole speed]
    print(observation, "\n", reward)
    score += reward
    if abs(observation[0]) > 2 or done:
        break

print("Final Score : ", score)