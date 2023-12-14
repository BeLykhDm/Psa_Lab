import matplotlib.pyplot as plt
import random
from collections import Counter


def simulate_coin_toss(num_tosses):
    return [random.choice(["H", "T"]) for _ in range(num_tosses)]


def count_heads(toss_results):
    return toss_results.count("H")


def run_experiment(num_experiments, num_tosses):
    results = [
        count_heads(simulate_coin_toss(num_tosses)) for _ in range(num_experiments)
    ]
    return results


def plot_bar_graph(results):
    counts = Counter(results)
    n_values = list(range(35, 66))
    proportions = [counts[n] / len(results) for n in n_values]

    plt.bar(n_values, proportions, align="center", alpha=0.75)
    plt.title("Proportion of Heads in 1000 Coin Toss Experiments")
    plt.xlabel("Number of Heads")
    plt.ylabel("Proportion")
    plt.show()


# Run the program
num_experiments = 1000
num_tosses = 100

results = run_experiment(num_experiments, num_tosses)
plot_bar_graph(results)
