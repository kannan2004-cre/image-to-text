from PIL import Image
import pytesseract

# Path to the Tesseract executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'<path_to_your_tesseract_executable>'

def image_to_text(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Perform OCR
    text = pytesseract.image_to_string(img)

    return text

if __name__ == "__main__":
    # Path to the image file
    image_path = 'image.jpg'

    # Convert image to text
    extracted_text = image_to_text(image_path)

    # Print the extracted text
    print(extracted_text)
