from PIL import Image
import numpy as np

# Load the image
image_path = '/mnt/data/DALL·E 2023-11-08 11.00.28 - A die-cut sticker, digital drawing, of a cat. The sticker has a solid white background, a strong black border surrounding the white die-cut border, an.png'
original_image = Image.open(image_path)

# Define the number of rows and columns for the puzzle
rows, cols = 4, 4

# Calculate the size of the individual pieces
piece_width = original_image.width // cols
piece_height = original_image.height // rows

# Create a list to hold the puzzle pieces
pieces = []

# Cut the image into pieces
for i in range(rows):
    for j in range(cols):
        left = j * piece_width
        upper = i * piece_height
        right = (j + 1) * piece_width
        lower = (i + 1) * piece_height
        piece = original_image.crop((left, upper, right, lower))
        pieces.append(piece)

# Shuffle the pieces
np.random.shuffle(pieces)

# Create a new image to hold the shuffled pieces
shuffled_image = Image.new('RGB', (original_image.width, original_image.height))

# Paste the shuffled pieces into the new image
for i in range(rows):
    for j in range(cols):
        piece = pieces.pop(0)
        left = j * piece_width
        upper = i * piece_height
        shuffled_image.paste(piece, (left, upper))

# Save the shuffled image
shuffled_image_path = '/mnt/data/shuffled_cat_sticker_puzzle.png'
shuffled_image.save(shuffled_image_path)
shuffled_image_path
