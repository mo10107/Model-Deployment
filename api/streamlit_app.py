import streamlit as st
import requests
import os

st.title("Iris Flower Predictor")

sepal_length = st.slider('Sepal Length', 4.0, 8.0, 5.1)
sepal_width = st.slider('Sepal Width', 2.0, 4.5, 3.5)
petal_length = st.slider('Petal Length', 1.0, 7.0, 1.4)
petal_width = st.slider('Petal Width', 0.1, 2.5, 0.2)

# Get backend URL from environment variable
BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:5000")

if st.button('Predict'):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    try:
        res = requests.post(f"{BACKEND_URL}/predict", json={"features": features})
        if res.status_code == 200:
            prediction = res.json()['prediction']
            classes = ['Setosa', 'Versicolor', 'Virginica']
            st.success(f"Predicted class: **{classes[prediction]}**")
        else:
            st.error("Prediction failed. Server returned an error.")
    except Exception as e:
        st.error(f"Error: {e}")
