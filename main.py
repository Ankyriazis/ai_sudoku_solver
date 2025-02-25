import cv2
import numpy as np
from image_processing import load_image, preprocess_image, detect_sudoku_grid
from ocr import recognize_numbers
from solver import SudokuSolver

def main():
    # Load and preprocess the image
    image_path = 'data/sample_images/example.jpg'
    image = load_image(image_path)
    processed_image = preprocess_image(image)

    # Detect the Sudoku grid
    grid = detect_sudoku_grid(processed_image)

    # Recognize numbers in the grid
    numbers = recognize_numbers(grid)

    # Solve the Sudoku puzzle
    solver = SudokuSolver(numbers)
    if solver.solve():
        print("Sudoku solved successfully!")
        print(solver.get_solution())
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()