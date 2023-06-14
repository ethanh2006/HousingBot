from PIL import Image
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
fileName = r"Counters6.png"
img1 = np.array(Image.open(fileName))
text = pytesseract.image_to_string(img1)


tempFile = open("tempValues.txt", "w")
tempFile.write(text)
tempFile.close()
tempFile = open("tempValues.txt", "r")

tempText = tempFile.readlines()
num_lines = len(tempText)
for x in range(num_lines):
    tempLine = tempText[x]
    tempLine = tempLine.lower()
    if "guests:" in tempLine:
          print(tempLine)
tempFile.close()

for x in range(num_lines):
    tempLine = tempText[x]
    tempLine = tempLine.lower()
    if "cookies:" in tempLine:
          print(tempLine)
tempFile.close()