import matplotlib.pyplot as plt
import numpy as np


def generate_circle_points(radius, num_points):
    theta = np.linspace(0, 2 * np.pi, num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y


def calculate_distances(points):
    distances = np.sqrt(np.diff(points[:, 0]) ** 2 + np.diff(points[:, 1]) ** 2)
    total_distance = np.sum(distances)
    return total_distance


def is_acute_triangle(lines):
    # Find the longest side (c)
    c_squared = np.max(np.sum((lines[:, 2:] - lines[:, :2]) ** 2, axis=1))

    # Find the sum of the squares of the other two sides (a^2 + b^2)
    a_squared = np.sum((lines[0, 2:] - lines[0, :2]) ** 2)
    b_squared = np.sum((lines[1, 2:] - lines[1, :2]) ** 2)
    sum_squared = a_squared + b_squared

    return c_squared < sum_squared


def plot_circle_with_random_points(radius, num_random_points):
    # Generate points on the circle
    circle_x, circle_y = generate_circle_points(radius, 100)

    # Generate random points on the circle
    random_indices = np.random.choice(len(circle_x), num_random_points, replace=False)
    random_x = circle_x[random_indices]
    random_y = circle_y[random_indices]

    # Store coordinates of lines
    lines = np.array(
        [
            [
                random_x[i],
                random_y[i],
                random_x[(i + 1) % num_random_points],
                random_y[(i + 1) % num_random_points],
            ]
            for i in range(num_random_points)
        ]
    )

    # Calculate distances between random points
    total_distance = calculate_distances(lines[:, :2])

    # Check if the triangle is acute
    if is_acute_triangle(lines):
        triangle_type = "Acute Triangle"
        return 1  # Indicates that an acute triangle was found
    else:
        triangle_type = "Not Acute Triangle"
        return 0  # Indicates that an acute triangle was not found


def run_experiment(num_trials, circle_radius, num_random_points):
    acute_count = 0

    for _ in range(num_trials):
        acute_count += plot_circle_with_random_points(circle_radius, num_random_points)

    percentage_acute = (acute_count / num_trials) * 100
    print(f"Percentage of acute triangles: { 100 - percentage_acute:.2f}%")


# Set parameters for the experiment
num_trials = 1000
circle_radius = 1
num_random_points = 3

# Run the experiment
run_experiment(num_trials, circle_radius, num_random_points)
