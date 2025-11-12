import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model and preprocessing tools
model = joblib.load("salary_prediction_model.joblib")
scaler = joblib.load("scaler.joblib")
label_encoders = joblib.load("label_encoders.joblib")

st.set_page_config(page_title="Salary Prediction", layout="centered")

st.title("💼 Salary Prediction App")
st.write("Enter candidate details below and click **Predict Salary**.")

# Extract unique choices from saved label encoders
def get_choices(col):
    le = label_encoders.get(col)
    return list(le.classes_) if le else []

gender_choices = get_choices("Gender") or ["Male", "Female"]
job_choices = get_choices("Job Title") or ["Software Engineer", "Data Analyst"]
country_choices = get_choices("Country") or ["USA", "UK", "India"]
race_choices = get_choices("Race") or ["Asian", "White", "Black", "Hispanic"]

# Input fields
age = st.number_input("Age", 18, 100, 30)
gender = st.selectbox("Gender", gender_choices)
education = st.number_input("Education Level (1=Bachelor, 2=Master, 3=PhD)", 0, 10, 2)
job = st.selectbox("Job Title", job_choices)
experience = st.number_input("Years of Experience", 0.0, 50.0, 3.0, step=0.5)
country = st.selectbox("Country", country_choices)
race = st.selectbox("Race", race_choices)
senior = st.selectbox("Senior (1=Yes, 0=No)", [0, 1], index=0)

if st.button("Predict Salary"):
    try:
        df_input = pd.DataFrame([{
            "Age": age,
            "Gender": gender,
            "Education Level": education,
            "Job Title": job,
            "Years of Experience": experience,
            "Country": country,
            "Race": race,
            "Senior": senior
        }])

        # Encode categorical values
        for col in ["Gender", "Job Title", "Country", "Race"]:
            le = label_encoders[col]
            if df_input.at[0, col] not in le.classes_:
                df_input[col] = 0
            else:
                df_input[col] = le.transform([df_input.at[0, col]])[0]

        # Ensure column order
        order = ["Age", "Gender", "Education Level", "Job Title",
                 "Years of Experience", "Country", "Race", "Senior"]
        df_input = df_input[order]

        # Scale + Predict
        X_scaled = scaler.transform(df_input)
        pred = model.predict(X_scaled)[0]
        st.success(f"💰 Predicted Salary: ${pred:,.2f}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
