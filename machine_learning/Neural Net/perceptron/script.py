import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, size):
        self.learning_rate = 0.025
        self.size = size
        self.weight = np.random.rand(3)

    def __repr__(self):
        return "{}".format(self.weight)

    def fit(self, samples, target):
        for i in range(len(samples)):
            guess = np.sign(np.sum(self.weight * samples[i]))
            error = target[i] - guess
            self.weight += error * self.learning_rate * samples[i]

    def guess(self, list_point, target):
        accuracy = 0
        for i in range(len(list_point)):
            guess = np.sign(np.sum(self.weight * list_point[i]))
            if guess == target[i]:
                accuracy += 1
        return accuracy/len(list_point)

    def evaluate(self, X):
        return -(self.weight[1]*X + self.weight[0])/self.weight[2]


def f(x):
    return 2*x-0.1

brain = Perceptron(3)

#training set
n = 5000
bias = np.ones(n)
X = np.random.rand(n)
Y = np.random.rand(n)
C = np.sign(Y-f(X))

brain.fit(np.c_[bias, X, Y], C)

# test set
n = 500
bias = np.ones(n)
X = np.random.rand(n)
Y = np.random.rand(n)
C = np.sign(Y-f(X))

acc = brain.guess(np.c_[bias, X, Y], C)

print("accuracy {:.2f} %".format(acc*100))

plt.plot([0, 1], [brain.evaluate(0), brain.evaluate(1)], color="red", label="Guess")
plt.plot([0, 1], [f(0), f(1)], color="green", label="Theory")
plt.scatter(X, Y, c=C )
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.legend(loc="upper right")
plt.text(0.05, 0.92, "accuracy {:.2f} %".format(acc*100), bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
plt.show()


