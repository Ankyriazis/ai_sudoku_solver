# AI-Based Sudoku Solver

## Overview
This project presents an AI-driven solution for solving Sudoku puzzles using computer vision and deep learning techniques. The application leverages OpenCV for image processing, Tesseract OCR for number recognition, and Convolutional Neural Networks (CNNs) to enhance accuracy in recognizing numbers from Sudoku puzzles.

## Technologies Used
- Python
- OpenCV
- NumPy
- Deep Learning (CNNs)

## Key Features
- **Image Processing Pipeline**: Scans Sudoku puzzles from images using OpenCV.
- **Number Recognition**: Utilizes Tesseract OCR, improved with CNNs for better accuracy.
- **Sudoku Solver**: Implements a backtracking algorithm to efficiently solve the puzzle.

## Project Structure
```
ai-sudoku-solver
├── src
│   ├── main.py            # Entry point of the application
│   ├── image_processing.py # Functions for processing Sudoku images
│   ├── ocr.py             # Tesseract OCR integration for number recognition
│   ├── solver.py          # Backtracking algorithm for solving Sudoku
│   └── utils.py           # Utility functions for various tasks
├── models
│   └── cnn_model.h5       # Trained CNN model for number recognition
├── data
│   └── sample_images
│       └── example.jpg    # Sample image of a Sudoku puzzle
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Installation Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-sudoku-solver.git
   cd ai-sudoku-solver
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines
1. Place your Sudoku puzzle images in the `data/sample_images` directory.
2. Run the application:
   ```
   python src/main.py
   ```
3. The solution will be displayed in the console, and the processed image will be saved in the output directory.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.