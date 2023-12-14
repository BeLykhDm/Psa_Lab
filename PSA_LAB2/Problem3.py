import random


def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def simulate_breaks(num_trials):
    count = 0
    for _ in range(num_trials):
        # Break the stick at a random point
        first_break = random.uniform(0, 1)
        # Determine lengths of the two pieces
        piece_one = first_break
        piece_two = 1 - first_break
        # Break the longer piece at a random point
        second_break = random.uniform(0, max(piece_one, piece_two))
        # Determine lengths of the three final pieces
        if piece_one > piece_two:
            piece_three = piece_one - second_break
            piece_one = second_break
        else:
            piece_three = piece_two - second_break
            piece_two = second_break
        # Check if the pieces can form a triangle
        if can_form_triangle(piece_one, piece_two, piece_three):
            count += 1
    return count / num_trials


# Number of simulations
num_trials = 100000
probability = simulate_breaks(num_trials)
print(f"The probability of being able to form a triangle is {probability:.4f}")
