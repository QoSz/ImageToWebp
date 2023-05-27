# Image Conversion to WebP

This Python script converts all images in the current directory to WebP format and saves them in a folder called "WEBP". It utilizes the Pillow library to perform the image conversion.

## Requirements

The following dependencies are required to run the script. Install them using the provided `requirements.txt` file.

### Installing Dependencies

To install the dependencies, run the following command:

1. Create a virutal environment using the following command: `python -m venv venv`
2. Activate the virtual environment using the following command: `venv\Scripts\activate`
3. Install the dependencies using the following command: `pip install -r requirements.txt`

- **Pillow**: A powerful Python library for image processing that provides support for opening, manipulating, and saving many different image file formats.

## Usage

1. Place the script file (`convert_images_to_webp.py`) in the directory where your images are located.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:
4. The script will convert all supported image files (JPEG, PNG) in the current directory to WebP format.
5. The converted images will be saved in a folder called "WEBP" in the same directory.

Please note that the script assumes the images are in JPEG or PNG format. If you have images in other formats that you want to convert to WebP, you can modify the `file.endswith()` condition in the script accordingly.

## License

This code is released under the [MIT License](LICENSE).
