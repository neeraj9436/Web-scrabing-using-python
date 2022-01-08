import pytesseract as tess
from pytesseract import Output
from PIL import Image
import cv2

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img2 = cv2.imread('photo3.jpg')

text=tess.image_to_string(img2)
##boxes = tess.image_to_boxes(img2) # also include any config options you use
##h, w, _ = img2.shape # assumes color image
### draw the bounding boxes on the image
##for b in boxes.splitlines():
##    b = b.split(' ')
##    img2 = cv2.rectangle(img2, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
##
### show annotated image and wait for keypress
##cv2.imshow('ppp', img2)

d = tess.image_to_data(img2,output_type=Output.DICT)
keys = list(d.keys())
##print(keys)
##print(d)
##print(d[0])
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    if d['text'][i] == "":
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print(w*h)
        cv2.putText(img2,str(i),(x+20,y+20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)

print(text)
cv2.imshow('img', img2)
cv2.waitKey(0)












