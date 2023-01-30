from PIL import Image
import sys

def change_colors(image_path, color1, color2):
    # Open the image
    image = Image.open(image_path)

    # Convert image to RGB mode
    image = image.convert('RGB')

    # Get the image data as a list of tuples
    pixels = list(image.getdata())

    # Replace the first color with black and second color with dark grey
    new_pixels = [(0, 0, 0) if pixel == color1 else (64, 64, 64) if pixel == color2 else pixel for pixel in pixels]

    # Update the image with the new pixels
    image.putdata(new_pixels)

    # Save the modified image
    image.save(image_path)

# Example usage
change_colors('hero.png', (215, 170, 117), (222, 197, 172))