

import streamlit as st
import joblib

model = joblib.load("diabetes_model.pkl")

st.title("Diabetes Prediction App")

preg = st.number_input("Pregnancies")
glu = st.number_input("Glucose")
bp = st.number_input("Blood Pressure")
skin = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

if st.button("Predict"):
    input_data = [[preg, glu, bp, skin, insulin, bmi, dpf, age]]
    prediction = model.predict(input_data)[0]
    result = "Diabetic" if prediction == 1 else "Not Diabetic"
    st.success(result)
