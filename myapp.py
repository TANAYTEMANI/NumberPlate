import streamlit as st
import pandas as pd
import numpy as np



col1, col2 = st.columns([2 , 1], gap="medium")
data = np.random.randn(10, 1)
df = pd.read_csv("plates/data.csv")

with col1:
    container1=st.container()
    if container1.button('Start', type="primary"):
        col3, col4 = st.columns([1, 1], gap="small")
        with col3:
            st.button('Checkin')
        with col4:
            st.button('Checkout')
    st.header("Camera View")
    st.line_chart(data)
    container2=st.container()
    if container2.button('Capture'):
        st.write("Number Plate Captured")

with col2:
    st.subheader("Dataset")
    st.write(df, 3)