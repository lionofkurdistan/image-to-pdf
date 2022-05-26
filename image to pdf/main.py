from PIL import Image
from numpy import imag

# add image to pdf
img = Image.open("anonymus-1920x1080.jpg")

image = img.convert("RGB")

image.save("PDF File.pdf")