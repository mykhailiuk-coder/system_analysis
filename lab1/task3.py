import random

def get_bankruptcy_prob(distribution, fund, n=10):
    x = [] # відшкодування клієнтам
    k = 0 # кількість банкрутств
    for i in range(n):
        # ймовірність відшкодування
        p = random.uniform(0, 1)
        for x_i, p_i in distribution.items():
            if p <= p_i:
                x.append(x_i)
            if sum(x) > fund:
                k += 1
    return k / n

dist = {
    0 : 0.8,
    100_000 : 0.15,
    200_000 : 0.05,
}

fund_money = 100_000
prob = get_bankruptcy_prob(dist, fund_money)
print(f"Bankruptcy probability with {fund_money}$:", prob)
