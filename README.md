# Python Developer Test 2: FFmpeg and Pillow

## Objective
This script generates a short video from an image using FFmpeg and Pillow. It overlays text onto the image, applies a basic transformation (grayscale, rotation, or resize), and then converts it into a short video clip with background music.

## Features
- **Image Processing:**  
  - Load an image and overlay custom text.
  - Apply basic transformations: grayscale, rotation, or resize.
- **Video Generation:**  
  - Convert the processed image into a video using FFmpeg.
  - Overlay background music on the video.
- **Configurability:**  
  - Easily modify text overlay and transformation type.
  - Customize file inputs for the image and background music.

---

## Installation

### Prerequisites
Make sure you have the following installed:
- **Python 3.x**
- **FFmpeg** ([Download here](https://ffmpeg.org/download.html))
- **Pillow** (Python package)
  ```sh
  pip install pillow

### Setup
1. **Clone the Repository:**
   ```sh
   https://github.com/pranjali-22/Image-to-Video.git
   cd Image-to-Video
2. **Run the script**
   ```sh
    python script.py
## Input Needed

To run the script successfully, ensure you have the following inputs in your project folder:

- **Input Image:**  
  A file (e.g., `input.jpg`) that will be processed. 

- **Background Music:**  
  A music file (e.g., `background.mp3`) that will be used as the background audio for the generated video.

- **Configuration Parameters:**  
  In `script.py`, adjust the following variables to match your input:
  - `input_image`: The path to your input image.
  - `music_file`: The path to your background music file.
  - The overlay text (e.g., `"Hello, World!"`).
  - The transformation type: `"grayscale"`, `"rotate"`, or `"resize"`.

### Output Generated

A user can input the type of transformation that they want to apply—such as **grayscale**, **rotation**, or **resizing**. Based on the input, two files will be generated:

1. **output.jpg:** The image with the applied transformation.  
2. **output.mp4:** A short video generated using the processed image and the background music.





