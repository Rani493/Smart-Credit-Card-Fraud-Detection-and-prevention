import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load('fraud_detection_model.pkl')

st.title(" Credit Card Fraud Detection App")
st.markdown("Upload a transaction or manually input details to test fraud detection.")

# File Upload
uploaded_file = st.file_uploader("Upload CSV file with transaction(s)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Show uploaded data
    st.subheader("Uploaded Transactions:")
    st.write(data)

    # Predict
    predictions = model.predict(data)
    data['Prediction'] = ['Fraud' if pred == 1 else 'Legit' for pred in predictions]

    st.subheader("Prediction Results:")
    st.write(data)
else:
    st.subheader("Or enter transaction manually:")

    # Replace 30 with the number of features your model was trained on
    num_features = 30
    feature_input = []
    for i in range(num_features):
        val = st.number_input(f"Feature {i + 1}", value=0.0)
        feature_input.append(val)

    if st.button("Predict"):
        input_array = np.array([feature_input])
        result = model.predict(input_array)[0]
        st.success("FRAUD Detected!" if result == 1 else " Transaction is Legit")
