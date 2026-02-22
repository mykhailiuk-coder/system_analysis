import random

def get_bankruptcy_prob(dist, fund, n):
    x_i = [] # відшкодування
    k = 0 # кількість банкрутств
    for key, value in dist.items():
        # ймовірність відшкодування
        p_i = random.uniform(0, 1)
        for _ in range(len(dist)):
            if p_i <= value:
                x_i.append(key)
        if sum(x_i) > fund:
            k += 1
    return k / n
