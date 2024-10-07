ITU Image Processing Project: Logarithmic Transformation

Welcome to the ITU Image Processing Project, where we explore logarithmic transformations in image processing using Python's powerful libraries, including OpenCV and NumPy. This transformation is particularly useful for enhancing the visibility of darker regions in an image, providing better contrast and visual detail.

 Project Overview
In this project, we:

Apply logarithmic transformation to grayscale images.
Rescale the image's pixel intensities to fit into the 0-255 range, which is the standard for image processing.
Display the transformed image alongside the original for comparison.
Demonstrate the transformation on both an image and an array of pixel values.
This project is a great introduction to basic image processing techniques and serves as a hands-on application for students and developers working with contrast enhancements.

✨ Features
Logarithmic Image Transformation: Improves the contrast of images, especially in darker areas.
Image Rescaling: Rescales pixel intensities to make the output image displayable and visually appealing.
Side-by-Side Comparison: Easily compare the original and transformed images.
Customizable: Change the scaling constant and apply the transformation to any image.
💻 Requirements
To run this project, you will need the following libraries:

OpenCV (opencv-python)
NumPy
Matplotlib
You can install them using pip:
pip install opencv-python numpy matplotlib

Logarithmic Transformation Explained
Logarithmic transformation is a technique often used to enhance images with large dynamic ranges. It emphasizes darker pixel values while compressing higher ones, resulting in better contrast for low-intensity regions.

The transformation function is:

s=c⋅log(1+r)

Where:

r is the original pixel value.
c is a scaling constant (often set to 1).
s is the transformed pixel value.
After applying this transformation, the pixel values are rescaled to fit into the 0-255 range to make them suitable for display.

Why Logarithmic Transformation?
Enhances low-intensity values in the image, which makes it easier to see details in dark regions.
Useful for images with wide intensity ranges, such as astronomical images, X-rays, and low-light photography.

📊 Results
After running the script, you will be able to see both the original and log-transformed images side by side. Here’s what happens:

The darker regions of the image become more visible.
The transformation improves the contrast in low-intensity areas, while compressing the brighter areas.
