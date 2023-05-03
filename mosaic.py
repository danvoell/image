import sys
from PIL import Image

def create_mosaic(input_image_path, output_image_path, mosaic_size=50):
    # Open the input image
    input_image = Image.open(input_image_path)

    # Calculate the width and height of the individual mosaic pieces
    piece_width = input_image.width // mosaic_size
    piece_height = input_image.height // mosaic_size

    # Create a blank image to store the mosaic
    mosaic_image = Image.new("RGB", (input_image.width, input_image.height))

    # Loop through the image and extract the individual mosaic pieces
    for i in range(0, input_image.width, piece_width):
        for j in range(0, input_image.height, piece_height):
            # Crop the piece
            piece = input_image.crop((i, j, i + piece_width, j + piece_height))

            # Calculate the average color of the piece
            avg_color = piece.resize((1, 1)).getpixel((0, 0))

            # Create a solid color image with the average color
            color_piece = Image.new("RGB", (piece_width, piece_height), avg_color)

            # Paste the color piece to the mosaic
            mosaic_image.paste(color_piece, (i, j))

    # Save the mosaic image
    mosaic_image.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "input.jpg" # Path to your input image
    output_image_path = "output.jpg" # Path to save the mosaic image

    create_mosaic(input_image_path, output_image_path)
