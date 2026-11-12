import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Load the CSV data
file_path = "palm_20250117_150904.csv"  # Replace with your actual file path
data = pd.read_csv(file_path)

# Print column names to debug
print("Columns in CSV:", data.columns)

# Use the exact column names found in the file
timestamps = data["Timestamp"]  # Update this based on actual column names
values = data["Analog1"]        # Update this based on actual column names

# Normalize the values to range between 0 and 1
normalized_values = (values - values.min()) / (values.max() - values.min())

# Prepare data for radial plot
angles = np.linspace(0, 2 * np.pi, len(normalized_values), endpoint=False)
radii = normalized_values

# Function to create radial visualizations
def create_radial_plot(option):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, polar=True)

    if option == "line":
        ax.plot(angles, radii, color="black")

    elif option == "filled_line":
        ax.plot(angles, radii, color="black")
        ax.fill(angles, radii, color="black", alpha=0.3)

    elif option == "bar":
        ax.bar(angles, radii, width=0.05, color='black', edgecolor='white')

    elif option == "heatmap":
        theta, r = np.meshgrid(angles, np.linspace(0, 1, 10))
        z = np.tile(radii, (10, 1))
        ax.pcolormesh(theta, r, z, cmap="Greys")

    elif option == "spiral":
        radii_spiral = radii + np.linspace(0, 1, len(normalized_values))
        ax.plot(angles, radii_spiral, color='black')

    elif option == "scatter":
        ax.scatter(angles, radii, color='black', s=10)
        ax.fill(angles, radii, color="black", alpha=0.3)

    elif option == "waveform":
        wave_radii = radii + 0.1 * np.sin(angles * 10)
        ax.plot(angles, wave_radii, color='black')
        ax.fill(angles, radii, color="black", alpha=0.3)

    elif option == "rose":
        bin_edges = np.linspace(0, 1, 10)
        hist, _ = np.histogram(radii, bins=bin_edges)
        ax.bar(angles[:len(hist)], hist, width=0.3, color='black', edgecolor='white')

    else:
        print("Invalid option")
        return

    # Customize the plot
    ax.set_yticks([])  # Remove radial ticks
    ax.set_xticks([])  # Remove angular ticks
    ax.spines["polar"].set_visible(False)  # Hide the polar spine

    # Save the figure
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"swim_{option}__{timestamp}.png"
    plt.savefig(filename, dpi=100, bbox_inches="tight", pad_inches=0)
    print(f"Radial graph saved as '{filename}'")

# Example: Choose which type of visualization to create
# Options: "line", "filled_line", "bar", "heatmap", "spiral", "scatter", "waveform", "rose"
create_radial_plot("scatter")
