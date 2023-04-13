import cv2
import easyocr
import pandas as pd
import numpy as np
from datetime import datetime
import sys

print(sys.argv)
assert len(sys.argv) == 2, 'There should only be one task given.'

task = sys.argv[1]
reader = easyocr.Reader(['en'], gpu=False)
image=cv2.imread('plates/scaned_img.jpg')
output = reader.readtext(image,detail=0)[0]
now = datetime.now()
data = pd.read_csv('plates/data.csv')

if task == 'checkin':
	data.loc[len(data.index)] = [output, now, np.nan]
	data.to_csv('plates/data.csv', index=False)
	
elif task == 'checkout':
	checkout = data.columns[-1]
	print(data.loc[data['platenumber'] == output])
	assert data.loc[data['platenumber'] == output] == np.nan, 'User already checked out.'
	data.loc[data['platenumber'] == output].iloc[-1] = now
	data.to_csv('plates/data.csv', index=False)