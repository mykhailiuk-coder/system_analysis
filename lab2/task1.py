#correct version
import numpy as np

def get_state(matrix, current_state_idx, states):
    matrix = np.array(matrix)
    probs = matrix[current_state_idx]
    probs = probs / probs.sum()
    return np.random.choice(states, p=probs)

m = [
    [0, 1, 0, 0, 0, 0],
    [0.2, 0, 0.8, 0, 0, 0],
    [0, 0.4, 0, 0.6, 0, 0],
    [0, 0, 0.6, 0, 0.4, 0],
    [0, 0, 0, 0.8, 0, 0.2],
    [0, 0, 0, 0, 1, 0]
]

all_states = [0, 1, 2, 3, 4, 5]
current_state = 2  

print(f"Початковий стан: {current_state}")
history = [current_state]

for _ in range(20):
    current_state = get_state(m, current_state, all_states)
    history.append(current_state)

print("Траєкторія:")
print(" -> ".join(map(str, history)))
