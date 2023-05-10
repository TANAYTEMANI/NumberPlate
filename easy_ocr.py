import cv2
import easyocr
import pandas as pd
import numpy as np
from datetime import datetime
import sys
import random

print(sys.argv)
assert len(sys.argv) == 2, 'There should only be one task given.'

task = sys.argv[1]
reader = easyocr.Reader(['en'], gpu=False)
image=cv2.imread('plates/scaned_img.jpg')
output = reader.readtext(image,detail=0)[0]
now = datetime.now()
data = pd.read_csv('plates/checkin_data.csv')
data = pd.read_csv('plates/checkout_data.csv')

slot = ['1A', '1B','2A', '2B','3A', '3B','4A', '4B','5A', '5B','6A', '6B']

if task == 'checkin':
	for i in range(20):
		data.loc[len(data.index)] = [output,random.choice(slot), now]
		data.to_csv('plates/checkin_data.csv', index=False)

	
elif task == 'checkout':
	data.loc[len(data.index)] = [output, now]
	data.to_csv('plates/checkout_data.csv', index=False)