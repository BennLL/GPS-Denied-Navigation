import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the trajectory file
def load_trajectory(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("#"):  # Skip comments
                continue
            values = list(map(float, line.strip().split()))
            timestamp, tx, ty, tz = values[:4]
            data.append([tx, ty, tz])
    return np.array(data)

# Plot the trajectory
def plot_trajectory(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(data[:, 0], data[:, 1], data[:, 2], label="Keyframe Trajectory")
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='r', marker='o')  # Mark keyframes
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()

# Main function
trajectory_file = "test.txt"  # Replace with your file path
trajectory_data = load_trajectory(trajectory_file)
plot_trajectory(trajectory_data)
