import random


def play_game():
    j = 0
    while random.choice([0, 1]) == 0:
        j += 1
    return 2**j


def simulate(num_games):
    total_payout = 0
    for _ in range(num_games):
        total_payout += play_game()
    average_payout = total_payout / num_games
    return average_payout


num_games = 100000
average_payout = simulate(num_games)

print(f"Average payout per game over {num_games} simulations: ${average_payout:}")
