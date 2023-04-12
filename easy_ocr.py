import cv2
import easyocr

image=cv2.imread('plates/scaned_img.jpg')

reader = easyocr.Reader(['en'], gpu=False)

output = reader.readtext(image,detail=0)
print(1)
print(output[0])
