from PIL import Image
import pytesseract


def extract_text_from_image(image_path):
    # Load the image
    image = Image.open(image_path)
    # Extract text using Tesseract OCR
    text = pytesseract.image_to_string(image)
    return text


# Example usage
screenshot_path = r"C:\Users\Ragha\Downloads\TextExtract"
extracted_text = extract_text_from_image(screenshot_path)
print("Extracted Text:", extracted_text)
