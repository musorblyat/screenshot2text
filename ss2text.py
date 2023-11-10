from PIL import Image
import pytesseract
import argparse


def image_to_text(image_path):
   
    image = Image.open(image_path)
    
    
    text = pytesseract.image_to_string(image)
    
    return text

#Colors
def colorful_output(text):
    
    color_code = {
        'header': '\033[95m',
        'blue': '\033[94m',
        'green': '\033[92m',
        'warning': '\033[93m',
        'fail': '\033[91m',
        'end': '\033[0m',
    }
    
    print(color_code['header'] + "[+]Converted Text:" + color_code['end'])
    print(color_code['blue'] + text + color_code['end'])


parser = argparse.ArgumentParser(description="Convert image to text")
parser.add_argument("image_path", help="Path to the image file")
args = parser.parse_args()


result_text = image_to_text(args.image_path)


colorful_output(result_text)

