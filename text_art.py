import os
import numpy as np
from PIL import Image
import requests


WIDTH = 100
image_path = 'channels4_profile.jpg'
file_output_file = 'text_art.txt'


# Open the image file
img = Image.open(image_path).convert('L')  # convert image to 8-bit grayscale

# Define the ASCII characters that will represent the grayscale values
# The list of characters is sorted by increasing "density"
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Resize the image according to a new width

width, height = img.size
ratio = height / width
new_height = int(WIDTH * ratio)
img = img.resize((WIDTH, new_height))

# Convert each pixel to grayscale
pixels = np.array(img)

# Normalize the pixels between 0 and 1 and multiply by the number of ASCII characters
normalized_pixels = pixels / 255
ascii_pixels = (normalized_pixels * (len(ASCII_CHARS) - 1)).astype(int)

# Map each normalized pixel to an ASCII character
ascii_image = [" ".join([ASCII_CHARS[pixel] for pixel in row]) for row in ascii_pixels]

ascii_image_text = "\n".join(ascii_image)

# Open the code to see the text art in terminal
# print(ascii_image_text)

with open(file_output_file, 'w') as file:
    file.write(ascii_image_text)

os.system(f'notepad {file_output_file}')

print("[info] complete")