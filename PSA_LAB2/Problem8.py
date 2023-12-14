import random


# Function to check if no two people sit next to each other
def no_adjacent_seating(arrangement):
    n = len(arrangement)
    for i in range(n):
        if arrangement[i] == arrangement[(i + 1) % n]:
            return False
    return True


# Function to simulate seating and calculate probability
def simulate_probability(iterations):
    favorable_outcomes = 0

    for _ in range(iterations):
        participants = list(range(1, 11))  # Participants labeled from 1 to 10
        random.shuffle(participants)  # Randomly shuffle the participants

        lunch_arrangement = participants.copy()  # Copy the arrangement for lunch
        random.shuffle(
            participants
        )  # Randomly shuffle the participants again for dinner

        dinner_arrangement = participants

        if no_adjacent_seating(lunch_arrangement) and no_adjacent_seating(
            dinner_arrangement
        ):
            favorable_outcomes += 1

    probability = favorable_outcomes / iterations
    return probability


# Number of simulations
num_simulations = 100000

# Run the simulation
result = simulate_probability(num_simulations)

# Print the estimated probability
print(f"Estimated probability: {result}")
