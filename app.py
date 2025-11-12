import streamlit as st
import pandas as pd
import joblib
from streamlit_lottie import st_lottie
import requests

# ---------------- LOAD MODEL ----------------
model = joblib.load("salary_prediction_model.joblib")
scaler = joblib.load("scaler.joblib")
label_encoders = joblib.load("label_encoders.joblib")

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Salary Prediction App", page_icon="💼", layout="centered")

# ---------------- LOAD ANIMATION ----------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

money_anim = load_lottie("https://assets10.lottiefiles.com/packages/lf20_0fhlytwe.json")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    body, .stApp, .main, .block-container {
        padding: 0 !important;
        margin: 0 !important;
    }

    /* --- Centered Hero Section --- */
    .hero-section {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        width: 100%;
    }

    .title-text {
        font-size: 54px;
        font-weight: 800;
        color: #2c3e50;
        margin-bottom: 6px;
    }

    .subtitle-text {
        color: #7f8c8d;
        font-size: 18px;
        margin-bottom: 10px;
    }

    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 12px;
        padding: 12px 30px;
        font-size: 20px;
        font-weight: 600;
        border: none;
        transition: 0.3s;
        margin-top: 12px;
    }
    .stButton>button:hover {
        background-color: #2ecc71;
        transform: scale(1.05);
    }

    .back-icon {
        position: fixed;
        top: 20px;
        left: 25px;
        font-size: 28px;
        cursor: pointer;
        color: #2c3e50;
        text-decoration: none;
    }
    .back-icon:hover {
        color: #27ae60;
        transform: scale(1.1);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":
    # Top-centered layout with animation between text and button
    st.markdown("""
        <style>
        /* Remove Streamlit's default padding/margins */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
        }
        .main, .stApp {
            padding: 0 !important;
            margin: 0 !important;
        }

        /* Wrapper for centered layout */
        .hero-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            margin-top: 80px; /* space from top */
        }

        .hero-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px; /* equal spacing between items */
            max-width: 650px;
        }

        .title-text {
            font-size: 60px;
            font-weight: 800;
            color: #2c3e50;
            margin-bottom: 5px;
        }

        .subtitle-text {
            color: #7f8c8d;
            font-size: 20px;
            margin-bottom: 10px;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #3498db;
            color: white;
            border-radius: 12px;
            padding: 12px 40px;
            font-size: 20px;
            font-weight: 600;
            border: none;
            transition: 0.3s;
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: #2ecc71;
            transform: scale(1.05);
        }
        </style>
    """, unsafe_allow_html=True)

    # Centered hero section
    st.markdown("""
        <div class="hero-wrapper">
            <div class="hero-content">
                <div class="title-text">💼 Predict Salary</div>
                <div class="subtitle-text">
                    An AI-powered salary predictor based on experience, education, and job role.
                </div>
    """, unsafe_allow_html=True)

    # Add the animation between subtitle and button
    st_lottie(money_anim, speed=1, height=250, key="home_anim")

       # Center the Get Started button horizontally
    st.markdown("<div style='display:flex; justify-content:center; margin-top:10px;'>", unsafe_allow_html=True)
    if st.button("🚀 Get Started", key="get_started_btn"):
        st.session_state.page = "predict"
        try:
            st.rerun()
        except AttributeError:
            st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)


       



    # Close the divs
    st.markdown("</div></div>", unsafe_allow_html=True)






# ---------------- PREDICTION PAGE ----------------
elif st.session_state.page == "predict":
    if st.button("⬅️", key="back_btn"):
        st.session_state.page = "home"
        try:
            st.rerun()
        except AttributeError:
            st.experimental_rerun()

    st.markdown('<div style="text-align:center; font-size:28px; font-weight:700;">🧾 Enter Employee Details</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 18, 70, 30)
        education = st.selectbox("Education Level", [1, 2, 3], index=1, help="1 = Bachelor, 2 = Master, 3 = PhD")
        experience = st.number_input("Years of Experience", 0.0, 50.0, 3.0, step=0.5)
        senior = st.selectbox("Is Senior?", [0, 1])
    with col2:
        gender = st.selectbox("Gender", label_encoders["Gender"].classes_.tolist())
        job = st.selectbox("Job Title", label_encoders["Job Title"].classes_.tolist())
        country = st.selectbox("Country", label_encoders["Country"].classes_.tolist())
        race = st.selectbox("Race", label_encoders["Race"].classes_.tolist())

    st.markdown("<div style='display:flex; justify-content:center; margin-top:25px;'>", unsafe_allow_html=True)
    if st.button("💰 Predict Salary", use_container_width=False):
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

            for col in ["Gender", "Job Title", "Country", "Race"]:
                le = label_encoders[col]
                df_input[col] = le.transform(df_input[col])

            order = ["Age", "Gender", "Education Level", "Job Title",
                     "Years of Experience", "Country", "Race", "Senior"]
            df_input = df_input[order]

            scaled = scaler.transform(df_input)
            prediction = model.predict(scaled)[0]

            st.success(f"💰 Predicted Salary: ${prediction:,.2f}")
            st.balloons()
            st_lottie(money_anim, speed=1.2, height=250, key="result_anim")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    st.markdown("</div>", unsafe_allow_html=True)
