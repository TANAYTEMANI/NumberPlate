import cv2
import easyocr
import pandas as pd
import numpy as np
from datetime import datetime
import sys
import random

assert len(sys.argv) == 2, 'There should only be one task given.'

task = sys.argv[1]
reader = easyocr.Reader(['en'], gpu=False)
image=cv2.imread('plates/scaned_img.jpg')
output = reader.readtext(image,detail=0)[0]
now = datetime.now()
data_checkin = pd.read_csv('plates/checkin_data.csv')
data_checkout = pd.read_csv('plates/checkout_data.csv')

slot = pd.read_csv("../CarPark/status.csv")
emptySlots = list(slot[slot.status == True].parkVal)


if task == 'checkin':
	allocated_slot = emptySlots.pop(0)
	data_checkin.loc[len(data_checkin.index)] = [output,allocated_slot, now]
	slot.at[allocated_slot,'status']=False
	slot.to_csv("../CarPark/status.csv", index=False)
	data_checkin.to_csv('plates/checkin_data.csv', index=False)

		
elif task == 'checkout':
	data_checkout.loc[len(data_checkout.index)] = [output, now]
	slot.at[allocated_slot,'status']=False
	slot.to_csv("../CarPark/status.csv", index=False)
	data_checkout.to_csv('plates/checkout_data.csv', index=False)