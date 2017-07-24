import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self, C, G, Y):
        self.coord = C
        self.guess = G
        self.y_real = Y

    def __repr__(self):
        return "{} => {}".format(self.coord, self.guess)


class Perceptron:
    def __init__(self, size):
        self.learning_rate = 0.01
        self.size = size
        self.weight = [ random.random() for _ in range(self.size) ]

    def __repr__(self):
        return "{}".format([x / min(self.weight) for x in self.weight])

    def train(self, samples):
        for sample in samples:
            guess = self.guess(sample.coord)
            answer = sample.guess
            error = answer - guess
            for i in range(self.size):
                self.weight[i] += error * self.learning_rate * sample.coord[i]
            print(" ")
    def guess(self, point):
        S = sum([self.weight[i] * point[i] for i in range(self.size)])
        if S >= 0:
            output = 1
        else:
            output = -1
        return output

    def calc(self, x):
        return (-self.weight[0]*x - self.weight[2])/self.weight[1]

    def eval(self, samples):
        mistakes = 0
        for sample in samples:
            guess = self.guess(sample.coord)
            answer = sample.guess
            if guess != answer:
                mistakes += 1
        return 100*(1-(mistakes/len(samples)))

    def plot_sample(self, plot, samples):
        g, b = 0, 0
        for sample in samples:
            guess = self.guess(sample.coord)
            answer = sample.guess
            if guess != answer:
                plot.scatter(*sample.coord, color="red", label="wrong guess" if b == 0 else "")
                b += 1
            else:
                plot.scatter(*sample.coord, color="blue", label = "good guess" if g == 0 else "")
                g += 1

        plt.plot([0, 1], [self.calc(0), self.calc(1)], color="orange", label="Perceptron")

        return plot

def create_sample(n):
    sample = []
    for i in range(n):
        x = random.random()
        y = random.random()
        yt = f(x)
        if yt >= y:
            r = 1
        else:
            r = -1
        sample.append(Point([x, y, 1], r, yt))
    return sample

def f(x):
    return 2*x - 0.1

brain = Perceptron(3)
train_sample = create_sample(5000)
test_sample = create_sample(100)

plt.plot([0, 1], [f(0), f(1)], color="green", label="Theory")
plt.xlim(0, 1)
plt.ylim(0, 1)

print("before training : ", brain)
brain.train(train_sample)
print("after training : ", brain)
print("reussite : {:2f} %".format(brain.eval(test_sample)))
plt = brain.plot_sample(plt, test_sample)
plt.legend(loc=2)
plt.show()


