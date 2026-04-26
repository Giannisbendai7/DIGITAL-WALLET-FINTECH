import streamlit as st
from predict import predict

st.title("Digital Wallet LTV Predictor")

if st.button("Run prediction"):
    result = predict([[1, 2, 3]])
    st.write(result)
