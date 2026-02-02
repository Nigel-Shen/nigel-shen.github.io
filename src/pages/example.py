import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Configuration
OUTPUT_DIR = "public/projects/test-sim"
FRAMES = 100

# Ensure directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
    print(f"Created directory: {OUTPUT_DIR}")

# Grid Setup
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

print(f"Generating {FRAMES} frames...")

for i in range(FRAMES):
    # Physics: A decaying sine wave traveling outward
    t = i * 0.1
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R - t) * np.exp(-0.1 * R)

    # Plotting
    fig = plt.figure(figsize=(10, 6), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    
    # Visual Style: Dark background to match your site
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    
    # Wireframe Plot
    ax.plot_wireframe(X, Y, Z, color='cyan', linewidth=0.5, rstride=2, cstride=2)
    
    # Camera / Limits
    ax.set_zlim(-1, 1)
    ax.set_axis_off() # Hide axes for a clean look
    
    # Save Frame
    filename = f"frame_{str(i+1).zfill(3)}.jpg"
    filepath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(filepath, bbox_inches='tight', pad_inches=0, facecolor='black')
    plt.close(fig)
    
    if (i+1) % 10 == 0:
        print(f"Saved {filename}")

print("Done! Images saved to public/projects/test-sim/")