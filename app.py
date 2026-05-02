import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("🌱 Crop Recommendation App")

# Load dataset
data = pd.read_csv("crop_data.csv")

X = data[['N','P','K','temperature','humidity','rainfall','ph']]
y = data['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Simple Inputs
temp = st.number_input("🌡️ Temperature (°C)", min_value=0.0)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0)
rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0)

soil = st.selectbox("🌍 Soil Type", ["Sandy", "Loamy", "Clay", "Black"])

# Soil → NPK conversion
if soil == "Sandy":
    N, P, K = 40, 40, 40
elif soil == "Loamy":
    N, P, K = 80, 50, 50
elif soil == "Clay":
    N, P, K = 60, 60, 60
else:
    N, P, K = 90, 60, 60

ph = 6.5

# Prediction
if st.button("🌾 Recommend Crop"):
    data_input = np.array([[N, P, K, temp, humidity, rainfall, ph]])
    result = model.predict(data_input)
    st.success(f"🌱 Best Crop: {result[0]}")

