from rembg import remove
import cv2
import numpy as np
from PIL import Image

import cv2

img = cv2.imread("resouces/Healing_Potion.jpg")  # Read image

# Setting All parameters
t_lower = 100  # Lower Threshold
t_upper = 150  # Upper threshold
aperture_size = 5  # Aperture size

scale_percent = 20  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resizes image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Applying the Canny Edge filter
# with Custom Aperture Size
edge = cv2.Canny(resized, t_lower, t_upper)

cv2.imshow('original', resized)
cv2.imshow('edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()