import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def simulate_coin_toss(num_tosses, num_experiments):
    results = np.random.binomial(num_tosses, 0.5, size=num_experiments)
    return results


def plot_bar_graph(results):
    plt.hist(results, bins=range(35, 66), density=True, edgecolor="black", alpha=0.7)
    plt.title("Distribution of Heads in 100 Tosses, 1000 Experiments")
    plt.xlabel("Number of Heads")
    plt.ylabel("Proportion")

    # Fit a normal distribution curve
    mu, std = norm.fit(results)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, "k", linewidth=2)

    plt.show()


num_tosses = 100
num_experiments = 1000

coin_toss_results = simulate_coin_toss(num_tosses, num_experiments)
plot_bar_graph(coin_toss_results)
