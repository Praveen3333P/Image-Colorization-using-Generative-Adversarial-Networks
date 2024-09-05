# Image Colorization Project

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Model Architecture](#model-architecture)
8. [Training](#training)
9. [Future Improvements](#future-improvements)
10. [Contributing](#contributing)
11. [License](#license)

## Introduction
This project implements an image colorization system using a Generative Adversarial Network (GAN). It takes grayscale images as input and produces colorized versions. The project combines a deep learning backend built with TensorFlow/Keras and a user-friendly frontend web application using Flask.

## Features
- Colorize grayscale images using a trained GAN model.
- Web-based user interface for easy image upload and colorization.
- Real-time colorization preview.
- Ability to download colorized images.

## Technologies Used
### Backend:
- Python 3.11.4
- TensorFlow 2.16.1
- Keras 3.0.5
- NumPy 1.24.3
- Matplotlib 3.7.2
- scikit-image 0.22.0

### Frontend:
- HTML5
- CSS3
- JavaScript
- Flask (Python web framework)

## Project Structure
```
image-colorization/
│
├── data2/
│   ├── test_black/
│   ├── test_color/
│   ├── train_black/
│   └── train_color/
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── webimages/
│       ├── about2.png
│       ├── colorsplash.jpg
│       ├── luffy.jpg
│       └── Tlogo.png
│
├── templates/
│   └── index.html
│
├── colorization_generator.h5
├── colorization_test.py
├── app.py
├── NEWTESTGAN.ipynb
└── README.md
```

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Praveen3333P/Image-Colorization-using-GANS.git
   cd image-colorization
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Upload a grayscale image and click the "Colorize" button.

4. View the colorized result and download it if desired.

## Model Architecture
The colorization model uses a GAN architecture:

- **Generator**: U-Net architecture for image-to-image translation.
- **Discriminator**: Convolutional neural network for distinguishing real from generated images.

For more details, refer to the GAN model implementation in `NEWTESTGAN.ipynb`.

## Training
To train the model on your own dataset:

1. Prepare your dataset in the `data2/` directory.
2. Adjust training parameters in `NEWTESTGAN.ipynb` if needed.
3. Run the training script within the notebook.

The script will save the trained generator model as `colorization_generator.h5`.

## Future Improvements
- Implement data augmentation for better generalization.
- Experiment with different loss functions (e.g., perceptual loss).
- Add support for batch processing of multiple images.
- Optimize the model for faster inference on lower-end devices.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
