import random

def get_xi(distribution):
    p = random.random()
    sum_pi = 0
    for x_i, p_i in distribution.items():
        sum_pi += p_i
        if p <= sum_pi:
            return x_i
    return None


def get_bankruptcy_prob(distribution, fund, n=10, simulations=100_000):
    bankruptcies = 0

    for _ in range(simulations):
        total = 0
        for _ in range(n):
            total += get_xi(distribution)

        if total > fund:
            bankruptcies += 1

    return bankruptcies / simulations


def find_required_fund(distribution, target_prob=0.05):
    fund = 0
    while True:
        prob = get_bankruptcy_prob(distribution, fund)
        if prob < target_prob:
            return fund, prob
        fund += 50_000


dist = {
    0: 0.8,
    100_000: 0.15,
    200_000: 0.05,
}

fund_money, bank_prob = find_required_fund(dist)

print(f"Required fund: {fund_money}$")
print(f"Estimated bankruptcy probability:", bank_prob)
