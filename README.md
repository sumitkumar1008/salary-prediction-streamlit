💼 Salary Prediction Using Machine Learning & Streamlit

An AI-powered web application that predicts employee salaries based on multiple factors such as age, education level, job title, experience, country, race, and seniority.
This project uses Machine Learning models and is deployed as an interactive web app using Streamlit Cloud.

🚀 Live Demo

https://salary-prediction-app-3uxtwhfbs9qzqwsca7ossp.streamlit.app/

📌 Project Description

This project aims to estimate salaries using real-world data obtained from Kaggle:

The dataset was already clean (no missing values, no encoding required).

Features such as age, education, job title, experience, country, race, and seniority were used to predict salary.

Several machine learning models were trained and compared.

The best model was integrated into a Streamlit web application for user interaction.

The system can help job seekers, HR departments, and analysts understand expected salary ranges based on personal and professional details.

🧠 Features

✔ Predict salary based on multiple user inputs
✔ Simple and clean interface
✔ Ensemble ML model for high accuracy
✔ Real-time predictions
✔ Fully deployed using Streamlit
✔ Supports structured, real-world dataset

📊 Dataset

Source: Kaggle – Salary Data (Country & Race Based)
The dataset includes:

Feature	Description
Age	Age of the employee
Gender	Male/Female
Education Level	Bachelor/Master/PhD
Job Title	Various job roles
Years of Experience	Numerical
Country	Work location
Race	Demographic
Senior	1 = Senior Role, 0 = Non-Senior
Salary	Target variable
🛠️ Technologies Used

Python

Pandas, NumPy

Scikit-Learn

Random Forest, Gradient Boosting, Voting Regressor

Joblib

Streamlit

Google Colab

🔧 Model Development
Preprocessing

Dataset was clean → no encoding required

StandardScaler used for feature scaling

Train–test split applied

Target variable: Salary

Models Trained

Random Forest Regressor

Gradient Boosting Regressor

Voting Regressor (best performance)

The final saved model files include:

salary_prediction_model.joblib
scaler.joblib
label_encoders.joblib (only if categorical encoding existed)

🖥️ Streamlit Web App

The web app allows users to enter the following details:

Age

Gender

Education Level

Job Title

Years of Experience

Country

Race

Seniority

The model predicts salary instantly and displays it in a visually appealing interface.

📁 Project Structure
salary_prediction_streamlit/
│
├── app.py                         # Streamlit application
├── salary_prediction_model.joblib # Trained ML model
├── scaler.joblib                  # Scaler for preprocessing
├── Salary.csv                     # Dataset (optional)
├── requirements.txt               # Dependencies
└── README.md                      # Project documentation

▶️ Running the Project Locally
1. Clone the repository
git clone https://github.com/Ayush1344/salary_prediction_streamlit.git

2. Install dependencies
pip install -r requirements.txt

3. Run the Streamlit app
streamlit run app.py

🚀 Deployment

The application is deployed using Streamlit Cloud.
To deploy your own version:

Upload project to GitHub

Go to https://share.streamlit.io

Select your GitHub repo

Choose app.py as the main app file

Deploy

🙌 Conclusion

This project successfully demonstrates how machine learning can be used to predict salaries and assist job seekers and HR teams.
The clean UI and accurate predictions make this application practical and easy to use.

⭐ Support

If you like this project, don’t forget to star ⭐ the repository!
