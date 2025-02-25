import cv2
import pytesseract

def extract_numbers_from_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Preprocess the image: convert to grayscale and apply thresholding
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

    # Use Tesseract to extract numbers from the processed image
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    recognized_text = pytesseract.image_to_string(thresh_image, config=custom_config)

    # Convert the recognized text into a structured format (list of integers)
    numbers = []
    for line in recognized_text.splitlines():
        if line.strip():
            numbers.append([int(num) if num.isdigit() else 0 for num in line.split()])

    return numbers