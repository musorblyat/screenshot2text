![Icon](/images/icon.png)
# screenshot2text


This Python script converts images to text using the Tesseract OCR library. The output text is displayed in a colorful format.

## Prerequisites

- Python 3.x
- Tesseract OCR installed on your system
  - On Ubuntu: `sudo apt-get install tesseract-ocr`
  - On Windows: Download and install from [Tesseract GitHub Releases](https://github.com/tesseract-ocr/tesseract/releases)
 
## Example

![GIF](/images/ss2text.gif)


## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/image-to-text-converter.git](https://github.com/vinetsuicide/screenshot2text.git
    cd screenshot2text
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script with the path to the image file as a command-line argument:

    ```bash
    python3 ss2text.py "ur image"
    ```

   The converted text will be displayed in a colorful format.

## Customization

You can customize the colors in the script (`colorful_output` function) according to your preferences.

## Script Overview

The script consists of two main functions:

- **image_to_text(image_path):** Opens an image file and uses Tesseract OCR to extract text.
- **colorful_output(text):** Prints the converted text in a colorful format.

## Command Line Arguments

- **image_path:** Path to the image file that you want to convert to text.

