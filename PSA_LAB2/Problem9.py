import random


def play_game():
    x = random.uniform(0, 1)
    i = 1

    while True:
        y = random.uniform(0, 1)
        if y > x:
            return i - 1
        i += 1


def simulate(num_trials):
    total_payout = 0

    for _ in range(num_trials):
        total_payout += play_game()

    expected_payout = total_payout / num_trials
    return expected_payout


num_trials = 100000
result = simulate(num_trials)

print(f"Estimated expected payout: {result}")
