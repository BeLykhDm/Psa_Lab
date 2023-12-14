import matplotlib.pyplot as plt
import random


# Simulate the dice rolls and calculate proportions
def simulate_dice_rolls(number_of_tests):
    nine_count = 0
    ten_count = 0

    for _ in range(number_of_tests):
        result = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        if result == 9:
            nine_count += 1
        elif result == 10:
            ten_count += 1

    proportion_nine = nine_count / number_of_tests
    proportion_ten = ten_count / number_of_tests
    print(f"Proportion of getting a sum of 9: {proportion_nine:.2%}")
    print(f"Proportion of getting a sum of 10: {proportion_ten:.2%}")
    return proportion_nine, proportion_ten


# Number of tests (simulations)
x = 10000  # Example value for demonstration

# Get the proportions from the simulation
proportion_nine, proportion_ten = simulate_dice_rolls(x)

# Data for plotting
labels = ["Sum of 9", "Sum of 10"]
proportions = [proportion_nine, proportion_ten]

# Plotting the proportions as a bar graph
plt.bar(labels, proportions, color=["blue", "green"])
plt.ylabel("Proportion")
plt.title("Proportion of Getting a Sum of 9 vs 10")

# Display the graph
plt.show()
