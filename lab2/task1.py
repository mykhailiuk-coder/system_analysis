import numpy as np

def get_state(matrix, current_state_arr, states):
    matrix = np.array(matrix)
    probs = matrix @ current_state_arr
    probs = probs / probs.sum()
    new_state_value = np.random.choice(states, p=probs)
    new_state = [0] * len(states)
    new_state[states.index(new_state_value)] = 1
    return new_state

while True:
    task = int(input("Input task: "))
    if task == 1:
        all_states1 = [0, 1, 2, 3, 4, 5]
        current_state1 = [1, 0, 0, 0, 0, 0]
        m1 = [ 
            [0, 1, 0, 0, 0, 0],
            [0.2, 0, 0.8, 0, 0, 0],
            [0, 0.4, 0, 0.6, 0, 0],
            [0, 0, 0.6, 0, 0.4, 0],
            [0, 0, 0, 0.8, 0, 0.2],
            [0, 0, 0, 0, 1, 0]
        ]

        print(f"Initial state: {current_state1}")
        history1 = [current_state1]

        for _ in range(20):
            current_state = get_state(m1, current_state1, all_states1)
            history1.append(current_state1)

        print("Trajectory:")
        print(" ->\n".join(map(str, history1)))
    if task == 2:
        all_states2 = ["Sunny", "Rainy", "Snowy"]
        current_state2 = [1, 0, 0]
        m2 = [
            [0, 0.5, 0.5],
            [0.25, 0.5, 0.25],
            [0.25, 0.25, 0.5]
        ]

        print(f"Initial state: {current_state2}")
        history2 = [current_state2]

        for _ in range(20):
            current_state2 = get_state(m2, current_state2, all_states2)
            history2.append(current_state2)

        print("Trajectory:")
        print(" ->\n".join(map(str, history2)))

    else:
        print("Invalid task number. Please enter 1 to run the simulation.")
