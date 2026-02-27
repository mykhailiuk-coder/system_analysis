import numpy as np

def get_state(matrix, current_state_arr, states):
    current_state_idx = current_state_arr.index(1)
    matrix = np.array(matrix)
    probs = matrix @ current_state_arr
    probs = probs / probs.sum()
    new_state_value = np.random.choice(states, p=probs)
    new_state = [0] * len(states)
    new_state[states.index(new_state_value)] = 1
    return new_state

m = [ 
    [0, 1, 0, 0, 0, 0],
    [0.2, 0, 0.8, 0, 0, 0],
    [0, 0.4, 0, 0.6, 0, 0],
    [0, 0, 0.6, 0, 0.4, 0],
    [0, 0, 0, 0.8, 0, 0.2],
    [0, 0, 0, 0, 1, 0]
]

all_states = [0, 1, 2, 3, 4, 5]
current_state = [1, 0, 0, 0, 0, 0]

print(f"Initial state: {current_state}")
history = [current_state]

for _ in range(20):
    current_state = get_state(m, current_state, all_states)
    history.append(current_state)

print("Trajectory:")
print(" ->\n".join(map(str, history)))
