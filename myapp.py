import streamlit as st
import random
import pandas as pd
import numpy as np
import cv2
import os
import pandas as pd

harcascade = "model/haarcascade_russian_plate_number.xml"

st. set_page_config (layout="wide")

col1, col2 = st.columns([2 , 1], gap="large")
data = np.random.randn(10, 1)
checkin_df = pd.read_csv("plates/checkin_data.csv")
checkout_df = pd.read_csv("plates/checkout_data.csv")
min_area = 500
with col1:
    st.header("Checkin")
    url = "http://10.120.104.178:8080/video"
    cap = cv2.VideoCapture(url)
    ret, frame = cap.read()
    img_file_buffer = st.camera_input('Input Camera', key = 'check_in_camcam')
    confirm = st.button('Confirm Checkin', use_container_width=True)
    if img_file_buffer is not None and confirm:
        bytes_data = img_file_buffer.getvalue()
        img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        plate_cascade = cv2.CascadeClassifier(harcascade)
        plates = plate_cascade.detectMultiScale(img, 1.1, 4)
        for (x,y,w,h) in plates:
            area = w * h
            if area > min_area:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
                img_roi = img[y: y+h, x:x+w]
                st.image(img_roi)
        cv2.imwrite("plates/scaned_img.jpg", img_roi)
        os.system('~/miniconda3/envs/easyocr/bin/python easy_ocr.py checkin')
            
with col2:
    st.subheader("Parking Lot Status")
    st.dataframe(checkin_df, use_container_width=True)


col3, col4 = st.columns([2 , 1], gap="large")
data = np.random.randn(10, 1)
min_area = 500
with col3:
    st.header("Camera View")
    img_file_buffer = st.camera_input('Input Camera', key = 'check_out_cam')
    confirm = st.button('Confirm Checkout', use_container_width=True)
    if img_file_buffer is not None and confirm:
        bytes_data = img_file_buffer.getvalue()
        img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        plate_cascade = cv2.CascadeClassifier(harcascade)
        plates = plate_cascade.detectMultiScale(img, 1.1, 4)
        for (x,y,w,h) in plates:
            area = w * h
            if area > min_area:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
                img_roi = img[y: y+h, x:x+w]
                st.image(img_roi)
        cv2.imwrite("plates/scaned_img.jpg", img_roi)
        os.system('~/miniconda3/envs/easyocr/bin/python easy_ocr.py checkin')

amount = [78, 24, 59, 103, 179, 37, 44, 82, 113, 68, 72, 94, 29]
st.button("Please Select the Vehicle to generate bill")
option=st.selectbox("Select the vehicle:", checkin_df)
st.write("The bill amount for vehicle", option, ": ", random.choice(amount))
            
with col4:
    st.subheader("Dataset")
    st.dataframe(checkout_df, use_container_width=True)

