import numpy as np
import deepmlp as mlp

X = np.array([
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
[0, 0],
[0, 1],
[1, 0],
[1, 1],
])

y = np.array([
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
[0],
[1],
[1],
[0],
])

l = [2, 3, 1]

net = mlp.DeepMLP(X, y, l, DEBUG=True)
net.train(function="leaky", epochs=100, learn_rate=0.1)
net.print_weights()
#net.plot_error()
net.adjacency_matrix()