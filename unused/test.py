import numpy as np
import deepmlp as mlp

X = np.array([
[0, 0, 0, 0],
[0, 0, 0, 1],
[0, 0, 1, 0],
[0, 0, 1, 1],
[0, 1, 0, 0],
[0, 1, 0, 1],
[0, 1, 1, 0],
[0, 1, 1, 1],
[1, 0, 0, 0],
[1, 0, 0, 1],
[1, 0, 1, 0],
[1, 0, 1, 1],
[1, 1, 0, 0],
[1, 1, 0, 1],
[1, 1, 1, 0],
[1, 1, 1, 1],
[0, 0, 0, 0],
[0, 0, 0, 1],
[0, 0, 1, 0],
[0, 0, 1, 1],
[0, 1, 0, 0],
[0, 1, 0, 1],
[0, 1, 1, 0],
[0, 1, 1, 1],
[1, 0, 0, 0],
[1, 0, 0, 1],
[1, 0, 1, 0],
[1, 0, 1, 1],
[1, 1, 0, 0],
[1, 1, 0, 1],
[1, 1, 1, 0],
[1, 1, 1, 1],
[0, 0, 0, 0],
[0, 0, 0, 1],
[0, 0, 1, 0],
[0, 0, 1, 1],
[0, 1, 0, 0],
[0, 1, 0, 1],
[0, 1, 1, 0],
[0, 1, 1, 1],
[1, 0, 0, 0],
[1, 0, 0, 1],
[1, 0, 1, 0],
[1, 0, 1, 1],
[1, 1, 0, 0],
[1, 1, 0, 1],
[1, 1, 1, 0],
[1, 1, 1, 1],
[0, 0, 0, 0],
[0, 0, 0, 1],
[0, 0, 1, 0],
[0, 0, 1, 1],
[0, 1, 0, 0],
[0, 1, 0, 1],
[0, 1, 1, 0],
[0, 1, 1, 1],
[1, 0, 0, 0],
[1, 0, 0, 1],
[1, 0, 1, 0],
[1, 0, 1, 1],
[1, 1, 0, 0],
[1, 1, 0, 1],
[1, 1, 1, 0],
[1, 1, 1, 1],
])

l = [4, 10, 10, 4]

net = mlp.DeepMLP(X, X, l, DEBUG=True)
net.train(function="leaky", epochs=100)
net.plot_error()
net.adjacency_matrix()
