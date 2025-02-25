import cv2
import numpy as np

def load_image(image_path):
    """Load an image from the specified path."""
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found at the path: {image_path}")
    return image

def convert_to_grayscale(image):
    """Convert the image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def detect_sudoku_grid(image):
    """Detect the Sudoku grid in the image."""
    gray_image = convert_to_grayscale(image)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edged_image = cv2.Canny(blurred_image, 50, 150)

    contours, _ = cv2.findContours(edged_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sudoku_contour = max(contours, key=cv2.contourArea)

    return sudoku_contour

def extract_sudoku_region(image, contour):
    """Extract the Sudoku region from the image based on the detected contour."""
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Create a mask for the Sudoku grid
    mask = np.zeros_like(image)
    cv2.drawContours(mask, [approx], -1, (255, 255, 255), thickness=cv2.FILLED)

    # Bitwise AND to extract the Sudoku grid
    sudoku_region = cv2.bitwise_and(image, mask)

    return sudoku_region, approx

def preprocess_image(image):
    """Preprocess the image for Sudoku solving."""
    contour = detect_sudoku_grid(image)
    sudoku_region, approx = extract_sudoku_region(image, contour)

    # Further processing can be done here (e.g., resizing, thresholding)
    return sudoku_region, approx