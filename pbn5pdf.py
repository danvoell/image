from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Load the image
image = Image.open("input.jpg")

# Set the desired width and height for the resized image
width = 40
height = 40

# Resize the image (optional)
image = image.resize((width, height))

# Convert the image to a NumPy array
image_array = np.array(image)

# Flatten the array to 2D
image_array_2d = image_array.reshape(-1, 3)

# Apply k-means clustering to reduce colors
n_colors = 6
kmeans = KMeans(n_clusters=n_colors)
kmeans.fit(image_array_2d)
reduced_colors = kmeans.cluster_centers_

# Replace each pixel color with its cluster number
labels = kmeans.labels_
numbered_image_array = labels.reshape(image_array.shape[:-1])

# Create a color map
color_map = {i: tuple(map(int, reduced_colors[i])) for i in range(n_colors)}

# Create a PDF file with the numbered grid
doc = SimpleDocTemplate("numbered_image.pdf", pagesize=A4)
table_data = []

# Calculate cell size (width and height) based on the desired width and height of the image
page_width, page_height = A4
padding = 20  # margin around the grid
cell_width = (page_width - 2 * padding) / width
cell_height = (page_height - 2 * padding) / height

# Convert the numbered_image_array to a list of lists
for row in numbered_image_array.tolist():
    table_data.append([str(cell) for cell in row])

# Create the table with the data
table = Table(table_data, colWidths=cell_width, rowHeights=cell_height)

# Apply a grid style to the table
table.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('FONT', (0, 0), (-1, -1), 'Helvetica', 10)
]))

# Add the table to the PDF document
doc.build([table])

# Save the color map
with open("color_map.txt", "w") as f:
    for number, color in color_map.items():
        f.write(f"{number}: {color}\n")
