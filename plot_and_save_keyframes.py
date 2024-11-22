import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Load the keyframe trajectory
def load_trajectory(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("#"):  # Skip comments
                continue
            values = list(map(float, line.strip().split()))
            timestamp, tx, ty, tz = values[:4]  # Extract the position data
            data.append([tx, ty, tz])
    return np.array(data)

# Plot the keyframe trajectory
def plot_and_save_trajectory(data, output_image_path):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the trajectory
    ax.plot(data[:, 0], data[:, 1], data[:, 2], label="Keyframe Trajectory", color='blue')
    
    # Mark keyframes
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='red', marker='o', label="Keyframes")
    
    # Label the starting point
    ax.scatter(data[0, 0], data[0, 1], data[0, 2], c='green', marker='o', s=100, label="Start Point")
    ax.text(data[0, 0], data[0, 1], data[0, 2], "Start", color='green')
    
    # Label the ending point
    ax.scatter(data[-1, 0], data[-1, 1], data[-1, 2], c='purple', marker='o', s=100, label="End Point")
    ax.text(data[-1, 0], data[-1, 1], data[-1, 2], "End", color='purple')

    # Labels and title
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")
    ax.set_title("Keyframe Trajectory")
    ax.legend()
    
    # Save the plot as an image
    plt.savefig(output_image_path)
    print("Trajectory plot saved as: {}".format(output_image_path))
    
    # Show the interactive graph
    plt.show()

# Main function
def main():
    trajectory_file = "MyVideoKeyFrameTrajectoryTUMFormat.txt"  # Replace with your file path
    output_image_path = "MyVideoKeyframeTrajectoryPlot.png"    # Image file to save the plot

    # Load trajectory data
    if not os.path.exists(trajectory_file):
        print("Error: File {} not found.".format(trajectory_file))
        return

    trajectory_data = load_trajectory(trajectory_file)

    # Plot and save the trajectory
    plot_and_save_trajectory(trajectory_data, output_image_path)

if __name__ == "__main__":
    main()
