import streamlit as st
import requests
import joblib
import json
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="A Telco Customer's Churn Prediction",
    page_icon="📇",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/dinanirham',
        'Report a bug': "https://github.com/streamlit/streamlit/issues",
        'About': "This is web-based application for Author's very first classification model deployment on subject of StartUp's Success Prediction"
    }
)

st.title("A Telco Customer's Churn Prediction")
st.subheader("Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs")

Partner = st.selectbox("Does customer have partner?", ['No', 'Yes'])
tenure = st.number_input("How many months does customer's payment tenure take", value=24)
MultipleLines = st.selectbox("Does Multiple Lines's service customer signup for?", ['No', 'No phone service', 'Yes'])
InternetService = st.selectbox("Does Internet's service customer signup for?", ['DSL', 'Fiber optic', 'No'])
OnlineBackup = st.selectbox("Does Online Backup's service customer signup for?", ['No', 'No internet service', 'Yes'])
DeviceProtection = st.selectbox("Does Device Protection's service customer signup for?", ['No', 'No internet service', 'Yes'])
StreamingTV = st.selectbox("Does Streaming TV's service customer signup for?", ['No', 'No internet service', 'Yes'])
StreamingMovies = st.selectbox("Does Streaming Movies's service customer signup for?", ['No', 'No internet service', 'Yes'])
Contract = st.selectbox("What kind of periodical type does customer's contract take?", ['Month-to-month', 'One year', 'Two year'])
PaymentMethod = st.selectbox("What kind of transaction type does customer's payment take?", ['Bank transfer (automatic)', 'Credit card (automatic)',
        'Electronic check', 'Mailed check'])
MonthlyCharges = st.number_input("How much USD is customer's monthly charges?", value=65)
TotalCharges = st.number_input("How much USD is customer's total charges?", value=2250)

# inference
input_data = [Partner, tenure, MultipleLines, InternetService, OnlineBackup, DeviceProtection,
              StreamingTV, StreamingMovies, Contract, PaymentMethod, MonthlyCharges, TotalCharges]
columns = ['Partner', 'tenure', 'MultipleLines', 'InternetService', 'OnlineBackup', 'DeviceProtection', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
num_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']
cat_columns = ['Partner', 'MultipleLines', 'InternetService', 'OnlineBackup', 'DeviceProtection', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod']
norm_columns = ['tenure', 'MonthlyCharges']
skew_columns = ['TotalCharges']

with open('prep_pipeline.pkl', 'rb') as file_1:
  prep_pipeline = joblib.load(file_1)

input_data = pd.DataFrame([input_data], columns=columns)

new_data = prep_pipeline.transform(input_data).tolist()

# URL = "http://localhost:5000/startup_prediction" # sebelum push backend
URL = "https://irham-dinan-ftds-p2m1-bend.herokuapp.com/v1/models/churned_customer:predict"

# komunikasi
input_data_json = json.dumps({
    'signature_name':'serving_default',
    'instances':new_data
})

r = requests.post(URL, data=input_data_json)
result = r.json()
res = result['predictions']

for res in result['predictions']:
    if res[0] > 0.5:
        st.subheader("Customer is Churned")
    else:
        st.subheader("Customer is Retained")