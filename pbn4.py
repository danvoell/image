from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

# Load the image
image = Image.open("input.jpg")

# Set the desired width and height for the resized image
width = 100
height = 100

# Resize the image (optional)
image = image.resize((width, height))

# Convert the image to a NumPy array
image_array = np.array(image)

# Flatten the array to 2D
image_array_2d = image_array.reshape(-1, 3)

# Apply k-means clustering to reduce colors
n_colors = 10
kmeans = KMeans(n_clusters=n_colors)
kmeans.fit(image_array_2d)
reduced_colors = kmeans.cluster_centers_

# Replace each pixel color with its cluster number
labels = kmeans.labels_
numbered_image_array = labels.reshape(image_array.shape[:-1])

# Create the color map
color_map = {i: tuple(map(int, reduced_colors[i])) for i in range(n_colors)}

# Save the numbered image as a text file
np.savetxt("numbered_image.txt", numbered_image_array, fmt="%d")

# Save the color map
with open("color_map.txt", "w") as f:
    for number, color in color_map.items():
        f.write(f"{number}: {color}\n")
