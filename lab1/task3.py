import random

def get_xi(distribution):
    p = random.random()
    sum_pi = 0
    for x_i, p_i in distribution.items():
        sum_pi += p_i
        if p <= sum_pi:
            return x_i

def get_bankruptcy_prob(distribution, fund, n=100_000):
    k = 0
    for _ in range(n):
        sum_xi = 0
        for _ in range(n): 
            sum_xi += get_xi(distribution)
        if sum_xi > fund:
            k += 1
    return k / n

def find_required_fund(distribution, target_prob=0.05):
    fund = 0
    while True:
        prob = get_bankruptcy_prob(distribution, fund)
        if prob < target_prob:
            return fund, prob
        fund += 50_000

dist = {
    0 : 0.8,
    100_000 : 0.15,
    200_000 : 0.05,
}

fund_money, prob = find_required_fund(dist)

print(f"Required fund: {fund_money}$")
print(f"Estimated bankruptcy probability:", prob)
