import numpy as np
import random

def get_state(matrix, initial_state, states):
    matrix = np.array(matrix)
    initial_state = np.array(initial_state)
    random_value = random.random()
    vector = matrix @ initial_state
    probs = []
    for v in vector:
        if v != 0:
            probs.append(v)
    if random_value < probs[0]:
        prob = probs[0]
        index = np.where(vector == prob)
        return states[index[0][0]]
    else:
        prob = probs[1]
        index = np.where(vector == prob)
        return states[index[0][0]]

m = [
    [0, 1, 0, 0, 0, 0],
    [0.2, 0, 0.8, 0, 0, 0],
    [0, 0.4, 0, 0.6, 0, 0],
    [0, 0, 0.6, 0, 0.4, 0],
    [0, 0, 0, 0.8, 0, 0.2],
    [0, 0, 0, 0, 1, 0]
    ]

all_states = [0, 1, 2, 3, 4, 5]
state0 = [0, 1, 0, 0, 0, 0]

for _ in range(20):
    print(get_state(m, state0, all_states), end=' ')
