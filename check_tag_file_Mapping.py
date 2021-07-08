import re
import cv2 
import numpy as np
import pytesseract
from pytesseract import Output
from matplotlib import pyplot as plt

image = cv2.imread('images/invoice2.png')
clone_image = cv2.imread('images/invoice2.png', 0)
d = pytesseract.image_to_data(image, output_type=Output.DICT)
print('DATA KEYS: \n', d.keys())

n_boxes = len(d['text'])
for i in range(n_boxes):
    # condition to only pick boxes with a confidence > 60%
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # extract text per word as plotted in image 
        thresh = 255 - cv2.threshold(clone_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
       
        ROI = thresh[y:y+h,x:x+w]
        data = pytesseract.image_to_string(ROI, lang='eng',config='--psm 6')
        print("data at word : "+str(i))
        print(data)

b,g,r = cv2.split(image)
rgb_img = cv2.merge([r,g,b])
plt.figure(figsize=(16,12))
plt.imshow(rgb_img)
plt.title('SAMPLE INVOICE WITH WORD LEVEL BOXES')
plt.show()