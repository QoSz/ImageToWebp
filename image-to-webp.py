import os
from PIL import Image

# Create a folder to store the converted images
output_folder = "WEBP"
os.makedirs(output_folder, exist_ok=True)

# Get a list of all files in the current directory
files = os.listdir()

# Iterate over each file in the directory
for file in files:
    # Check if the file is an image
    if file.endswith((".jpg", ".jpeg", ".png")):
        # Open the image file
        image = Image.open(file)

        # Convert the image to WebP format
        image.save(os.path.join(output_folder, os.path.splitext(file)[0] + ".webp"), "WEBP")

        # Close the image file
        image.close()

print("Image conversion complete!")
