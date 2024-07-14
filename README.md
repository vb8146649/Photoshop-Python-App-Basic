# Photoshop-Python-App-Basic

Welcome to the **Photoshop-Python-App-Basic**! This application allows you to perform various image editing tasks, including changing the image color to negative, applying blur, converting to grayscale, and removing the background using the `rembg` library. The app is built using the PyQt5 library, providing a user-friendly graphical interface for these operations.

<img src='https://github.com/vb8146649/Photoshop-Python-App-Basic/assets/133308727/ff9cd9d1-76b4-4c4b-a4e6-987c69b20512' width=350>

## Features

- **Negative Image**: Invert the colors of the image to create a negative effect.
- **Blur Image**: Apply a blur effect to the image.
- **Grayscale Image**: Convert the image to grayscale.
- **Remove Background**: Remove the background from the image using the `rembg` library.

## Installation

To run this application, you need to have Python installed on your system along with the required libraries. Follow the steps below to set up the environment:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/vb8146649/Photoshop-Python-App-Basic
    cd Photoshop-Python-App-Basic
    ```

2. **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```

## Requirements

- `PyQt5`
- `rembg`

These libraries will be installed when you run `pip install -r requirements.txt`.

## Usage

```bash
python main.py
```
### How to Use
**Open Image**: Load an image from your computer.
**Edit Image**:
- Click on "Negative" to invert the colors.
- Click on "Blur" to apply a blur effect.
- Click on "Grayscale" to convert the image to grayscale.
- Click on "Remove Background" to remove the background using rembg.
- Save Image: Save the edited image to your computer.

## Acknowledgements
- PyQt5 for the GUI components.
- rembg for background removal.

