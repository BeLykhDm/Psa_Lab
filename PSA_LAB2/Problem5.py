import random


def simulate_until_boy():
    children_count = 0
    while random.choice(["boy", "girl"]) != "boy":
        children_count += 1
    return children_count + 1  # Including the boy


def simulate_until_boy_and_girl():
    children_count = 0
    has_boy = False
    has_girl = False

    while not (has_boy and has_girl):
        child_gender = random.choice(["boy", "girl"])
        children_count += 1

        if child_gender == "boy":
            has_boy = True
        elif child_gender == "girl":
            has_girl = True

    return children_count


def simulate_families(num_families, simulation_function):
    total_children = 0

    for _ in range(num_families):
        total_children += simulation_function()

    average_children = total_children / num_families
    return average_children


# Number of families in the simulation
num_families = 1000000

# Simulate until having a boy
average_children_until_boy = simulate_families(num_families, simulate_until_boy)

# Simulate until having at least one boy and at least one girl
average_children_until_boy_and_girl = simulate_families(
    num_families, simulate_until_boy_and_girl
)

# Calculate the difference in average children
difference = average_children_until_boy_and_girl - average_children_until_boy

print(f"Average children until boy: {average_children_until_boy}")
print(f"Average children until boy and girl: {average_children_until_boy_and_girl}")
print(f"Difference in average children: {difference}")
