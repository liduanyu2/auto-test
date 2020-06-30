# coding=utf-8
import pytesseract
from PIL import Image

image = Image.open("#文件路径")
text = pytesseract.image_to_string(image)
print(text)