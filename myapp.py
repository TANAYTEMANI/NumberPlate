import streamlit as st
import pandas as pd
import numpy as np
import cv2
import os
import pandas as pd

harcascade = "model/haarcascade_russian_plate_number.xml"

st. set_page_config (layout="wide")

col1, col2 = st.columns([2 , 1], gap="large")
data = np.random.randn(10, 1)
df = pd.read_csv("plates/data.csv")
min_area = 500
with col1:
    st.header("Camera View")
    img_file_buffer = st.camera_input('Input Camera', key = 'cam')
    confirm = st.button('Confirm', use_container_width=True)
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
    st.subheader("Dataset")
    st.dataframe(df, use_container_width=True)