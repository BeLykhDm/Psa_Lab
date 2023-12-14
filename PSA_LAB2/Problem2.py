import random


def simulate_election(sample_size, republican_share, democratic_share, num_simulations):
    correct_predictions = 0

    for _ in range(num_simulations):
        votes = [random.random() < democratic_share for _ in range(sample_size)]
        democratic_votes = sum(votes)
        republican_votes = sample_size - democratic_votes

        if democratic_votes > republican_votes:
            correct_predictions += 1

    return correct_predictions


# Simulation parameters
num_simulations = 100
sample_size = 1000  # Change to 3000 for the second part of the experiment
republican_share_48 = 0.48
democratic_share_52 = 0.52
republican_share_49 = 0.49
democratic_share_51 = 0.51

# Run simulations
pred_48_52_sample_1000 = simulate_election(
    sample_size, republican_share_48, democratic_share_52, num_simulations
)
pred_49_51_sample_1000 = simulate_election(
    sample_size, republican_share_49, democratic_share_51, num_simulations
)

# Update sample size for the third simulation
sample_size = 3000
pred_49_51_sample_3000 = simulate_election(
    sample_size, republican_share_49, democratic_share_51, num_simulations
)
pred_48_52_sample_3000 = simulate_election(
    sample_size, republican_share_48, democratic_share_52, num_simulations
)
# Print results
print(f"Out of {num_simulations} simulations:")
print(
    f"With a 48/52 split and sample size of 1000, the pollster predicted correctly {pred_48_52_sample_1000} times."
)
print(
    f"With a 48/52 split and sample size of 3000, the pollster predicted correctly {pred_48_52_sample_3000} times."
)
print(
    f"With a 49/51 split and sample size of 1000, the pollster predicted correctly {pred_49_51_sample_1000} times."
)
print(
    f"With a 49/51 split and sample size of 3000, the pollster predicted correctly {pred_49_51_sample_3000} times."
)
