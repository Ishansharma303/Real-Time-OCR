
import pytesseract
import cv2
import matplotlib.pyplot as plt


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('3.png')
plt.imshow(img)
plt.show()

img2char = pytesseract.image_to_string(img)
print(img2char)

imgbox = pytesseract.image_to_boxes(img)
imgH, imgW,_ = img.shape

for boxes in imgbox.splitlines():
    boxes = boxes.split(' ')
    x,y,w, h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
    cv2.rectangle(img,(x, imgH-y),(w, imgH-h),(0,0,255),3)

plt.imshow(img)
plt.show()