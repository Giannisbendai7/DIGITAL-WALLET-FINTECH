import streamlit as st

st.title("Customer Lifetime Value Predictor")

age = st.number_input("Age")
income = st.number_input("Income")

if st.button("Predict"):
    st.write("Predicted LTV: 1234 € (dummy)")
