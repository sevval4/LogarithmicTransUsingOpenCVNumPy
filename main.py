import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to the image
img_path = "./images/Figure_1.png"

# Read the image in grayscale
img = cv2.imread(img_path, 0)
print("Image shape:", img.shape)

# Logarithmic transformation function
def log_transformation(r, c):
    r = r.astype(np.float32)  # Convert to float for log operation
    s = c * np.log(1 + r)  # Apply log transformation
    s = rescale_image(s)  # Rescale the result
    return s.astype(np.uint8)  # Convert back to uint8

# Rescale the image to 0-255 range
def rescale_image(img):
    img -= np.min(img)
    img /= np.max(img)
    img *= 255
    return img

# Apply the log transformation to the image
img_log_transformed = log_transformation(img, 1)

# Stack the original and transformed images horizontally
hstacked = np.hstack((img, img_log_transformed))

# Display the images
plt.imshow(hstacked, cmap="gray")
plt.show()

# Save the log-transformed image
plt.imsave("./images/output_log_image.png", img_log_transformed, cmap="gray")

# Display the log-transformed image again
plt.imshow(img_log_transformed, cmap="gray")
plt.show()

# Example with an array
a = np.array([5, 50, 150, 254, 255], dtype=np.uint8)
a_log = log_transformation(a, 1)

# Normalize the log-transformed values for display
a_log = a_log - np.min(a_log)
a_log = a_log / np.max(a_log)
a_log = a_log * 255

print("Original values:", a)
print("Log-transformed values:", a_log)
