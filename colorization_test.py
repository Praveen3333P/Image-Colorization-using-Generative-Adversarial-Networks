import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from PIL import Image
import matplotlib.pyplot as plt
from skimage import color
import io
import base64

# Load the trained model
model = load_model('colorization_generator.h5')

def preprocess_image(image_path, target_size=(128, 128)):
    img = Image.open(image_path).convert('RGB')
    img = img.resize(target_size)
    img_array = np.array(img)
    img_lab = color.rgb2lab(img_array / 255.0)
    img_l = img_lab[:,:,0]
    img_l = img_l / 50.0 - 1.0
    return np.expand_dims(img_l, axis=-1)

def postprocess_output(l_channel, ab_channels):
    lab = np.concatenate([l_channel, ab_channels], axis=-1)
    lab[:,:,0] = (lab[:,:,0] + 1.0) * 50.0
    lab[:,:,1:] = lab[:,:,1:] * 128.0
    rgb_image = color.lab2rgb(lab) * 255.0
    return rgb_image.astype(np.uint8)

def colorize_image(image_path):
    # Preprocess the input image
    input_image = preprocess_image(image_path)
    
    # Make prediction
    ab_output = model.predict(np.expand_dims(input_image, axis=0))[0]
    
    # Postprocess the output
    colorized_image = postprocess_output(input_image, ab_output)
    
    return colorized_image

def image_to_base64(image_array):
    img = Image.fromarray(image_array)
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def test_colorization(image_path):
    # Colorize the image
    colorized_image = colorize_image(image_path)
    
    # Convert the original image to grayscale for comparison
    original_image = Image.open(image_path).convert('RGB')
    grayscale_image = original_image.convert('L').convert('RGB')
    
    # Convert images to base64 for web display
    original_base64 = image_to_base64(np.array(original_image))
    grayscale_base64 = image_to_base64(np.array(grayscale_image))
    colorized_base64 = image_to_base64(colorized_image)
    
    return {
        'original': original_base64,
        'grayscale': grayscale_base64,
        'colorized': colorized_base64
    }

# Example usage
if __name__ == "__main__":
    test_image_path = "path/to/your/test/image.jpg"
    result = test_colorization(test_image_path)
    
    # You can now use these base64 strings in your HTML
    print("Original image (base64):", result['original'][:50] + "...")
    # print("Grayscale image (base64):", result['grayscale'][:50] + "...")
    print("Colorized image (base64):", result['colorized'][:50] + "...")